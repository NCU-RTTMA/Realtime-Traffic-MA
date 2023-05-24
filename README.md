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
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
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
