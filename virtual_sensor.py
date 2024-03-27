import paho.mqtt.client as mqtt_lib
import time
import random

# Configuration for connecting to ThingSpeak
channel_id = "2488423"
api_key = "B1L8UPH1N4ZL3RTS"
mqtt_client_id = "Hx8FMSc1NiscMwIFDTE1NTY"
user = "Hx8FMSc1NiscMwIFDTE1NTY"
passcode = "xlmjNREZ6+VwmgPLFEEtpkHl"

def handle_connect(mqtt_client, userdata, flags, result_code):
    # Handle the on_connect event
    if result_code == 0:
        print("Successfully connected with MQTT Broker")
    else:
        print("Connection failed with return code %d\n", result_code)

def send_sensor_data(mqtt_client):
    # Continuously send simulated sensor data
    while True:
        # Randomly generate sensor values
        temp_reading = random.uniform(-50, 50)  # Temperature in Celsius
        humidity_reading = random.uniform(0, 100)  # Humidity in percentage
        co2_reading = random.uniform(300, 2000)  # CO2 level in ppm

        # Format the data for ThingSpeak fields
        data_payload = f"field1={temp_reading}&field2={humidity_reading}&field3={co2_reading}"

        # MQTT topic for publishing data to ThingSpeak
        mqtt_topic = f"channels/{channel_id}/publish"

        # Publish the data to the specified MQTT topic
        publish_status = mqtt_client.publish(mqtt_topic, data_payload, qos=0)
        if publish_status[0] == 0:
            print(f"Published to {mqtt_topic}, Data: {data_payload}")
        else:
            print(f"Failed to publish to {mqtt_topic}")

        time.sleep(15)  # Wait for 15 seconds before sending next set of data

# Setup and initialization of MQTT client
mqtt_client = mqtt_lib.Client(mqtt_client_id)
mqtt_client.username_pw_set(user, passcode)
mqtt_client.on_connect = handle_connect

# Connect to the MQTT server
mqtt_client.connect("mqtt3.thingspeak.com", 1883, 60)
mqtt_client.loop_start()

try:
    # Start sending sensor data
    send_sensor_data(mqtt_client)
except KeyboardInterrupt:
    # Handle manual interruption (Ctrl + C)
    print("Data transmission stopped by user")
finally:
    # Cleanup and close the connection
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
