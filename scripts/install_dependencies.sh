#!/bin/bash

# Install required dependencies
apt-get update
apt-get install -y python3-pip
pip3 install uvicorn
pip3 install -r /dealflow/requirements.txt
