#!/bin/bash
#pip install virtualenv

# Create DEV env and activate it
virtualenv dev
source dev/bin/activate

# Install prerequisites 
pip install -r requirements.txt
# Install Monstr in dev mode
pip install -e . 

#deactivate
