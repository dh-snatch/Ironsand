# Set-up script adapted from https://altitude.otago.ac.nz/cosc349/vagrant-multivm


# replace all instances of http with https in sources.list, http connection was refused
# or not redirected when connecting to ubuntu repositories
sudo sed -i 's|http://|https://|g' /etc/apt/sources.list


apt-get update
      
# Placeholder password
export MYSQL_PWD='placeholder_password'


# MySQL installation
echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections 
echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections
apt-get -y install mysql-server

# Start MySQL service
service mysql start

# Create database called ironsand and a user called webuser with all privileges on the database
echo "CREATE DATABASE IF NOT EXISTS ironsand;" | mysql
echo "CREATE USER IF NOT EXISTS 'webuser'@'%' IDENTIFIED BY 'placeholder_password';" | mysql
echo "GRANT ALL PRIVILEGES ON ironsand.* TO 'webuser'@'%'" | mysql

export MYSQL_PWD='placeholder_password'

# see db.sql for the database schema, only contains the deposit table
cat /vagrant/db.sql | mysql -u webuser ironsand

# Allow remote connections to MySQL server   
sed -i'' -e '/bind-address/s/127.0.0.1/0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf

# Restart MySQL service to apply changes
service mysql restart
