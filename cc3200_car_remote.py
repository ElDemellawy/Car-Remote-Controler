#!/usr/bin/env python3
"""
HTTP Server for CC3200 Car Door Controller (Fixed)

This server receives HTTP commands from the CC3200
and provides a web interface for testing.

Author: Abdelrahman Mohamed
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
import time
from datetime import datetime

# Configuration
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 8080

# Car door state
car_door_status = "locked"
last_command = None
last_command_time = None
cc3200_status = None
last_cc3200_update = None

class CarDoorHTTPHandler(BaseHTTPRequestHandler):
    """
    HTTP handler for car door lock/unlock commands
    """
    
    def do_GET(self):
        """
        Handle GET requests - return car door status
        """
        if self.path == "/" or self.path == "/car/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>CC3200 Car Door Controller - HTTP</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }}
                    .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                    h1 {{ color: #333; text-align: center; }}
                    .button {{ background-color: #4CAF50; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin: 10px; }}
                    .button:hover {{ background-color: #45a049; }}
                    .button:active {{ background-color: #3d8b40; }}
                    .status {{ padding: 15px; margin: 20px 0; border-radius: 5px; }}
                    .status.locked {{ background-color: #ffebee; color: #c62828; border: 1px solid #ef9a9a; }}
                    .status.unlocked {{ background-color: #e8f5e8; color: #2e7d32; border: 1px solid #a5d6a7; }}
                    .info {{ background-color: #e3f2fd; padding: 15px; border-radius: 5px; margin: 20px 0; }}
                    .log {{ background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0; max-height: 200px; overflow-y: auto; }}
                    .cc3200-status {{ background-color: #fff3e0; padding: 15px; border-radius: 5px; margin: 20px 0; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🚗 CC3200 Car Door Controller (HTTP)</h1>
                    
                    <div class="info">
                        <h3>📡 HTTP Server Status</h3>
                        <p><strong>Server:</strong> {HOST}:{PORT}</p>
                        <p><strong>CC3200 IP:</strong> 192.168.0.105</p>
                        <p><strong>Endpoints:</strong></p>
                        <ul>
                            <li>GET /car/status - Get car door status</li>
                            <li>POST /lock - Lock car door</li>
                            <li>POST /unlock - Unlock car door</li>
                            <li>POST /api/car/status - CC3200 status updates</li>
                        </ul>
                    </div>
                    
                    <div class="status {'unlocked' if car_door_status == 'unlocked' else 'locked'}" id="carDoorStatus">
                        <h3>🚗 Car Door Status: {car_door_status.upper()}</h3>
                    </div>
                    
                    <div class="cc3200-status" id="cc3200Status">
                        <h3>📱 CC3200 Status</h3>
                        <p><strong>Connection:</strong> {'Connected' if cc3200_status else 'Disconnected'}</p>
                        <p><strong>Last Update:</strong> {last_cc3200_update.strftime('%H:%M:%S') if last_cc3200_update else 'Never'}</p>
                    </div>
                    
                    <div style="text-align: center;">
                        <button class="button" onclick="sendCommand('lock')">🔒 LOCK CAR</button>
                        <button class="button" onclick="sendCommand('unlock')">🔓 UNLOCK CAR</button>
                    </div>
                    
                    <div class="log">
                        <h4>📨 Recent Activity:</h4>
                        <div id="activityLog">
                            <div>Server started at {datetime.now().strftime('%H:%M:%S')}</div>
                            <div>Waiting for CC3200 connection...</div>
                        </div>
                    </div>
                </div>
                
                <script>
                    function sendCommand(command) {{
                        fetch('/' + command, {{
                            method: 'POST',
                            headers: {{ 'Content-Type': 'application/json' }},
                            body: JSON.stringify({{ command: command }})
                        }})
                        .then(response => response.json())
                        .then(data => {{
                            addLog(`Command sent: ${{command}}`);
                            updateStatus(data.status);
                        }})
                        .catch(error => {{
                            addLog(`Error: ${{error}}`);
                        }});
                    }}
                    
                    function updateStatus(status) {{
                        const statusDiv = document.getElementById('carDoorStatus');
                        if (status === 'unlocked') {{
                            statusDiv.className = 'status unlocked';
                            statusDiv.innerHTML = '<h3>🚗 Car Door Status: UNLOCKED</h3>';
                        }} else {{
                            statusDiv.className = 'status locked';
                            statusDiv.innerHTML = '<h3>🚗 Car Door Status: LOCKED</h3>';
                        }}
                    }}
                    
                    function addLog(message) {{
                        const logDiv = document.getElementById('activityLog');
                        const timestamp = new Date().toLocaleTimeString();
                        logDiv.innerHTML += `<div>[${{timestamp}}] ${{message}}</div>`;
                        logDiv.scrollTop = logDiv.scrollHeight;
                    }}
                    
                    // Auto-refresh status every 5 seconds
                    setInterval(() => {{
                        fetch('/car/status')
                        .then(response => response.json())
                        .then(data => {{
                            updateStatus(data.status);
                        }});
                    }}, 5000);
                </script>
            </body>
            </html>
            """
            
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """
        Handle POST requests for car door lock/unlock commands
        """
        global car_door_status, last_command, last_command_time, cc3200_status, last_cc3200_update
        
        if self.path == "/lock":
            car_door_status = "locked"
            last_command = "lock"
            last_command_time = datetime.now()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "result": "success",
                "action": "lock",
                "status": "locked",
                "timestamp": datetime.now().isoformat()
            }
            
            self.wfile.write(json.dumps(response).encode())
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Car door LOCKED via HTTP")
            
        elif self.path == "/unlock":
            car_door_status = "unlocked"
            last_command = "unlock"
            last_command_time = datetime.now()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "result": "success",
                "action": "unlock",
                "status": "unlocked",
                "timestamp": datetime.now().isoformat()
            }
            
            self.wfile.write(json.dumps(response).encode())
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Car door UNLOCKED via HTTP")
            
        elif self.path == "/api/car/status":
            # Handle CC3200 status updates
            cc3200_status = True
            last_cc3200_update = datetime.now()
            
            # Read the JSON payload from CC3200
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                print(f"[{datetime.now().strftime('%H:%M:%S')}] CC3200 Status Update: {data}")
                
                # Update car door status if provided
                if 'status' in data:
                    car_door_status = data['status']
                
            except Exception as e:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Error parsing CC3200 status: {e}")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "result": "success",
                "message": "Status received",
                "timestamp": datetime.now().isoformat()
            }
            
            self.wfile.write(json.dumps(response).encode())
            print(f"[{datetime.now().strftime('%H:%M:%S')}] CC3200 status update received")
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {"error": "Invalid endpoint"}
            self.wfile.write(json.dumps(response).encode())
    
    def log_message(self, format, *args):
        """
        Custom logging to show CC3200 connections
        """
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {format % args}")

def start_server():
    """
    Start the HTTP server
    """
    try:
        server = HTTPServer((HOST, PORT), CarDoorHTTPHandler)
        print(f"=== CC3200 HTTP Car Door Server (Fixed) ===")
        print(f"Server started on {HOST}:{PORT}")
        print(f"Web interface: http://localhost:{PORT}")
        print()
        print("Waiting for CC3200 connections...")
        print("Press Ctrl+C to stop")
        print()
        
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    start_server() 