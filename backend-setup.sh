#!/bin/bash

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

# Start the service
systemctl start flask.service