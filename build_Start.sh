#!/bin/bash

cd backend
docker build -t bragapp_backend .
docker run -p 5000:5000 -d --restart unless-stopped --env-file .env bragapp_backend


cd ..
cd frontend
docker build -t bragapp_frontend .
docker run -p 8080:8080 -d --restart unless-stopped bragapp_frontend
