#!/bin/bash

# Start the FastAPI application with Uvicorn
cd /dealflow
nohup uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 > /dev/null 2>&1 &
