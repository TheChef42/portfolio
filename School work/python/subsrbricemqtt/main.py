import requests

arduino_ip = "172.17.199.206"  # Replace with your Arduino's IP address
arduino_port = 65280  # Default OTA port for Arduino
username = "Arduino"  # Replace with your Arduino's username
password = "password"  # Replace with your Arduino's password

# URL to the new firmware to be flashed
firmware_url = "https://p5test.blob.core.windows.net/binfiles/Blink.ino.with_bootloader.bin"

# Send an HTTP request to start the OTA update with username and password
response = requests.get(f"http://{username}:{password}@{arduino_ip}:{arduino_port}/update?path={firmware_url}")

if response.status_code == 200:
    print(response.status_code)
    print("OTA update started successfully.")
else:
    print(response.status_code)
    print("Failed to start OTA update.")