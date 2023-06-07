# [WIP] Realtime Traffic Monitoring & Analysis

This is a simple backend server which performs realtime traffic monitoring and anaysis.

We currently generate fake car data to test the system.

## Tasks
- [x] REDIS/MongoDB Connection
- [x] WebSocket Connection
- [x] Car record caching
- [x] User report event handling
- [ ] Car path tracing

## Libraries/Frameworks
- flask
- flask_socketio
- flask_rest
- redis-py
- mongoengine/pymongo
- Docker / Docker Compose

## Folder Structure
- project
  - app.py : The root application script
  - cache.py : For cache handling between REDIS and MongoDB
  - api : REST API scripts
    - car.py
    - user.py
  - models : Persistent MongoDB models
    - car.py
    - user.py
  - templates
    - test.html


## Running the Server

The application has been wrapped into a Docker Compose package.

### Step 1: Build the images
```bash
docker compose build
```

### Step 2: Launch the containers
```bash
docker compose up -d
```
Note: Remove the `-d` parameter to see the real-time console logs
