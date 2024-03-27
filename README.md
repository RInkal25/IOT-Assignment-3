# IoT Assignment Repository

Welcome to my IoT Assignment Repository!

This repository contains the code and scripts needed to complete my cloud-based IoT system assignment.

## Assignment Overview
In this assignment, I am required to:
- Build a cloud-based IoT system that collects data from virtual sensors using the MQTT protocol.
- Display the latest sensor data values from all sensors of a specified environmental station.
- Display the sensor data values received during the last five hours from all environmental stations of a specified sensor.

## Files Included
1. **virtual_sensor.py**: This Python program represents the virtual environment IoT station. It periodically generates random virtual sensor values for temperature, humidity, and CO2 sensors.

2. **latest_data.m**: This MATLAB code fetches and displays the latest sensor data values from the cloud-based IoT system.

3. **last_5_hours_data.m**: This MATLAB code fetches and displays the sensor data values received during the last five hours from the cloud-based IoT system.

4. **thingspeak_publish.json**: This JSON file contains data to be published to the ThingSpeak channel, representing the sensor data collected by the IoT system.

## Cloud-based IoT Backend
The cloud-based backend is implemented using ThingSpeak.

Happy coding!
