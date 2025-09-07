Ironsand is a virtualised application for recording geological samples and displaying them on a map. The application is deployed across 3 VMs, and requires both Vagrant and VirtualBox to set up and use.

# To start 
[VirtualBox version: 7.2.0](https://www.virtualbox.org/wiki/Downloads)
[Vagrant 2.4.9](https://developer.hashicorp.com/vagrant/downloads)

# Structure of the repository

The frontend VM is responsible for serving static HTML, CSS, JS, and PHP files on an apache server. 
PHP acts as an intermediary between the browser and the backend flask server. All map related code 
operates in the browser using Leaflet (see )

The backend VM runs a Flask application as an API, and communicates with PHP files on the frontend.  
All endpoints currently run on main.py, as the application is fairly limited in scope. 

The database VM is just a MySQL database, with some test data populated and ready to go. Database name, password, and
user can be changed in the .env file for convenience (add this to gitignore).

Backend-setup, database-setup, and frontend-setup are shell scripts to automate VM processes.
To have additional python files run in the background, you can create a similar file to flask.service, cp it over to /etc/systemd/system/yourfilename, and start it with systemctl in backend-setup.sh.

Sometimes the VM hangs and won't boot for a while, but opening the machine's GUI in virtual box seems to fix the problem. 
For now, I have increased the timeout to 5 minutes in the vagrantfile. 
