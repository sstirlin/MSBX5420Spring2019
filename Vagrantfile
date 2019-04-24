# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/bionic64"
  config.disksize.size = '50GB'

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8888, host: 8888

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  #config.vm.synced_folder "C:/projects", "/home/vagrant/projects"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Don't boot with headless mode
    vb.gui = true
  
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "4096"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    #if Vagrant::Util::Platform.windows? then
    #	vb.customize ["storageattach", :id, "--storagectl", "IDE", 
    #    	      "--port", "0", "--device", "1", "--type", "dvddrive", "--medium", "emptydrive"] 
    #else
    #	vb.customize ["storageattach", :id, "--storagectl", "SATAController", 
    #    	      "--port", "0", "--device", "1", "--type", "dvddrive", "--medium", "emptydrive"] 
    #end
    vb.customize ['modifyvm', :id, '--clipboard', 'bidirectional']
  end

  # Provision
  config.vm.provision "shell", inline: "sudo apt-get update"
  config.vm.provision "shell", inline: "sudo apt-get -y upgrade"
  config.vm.provision "shell", inline: "sudo apt-get install -y linux-headers-$(uname -r) build-essential dkms xubuntu-core virtualbox-guest-dkms virtualbox-guest-utils virtualbox-guest-x11"
  # install guest additions
  #config.vm.provision "shell", inline: "wget http://download.virtualbox.org/virtualbox/5.2.22/VBoxGuestAdditions_5.2.22.iso"
  #config.vm.provision "shell", inline: "sudo mkdir /media/VBoxGuestAdditions"
  #config.vm.provision "shell", inline: "sudo mount -o loop,ro VBoxGuestAdditions_5.2.22.iso /media/VBoxGuestAdditions"
  #config.vm.provision "shell", inline: "sudo sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run"
  #config.vm.provision "shell", inline: "rm VBoxGuestAdditions_5.2.22.iso"
  #config.vm.provision "shell", inline: "sudo umount /media/VBoxGuestAdditions"
  #config.vm.provision "shell", inline: "sudo rmdir /media/VBoxGuestAddition"
  # Permit anyone to start the GUI
  #config.vm.provision "shell", inline: "sudo sed -i 's/allowed_users=.*$/allowed_users=anybody/' /etc/X11/Xwrapper.config"
  config.vm.provision "shell", inline: "sudo apt-get install -y docker docker-compose git zsh jq"
  config.vm.provision "shell", inline: "test -e ~/.oh-my-zsh || git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh", privileged: false
  config.vm.provision "shell", inline: "test -e ~/.zshrc || cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc", privileged: false
  #config.vm.provision "shell", inline: "sudo chsh -s $(which zsh) vagrant"
  #config.vm.provision "shell", inline: "sudo snap install vscode --classic"
  config.vm.provision "shell", inline: "sudo apt-get install -y firefox"
  config.vm.provision "shell", inline: "sudo usermod -a -G docker vagrant"
  config.vm.provision "shell", inline: "test -e Miniconda3-latest-Linux-x86_64.sh || wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh", privileged: false
  config.vm.provision "shell", inline: "test -e $HOME/miniconda3 || /bin/bash Miniconda3-latest-Linux-x86_64.sh -b", privileged: false
  config.vm.provision "shell", inline: "echo \". $HOME/miniconda3/etc/profile.d/conda.sh\" >> ~/.bashrc", privileged: false
  config.vm.provision "shell", inline: "echo \". $HOME/miniconda3/etc/profile.d/conda.sh\" >> ~/.zshrc", privileged: false
  config.vm.provision "shell", inline: "$HOME/miniconda3/bin/conda update -y --all", privileged: false
  config.vm.provision "shell", inline: "sudo userdel -r ubuntu || :"
  config.vm.provision "shell", inline: "test -e hadoop-2.7.6.tar.gz || wget http://apache.cs.utah.edu/hadoop/common/hadoop-2.7.6/hadoop-2.7.6.tar.gz", privileged: false
  config.vm.provision "shell", inline: "test -e hadoop-2.7.6 || tar zxvf hadoop-2.7.6.tar.gz", privileged: false
  config.vm.provision "shell", inline: "cd $HOME/hadoop-2.7.6/etc/hadoop && curl -O https://raw.githubusercontent.com/sstirlin/docker-spark/master/base/core-site.xml", privileged: false
  config.vm.provision "shell", inline: "cd $HOME/hadoop-2.7.6/etc/hadoop && curl -O https://raw.githubusercontent.com/sstirlin/docker-spark/master/base/hdfs-site.xml", privileged: false
  config.vm.provision "shell", inline: "sudo apt-get install -y openjdk-8-jre"

  config.vm.provision "shell", inline: "echo \"export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64\" >> ~/.bashrc", privileged: false
  config.vm.provision "shell", inline: "echo \"export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64\" >> ~/.zshrc", privileged: false
  config.vm.provision "shell", inline: "echo \"export HADOOP_HOME=$HOME/hadoop-2.7.6\" >> ~/.bashrc", privileged: false
  config.vm.provision "shell", inline: "echo \"export HADOOP_HOME=$HOME/hadoop-2.7.6\" >> ~/.zshrc", privileged: false
  config.vm.provision "shell", inline: "echo \"export PATH=$HOME/hadoop-2.7.6/bin:$PATH\" >> ~/.bashrc", privileged: false
  config.vm.provision "shell", inline: "echo \"export PATH=$HOME/hadoop-2.7.6/bin:$PATH\" >> ~/.zshrc", privileged: false
  
  #
  # View the documentation for the provider you're using for more
  # information on available options.

  # Enable provisioning with CFEngine. CFEngine Community packages are
  # automatically installed. For example, configure the host as a
  # policy server and optionally a policy file to run:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.am_policy_hub = true
  #   # cf.run_file = "motd.cf"
  # end
  #
  # You can also configure and bootstrap a client to an existing
  # policy server:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.policy_server_address = "10.0.2.15"
  # end

  # Enable provisioning with Puppet stand alone.  Puppet manifests
  # are contained in a directory path relative to this Vagrantfile.
  # You will need to create the manifests directory and a manifest in
  # the file default.pp in the manifests_path directory.
  #
  # config.vm.provision "puppet" do |puppet|
  #   puppet.manifests_path = "manifests"
  #   puppet.manifest_file  = "site.pp"
  # end

  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.
  #
  # config.vm.provision "chef_solo" do |chef|
  #   chef.cookbooks_path = "../my-recipes/cookbooks"
  #   chef.roles_path = "../my-recipes/roles"
  #   chef.data_bags_path = "../my-recipes/data_bags"
  #   chef.add_recipe "mysql"
  #   chef.add_role "web"
  #
  #   # You may also specify custom JSON attributes:
  #   chef.json = { mysql_password: "foo" }
  # end

  # Enable provisioning with chef server, specifying the chef server URL,
  # and the path to the validation key (relative to this Vagrantfile).
  #
  # The Opscode Platform uses HTTPS. Substitute your organization for
  # ORGNAME in the URL and validation key.
  #
  # If you have your own Chef Server, use the appropriate URL, which may be
  # HTTP instead of HTTPS depending on your configuration. Also change the
  # validation key to validation.pem.
  #
  # config.vm.provision "chef_client" do |chef|
  #   chef.chef_server_url = "https://api.opscode.com/organizations/ORGNAME"
  #   chef.validation_key_path = "ORGNAME-validator.pem"
  # end
  #
  # If you're using the Opscode platform, your validator client is
  # ORGNAME-validator, replacing ORGNAME with your organization name.
  #
  # If you have your own Chef Server, the default validation client name is
  # chef-validator, unless you changed the configuration.
  #
  #   chef.validation_client_name = "ORGNAME-validator"
end
