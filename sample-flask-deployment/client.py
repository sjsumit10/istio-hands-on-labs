import os
import requests
import time

# Get server host and port from environment variable
PING_SVC_HOST = os.getenv("PING_HOST", "localhost")
PING_SVC_PORT = os.getenv("PING_PORT", "8000")
PING_INTERVAL = os.getenv("PING_INTERVAL", 1)

def call_ping():
    while True:
        try:
            response = requests.get(f"http://{PING_SVC_HOST}:{PING_SVC_PORT}/ping")
            print(f"Response: {response.text}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        time.sleep(int(PING_INTERVAL))

if __name__ == "__main__":
    call_ping()
