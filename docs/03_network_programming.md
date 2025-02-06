# Network programming
## 1. Socket programming


> "What's the difference between TCP and UDP? When would we use each?"


> "TCP (Transmission Control Protocol) is a **connection-oriented** protocol that ensures **reliable, ordered, and error-checked data transmission**. It is used in applications like HTTP, FTP, and SSH.
> UDP (User Datagram Protocol) is a **connectionless** protocol that is **faster but unreliable**. It is used in **real-time applications** like VoIP, gaming, and live streaming."

------


> "How do we implement a basic TCP server and client in Python?"


```python
# TCP Server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP Socket
server.bind(("127.0.0.1", 5000))  # bind IP and port
server.listen(5)  # listen

print("Server listening on port 5000...")
conn, addr = server.accept()  # accept connection
print(f"Connection from {addr}")

data = conn.recv(1024).decode()  # receive data
print(f"Received: {data}")
conn.send("Hello from server!".encode())  # send data
conn.close()
```

```python
# TCP Client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))  # connect server
client.send("Hello Server".encode())  # send data
response = client.recv(1024).decode()  # receive server's response
print(f"Server Response: {response}")
client.close()
```

✅ **Applicable scenarios:**

- **TCP Suitable for reliable data transfer** (e.g. Web, database connection)
- **UDP Suitable for low latency applications** (e.g. gaming, live streaming)

## 2. Requests

> "How do we send an HTTP GET request in Python using `requests`?"

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # HTTP status code
print(response.json())  # analyse JSON response
```

✅ **Applicable to calling REST APIs, e.g. third-party APIs, database APIs**

------

> "How do we handle request timeouts in `requests`?"

```python
try:
    response = requests.get("https://api.github.com", timeout=3)  # 3 seconds timeout
    response.raise_for_status()  # check HTTP error
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

✅ **Timeout applies to avoid network latency affecting application performance**

------

> "How can we optimize HTTP requests for performance?"

- Use `Session()` to reuse connections:

```python
session = requests.Session()
response = session.get("https://api.github.com")
```
 - Use `ThreadPoolExecutor` for concurrent requests:
```python
from concurrent.futures import ThreadPoolExecutor
urls = ["https://api.github.com", "https://www.python.org"]
with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(requests.get, urls)
```
- Use gzip compression:
```python
response = requests.get("https://api.github.com", headers={"Accept-Encoding": "gzip"})
```

✅ **Suitable for highly concurrent API requests, such as crawlers, data collection**


## 3. Flask 和 FastAPI

> "How do we create a basic REST API using Flask?"

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
```

✅ **For small Web services and APIs**

------


> "Why is FastAPI faster than Flask?"

> "FastAPI is built on **ASGI (Asynchronous Server Gateway Interface)** and uses **async/await** for high-performance asynchronous processing, making it faster than Flask, which is synchronous."

------


> "How do we implement an async API in FastAPI?"


```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/async-api")
async def async_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com")
    return response.json()
```

✅ **For high concurrency Web APIs, such as financial trading systems.**


## **4. Summary**

| Themes | Key Concepts | Code Samples |
| ------------ | ------------------------- | ----------------------------------- |
| **Sockets** | TCP vs UDP, server/client | `socket.bind()`, `recv()`, `send()` |
| **Requests** | HTTP request optimization, timeout handling | `requests.get()`, `session` |
| **Flask** | REST API, JSON response | `Flask(route='/api')` |
| **FastAPI** | Asynchronous API, Performance Optimization | `async def`, `httpx` |