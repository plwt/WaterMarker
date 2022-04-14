#!/bin/bash

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

# make folders
# mkdir -p ./opt/WaterMarker/src/images

# run the script
python3 /opt/WaterMarker/src/WaterMarker.py

sleep 30m
