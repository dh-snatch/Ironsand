#!/bin/bash

# replace all instances of http with https in sources.list, http connection was refused
# or not redirected when connecting to ubuntu repositories
sudo sed -i 's|http://|https://|g' /etc/apt/sources.list

# Update packages
apt-get update -y

# Install Python3 and pip
apt-get install -y python3 python3-pip

# Install Flask and MySQL connector
pip3 install flask mysql-connector-python

# Systemd service file to start the Flask app automatically
cp /vagrant/flask.service /etc/systemd/system/flask.service

systemctl daemon-reload

systemctl enable flask.service

# Start the Flask service
systemctl start flask.service