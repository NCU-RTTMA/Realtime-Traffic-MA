# [WIP] Realtime Traffic Monitoring & Analysis

This is a simple backend server which performs realtime traffic monitoring and anaysis.

We currently generate fake car data to test the system.

## Tasks
- [x] REDIS/MongoDB Connection
- [x] WebSocket Connection
- [ ] Car record caching
- [ ] User report event handling
- [ ] Car path tracing

## Libraries/Frameworks
- flask
- flask_socketio
- flask_rest
- flask_redis
- mongoengine/pymongo

## Folder Structure
- project
  - app.py : The root application script
  - cache.py : For cache handling between REDIS and MongoDB
  - websocket.py : For handling WebSocket events
  - serve.sh : A simple startup script
  - stop.sh : A script to shutdown databases
  - api : REST API scripts
    - car.py
    - user.py
  - models : Persistent MongoDB models
    - car.py
    - user.py
  - templates
    - test.html


## Running the Server

### 1. Install Redis
```bash
sudo apt install
```

### 2. Install pip dependencies
```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install pip packages
pip install -r requirements.txt
```

### 3. Ensure databases have been shutdown
```bash
sudo bash ./stop.sh
```

### 4. Starting the server
```bash
sudo bash ./serve.sh
```
