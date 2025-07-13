# Automotive Dashboard - MQTT Implementation

This Android application provides an automotive dashboard with MQTT-based communication for car door control and sensor data monitoring.

## Features

- **MQTT Communication**: Uses MQTT protocol instead of HTTP/REST for better reliability
- **Car Door Control**: Lock and unlock car doors via MQTT commands
- **Sensor Data Display**: Real-time display of temperature, humidity, pressure, and car door status
- **Location Services**: Distance calculation from home location
- **Connection Status**: Real-time MQTT connection status monitoring

## Architecture

### MQTT Topics

- `automotive/car_door/commands` - Car door control commands (lock/unlock)
- `automotive/sensors/data` - Sensor data (temperature, humidity, pressure, etc.)
- `automotive/car_door/status` - Car door status updates

### Components

1. **MqttService.kt** - Singleton MQTT service for connection management
2. **SensorData.kt** - Data class for sensor data with JSON parsing
3. **MainActivity.kt** - Main UI with MQTT integration
4. **mqtt_test_broker.py** - Python script for testing MQTT communication

## Setup Instructions

### Android App Setup

1. **Open the project in Android Studio**
   ```bash
   # Open Android Studio and import the project
   ```

2. **Build and run the app**
   - Connect your Android device or start an emulator
   - Click "Run" in Android Studio
   - The app will automatically connect to the MQTT broker

### Testing with Python Simulator

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the MQTT test broker**
   ```bash
   python mqtt_test_broker.py
   ```

3. **Test the communication**
   - The Python script will publish sensor data every 5 seconds
   - Use the Android app to send car door commands
   - Watch the real-time updates in both the app and Python console

## Configuration

### MQTT Broker Settings

The app uses HiveMQ's public broker for testing:
- **Broker URL**: `tcp://broker.hivemq.com:1883`
- **Client ID**: `AutomotiveDashboard_[timestamp]`

### Home Location

Update the home coordinates in `MainActivity.kt`:
```kotlin
private val homeLat = 30.123456  // Replace with your home latitude
private val homeLon = 31.654321  // Replace with your home longitude
```

## Dependencies

### Android Dependencies
- `org.eclipse.paho:org.eclipse.paho.client.mqttv3:1.2.5`
- `org.eclipse.paho:org.eclipse.paho.android.service:1.1.1`
- `com.google.code.gson:gson:2.10.1`

### Python Dependencies
- `paho-mqtt==1.6.1`

## Usage

### Android App

1. **Launch the app** - It will automatically connect to the MQTT broker
2. **Monitor connection status** - Check the top status indicator
3. **View sensor data** - Real-time sensor readings are displayed
4. **Control car door** - Use the "Unlock Car Door" and "Lock Car Door" buttons
5. **Check distance** - View your distance from home

### Python Simulator

1. **Start the simulator** - Run `python mqtt_test_broker.py`
2. **Monitor output** - Watch for incoming car door commands
3. **Check sensor data** - Verify data is being published
4. **Test car door control** - Send commands from the Android app

## Troubleshooting

### Common Issues

1. **Connection Failed**
   - Check internet connectivity
   - Verify the broker URL is accessible
   - Ensure the app has internet permissions

2. **No Sensor Data**
   - Make sure the Python simulator is running
   - Check that both devices are connected to the same MQTT broker
   - Verify topic subscriptions

3. **Car Door Commands Not Working**
   - Ensure the Python simulator is listening for commands
   - Check the MQTT topic names match
   - Verify the command format (lowercase "lock"/"unlock")

### Debug Information

- Check Android Studio Logcat for MQTT connection logs
- Monitor Python console output for incoming commands
- Use MQTT client tools (like MQTT Explorer) to monitor topics

## Security Notes

- The current implementation uses a public MQTT broker for testing
- For production use, implement authentication and use a private broker
- Consider using TLS/SSL for secure communication
- Implement proper error handling and reconnection logic

## Author

**Mohamed Eldemellawy** - Embedded Software Engineer

## License

This project is for educational and testing purposes. 