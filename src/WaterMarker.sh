#!/bin/bash

python3 -m venv venv
source venv/bin/activate

# install requirements
python pip install pillow

# make folders
mkdir -p ./home/WaterMark

# run the script
python3 /opt/WaterMarker/src/WaterMarker.py

sleep 30m
