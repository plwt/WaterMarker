# create folder for virtual environment
mkdir python-virtual-environments

# go to the folder
cd python-virtual-environments

# create virtual environment
python3 -m venv wm-env

# activate virtual environment
source wm-env/bin/activate

# install requirements
python3 pip install pillow

# run the script
python3 WaterMarker.py

sleep 30m

# deactivate virtual environment
deactivate

# clean up
rm -rf wm-env