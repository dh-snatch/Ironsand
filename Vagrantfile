
Vagrant.configure("2") do |config|


    config.vm.box = "bento/ubuntu-22.04"

    config.vm.synced_folder ".", "/vagrant"
    # frontend set up
    config.vm.define "frontend" do |frontend|
    frontend.vm.hostname = "frontend"

    
    # Only the frontend VM needs port forwarding , it is the point of entry to the application
    frontend.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    
    # private network for communication between VMs 192.168.56.x
    frontend.vm.network "private_network", ip: "192.168.56.11"
    # link to shell script
    frontend.vm.provision "shell", path: "frontend-setup.sh"
    end
    # database set up
    config.vm.define "database" do |database|
    database.vm.hostname = "database"
    database.vm.network "private_network", ip: "192.168.56.12"
    database.vm.provision "shell", path: "database-setup.sh"
    end
    # backend set up
    config.vm.define "backend" do |backend|
    backend.vm.hostname = "backend"
    backend.vm.network "private_network", ip: "192.168.56.13"
    backend.vm.provision "shell", path: "backend-setup.sh"
    end
end





