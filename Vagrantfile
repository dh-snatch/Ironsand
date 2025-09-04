
Vagrant.configure("2") do |config|



    config.vm.box = "bento/ubuntu-22.04"

    config.vm.define "frontend" do |frontend|
    frontend.vm.hostname = "frontend"
    
    
    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine and only allow access
    # via 127.0.0.1 to disable public access
    frontend.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    

    # this address is for communicating between VMs
    frontend.vm.network "private_network", ip: "192.168.56.11"

    frontend.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y apache2
      sudo cp /vagrant/website.conf /etc/apache2/sites-available/
      sudo a2ensite website.conf
      sudo a2dissite 000-default
      sudo systemctl reload apache2
    SHELL
  end

    config.vm.define "database" do |database|
    database.vm.hostname = "database"
    
    # this address is for communicating between VMs
    database.vm.network "private_network", ip: "192.168.56.12"

    database.vm.provision "shell", path: "database-setup.sh"

    end




end





