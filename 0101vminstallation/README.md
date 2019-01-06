# Linux Virtual Machine rough guide

## Introduction

We will be installing a Linux virtual machine on your laptop.  Since we will do this together in class
(which is recorded), I only describe the rough steps here.
You can always watch the lecture again if you need to be reminded
of the steps.

We will work almost exclusively in Linux this semester.


## Steps

The minimum system required for this class is a laptop with 8GB of ram and 4 cores.  16GB is recommended.

First, browse to https://www.virtualbox.org/wiki/Download_Old_Builds_5_2 and pick the download link 
that corresponds to your operating system.  It is important that you download and install version 5.2 of VirtualBox.
Other versions are not guaranteed to work correctly.

Next, browse to https://www.vagrantup.com/downloads.html and pick the download link that corresponds to your 
operating system.  You need to download and install it.

NOTE:  If you have played with virtualization before and have enabled Hyper-V (Windows), KVM (Linux), or 
VMWare ESXi then you need to disable those now.  They are incompatible with VirtualBox.
If you don't know what this means then don't worry about it.

NOTE for people *not* on a Mac:  There is a slight chance that virtualization is disabled in your BIOS/UEFI.
If VirtualBox complains, then you need to enable it.  The steps are unique to every system,
but usually entails restarting your computer, waiting for the initial screen to flash, 
then hitting the `Del` or `Esc` keys to enter SETUP.  When in doubt, ask me.

Now that VirtualBox and Vagrant are installed, you need to open a terminal (aka command prompt).
In Windows search for `cmd`.  In OSX open up `Applications->Utilities->Terminal`.

Once open, type the following commands (if any single command fails then ask me before proceeding):

```bash
mkdir msbx5420vagrant
cd msbx5420vagrant
curl -O https://raw.githubusercontent.com/sstirlin/MSBX5420Spring2019/master/Vagrantfile
vagrant plugin install vagrant-disksize
vagrant up
```

NOTE:  If you are in Windows and the `curl` command above failed then you need to follow these
instructions to install it:
http://callejoabel.blogspot.com/2013/09/making-curl-work-on-windows-7.html

The `vagrant up` command should run for a long time (45 minutes to an hour).  Once it finishes 
your VM will be started, however it will not be in a usable state.  You need to restart it.

Type the following commands into your command prompt to restart it:

```bash
vagrant halt
vagrant up
```

Once your VM comes up you will be presented with a login prompt.  Choose the `vagrant` user.
The password is `vagrant`.  Congratulations!  You have a functioning Linux virtual machine now.
