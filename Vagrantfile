
Vagrant.configure("2") do |config|


    config.vm.box = "bento/ubuntu-22.04"
    config.vm.boot_timeout = 300



    # frontend set up
    config.vm.define "frontend" do |frontend|
    frontend.vm.hostname = "frontend"

    # default memory was 3GB, kept crashing my laptop and cs lab machines
    frontend.vm.provider "virtualbox" do |vb|
        vb.memory = 1024
        vb.cpus = 1
    end
    
    # Only the frontend VM needs port forwarding , it is the point of entry to the application
    frontend.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    frontend.vm.synced_folder ".", "/vagrant"
    # private network for communication between VMs 192.168.56.x
    frontend.vm.network "private_network", ip: "192.168.56.11"
    # link to shell script
    frontend.vm.provision "shell", path: "frontend-setup.sh"
    end
    # database set up
    config.vm.define "database" do |database|
    database.vm.hostname = "database"
    # default memory was 3GB, kept crashing my laptop and cs lab machines
    database.vm.provider "virtualbox" do |vb|
        vb.memory = 1024
        vb.cpus = 1
    end
    database.vm.network "private_network", ip: "192.168.56.12"
    database.vm.synced_folder ".", "/vagrant"
    database.vm.provision "shell", path: "database-setup.sh"
    end
    # backend set up
    config.vm.define "backend" do |backend|
    backend.vm.hostname = "backend"

    # default memory was 3GB, kept crashing my laptop and cs lab machines
    backend.vm.provider "virtualbox" do |vb|
        vb.memory = 1024
        vb.cpus = 1
    end
    backend.vm.network "private_network", ip: "192.168.56.13"
    backend.vm.synced_folder ".", "/vagrant"
    backend.vm.provision "shell", path: "backend-setup.sh"
    end




end





