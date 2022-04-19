#!/bin/bash

cd /opt/WaterMarker

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python3 -m pip install --upgrade pathlib

# make folders
mkdir -p ~/WaterMarker
mkdir /opt/WaterMarker/images

# run the script
python3 /opt/WaterMarker/src/WaterMarker.py

sleep 5m

deactivate

rm -r venv
