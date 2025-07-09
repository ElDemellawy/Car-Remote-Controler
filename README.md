# Car Remote Controller

A comprehensive car remote control system consisting of an Android application, Arduino-based hardware controller, and Python HTTP server for car control and sensor monitoring.

## Project Overview

This project provides a complete solution for remote car control with real-time sensor monitoring. The system includes:

- **Android App**: User interface for controlling car locks and viewing sensor data
- **Arduino Controller**: Hardware interface for car lock control and sensor reading
- **Python HTTP Server**: Backend server for handling HTTP requests and sensor data

## Features

- **Car Remote Control**: Lock and unlock car doors remotely
- **Real-time Sensor Monitoring**: Temperature, humidity, and other sensor data
- **HTTP-based Communication**: RESTful API for reliable communication
- **Distance Calculation**: Calculate distance from home location
- **Connection Status Monitoring**: Real-time connection status

## Project Structure

```
Car-Remote-Controler/
├── app/                          # Android application
│   ├── src/main/java/           # Kotlin source code
│   ├── src/main/res/            # Android resources
│   └── build.gradle.kts         # Android build configuration
├── cc3200_car_remote.ino # Arduino code for car control
├── cc3200_car_remote.py  # Python HTTP server
└── README.md                    # This file
```

## Components

### 1. Android Application (`app/`)

The Android app provides the user interface for:
- Sending car lock/unlock commands
- Displaying real-time sensor data
- Monitoring connection status
- Calculating distance from home

**Key Files:**
- `MainActivity.kt` - Main UI and HTTP communication
- `activity_main.xml` - User interface layout
- `AndroidManifest.xml` - App permissions and configuration

### 2. Arduino Controller (`cc3200_car_remote.ino`)

The Arduino code handles:
- Car door lock/unlock control
- Sensor data collection
- HTTP server communication
- Hardware interface management

### 3. Python HTTP Server (`cc3200_car_remote.py`)

The Python server provides:
- HTTP API endpoints for car door lock/unlock control
- Sensor data processing and storage
- Communication bridge between Android app and Arduino
- Data logging and monitoring

## Setup Instructions

### Prerequisites

- Android Studio (for Android development)
- Arduino IDE (for Arduino code)
- Python 3.x with required packages
- CC3200 LaunchPad or compatible Arduino board
- Car lock/unlock interface and sensors

### Android App Setup

1. **Open the project in Android Studio**
   ```bash
   # Open Android Studio and import the project
   # Navigate to the app/ directory
   ```

2. **Build and run the app**
   - Connect your Android device or start an emulator
   - Click "Run" in Android Studio
   - The app will connect to the Python HTTP server

### Arduino Setup

1. **Upload the Arduino code**
   - Open `cc3200_car_remote.ino` in Arduino IDE
   - Connect your CC3200 LaunchPad
   - Upload the code to the board

2. **Connect hardware**
   - Connect car door lock/unlock interface to appropriate pins
   - Connect sensors (temperature, humidity, etc.)
   - Ensure proper power supply

### Python Server Setup

1. **Install Python dependencies**
   ```bash
   pip install flask requests
   ```

2. **Run the HTTP server**
   ```bash
   python cc3200_car_remote.py
   ```

3. **Configure server settings**
   - Update IP address and port if needed
   - Configure sensor data endpoints
   - Set up car lock/unlock endpoints

## API Endpoints

### Car Remote Control
- `POST /car/lock` - Lock car doors
- `POST /car/unlock` - Unlock car doors
- `GET /car/status` - Get car lock status

### Sensor Data
- `GET /sensors/temperature` - Get temperature reading
- `GET /sensors/humidity` - Get humidity reading
- `GET /sensors/all` - Get all sensor data

## Configuration

### Android App Configuration

Update the server URL in `MainActivity.kt`:
```kotlin
private val serverUrl = "http://192.168.1.100:5000"  // Replace with your server IP
```

### Arduino Configuration

Update WiFi credentials in `cc3200_car_remote.ino`:
```cpp
const char* ssid = "YourWiFiSSID";
const char* password = "YourWiFiPassword";
```

### Python Server Configuration

Update server settings in `cc3200_car_remote.py`:
```python
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5000        # Server port
```

## Usage

### Android App

1. **Launch the app** - It will connect to the Python HTTP server
2. **Monitor connection status** - Check the top status indicator
3. **Control car locks** - Use the lock/unlock buttons to control car doors
4. **View sensor data** - Real-time sensor readings are displayed
5. **Check distance** - View your distance from home

### Arduino Controller

1. **Power on the Arduino** - It will connect to WiFi and start the HTTP server
2. **Monitor serial output** - Check for connection status and sensor readings
3. **Test car lock/unlock** - Send lock/unlock commands from the Android app
4. **Verify sensor data** - Ensure sensors are working properly

### Python Server

1. **Start the server** - Run `python cc3200_car_remote.py`
2. **Monitor logs** - Watch for incoming requests and sensor data
3. **Test endpoints** - Use a web browser or Postman to test API endpoints
4. **Check data flow** - Verify communication between all components

## Troubleshooting

### Common Issues

1. **Connection Failed**
   - Check WiFi connectivity on Arduino
   - Verify server IP address in Android app
   - Ensure Python server is running

2. **No Sensor Data**
   - Check sensor connections on Arduino
   - Verify sensor code in Arduino sketch
   - Test individual sensors

3. **Car Lock/Unlock Commands Not Working**
   - Check car lock interface connections
   - Verify pin assignments in Arduino code
   - Test lock/unlock manually

4. **Android App Issues**
   - Check internet permissions in AndroidManifest.xml
   - Verify server URL configuration
   - Check Android Studio logs

### Debug Information

- **Arduino**: Monitor serial output for connection and sensor data
- **Python Server**: Check console output for HTTP requests
- **Android**: Use Android Studio Logcat for app debugging
- **Network**: Use network tools to verify connectivity

## Security Considerations

- The current implementation uses HTTP (not HTTPS) for simplicity
- For production use, implement HTTPS and authentication
- Consider using a private network or VPN
- Implement proper error handling and validation

## Hardware Requirements

- CC3200 LaunchPad or compatible Arduino board
- Car door lock/unlock interface and relays
- Temperature and humidity sensors
- WiFi connectivity
- Power supply for Arduino and car lock system

## Dependencies

### Android Dependencies
- Android SDK and build tools
- HTTP client libraries
- JSON parsing libraries

### Arduino Dependencies
- WiFi library
- HTTP client library
- Sensor libraries (DHT, etc.)

### Python Dependencies
- Flask web framework
- Requests library
- Additional sensor libraries as needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and testing purposes. Use at your own risk.

## Support

For issues and questions:
- Check the troubleshooting section
- Review the code comments
- Test individual components
- Verify hardware connections 