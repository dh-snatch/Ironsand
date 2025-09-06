#!/bin/bash 
   

# replace all instances of http with https in sources.list, http connection was refused
# or not redirected when connecting to ubuntu repositories
sudo sed -i 's|http://|https://|g' /etc/apt/sources.list

apt-get update -y

# Install Apache and PHP
apt-get install -y apache2 php libapache2-mod-php php-mysql

# Copy over configuration file for Apache
cp /vagrant/website.conf /etc/apache2/sites-available/

# Disable default site and enable frontend site
a2dissite 000-default
a2ensite website.conf

# Restart Apache to apply changes
sudo systemctl reload apache2