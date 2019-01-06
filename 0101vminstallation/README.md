# Linux Virtual Machine rough guide

## Introduction

We will be installing a Linux virtual machine on your laptop together during the first class.
Remember:  the lecture is recorded, so if you need to repeat this procedure then you can always
rewatch it.  The steps are described below.

We will work almost exclusively in Linux this semester.


## Before we begin

The minimum hardware required for this class is a laptop with 8GB of ram and 4 cores.  16GB is recommended.

NOTE:  If you have played with virtualization before and have enabled Hyper-V (Windows), KVM (Linux), or 
VMWare ESXi then you need to disable it now.  Talk to me and we can work through it together.
We are using VirtualBox for the first several weeks, and it doesn't play well with those other
hypervisors.  If you don't know what this means then don't worry about it.


## Steps

First, browse to https://www.virtualbox.org/wiki/Download_Old_Builds_5_2 and pick the download link 
that corresponds to your host operating system (probably OSX or Windows).  It is important that you download 
and install version 5.2 of VirtualBox.  Other versions are not guaranteed to work correctly.

Next, browse to https://www.vagrantup.com/downloads.html and pick the download link that corresponds to your 
host operating system.  Download and install it.

**NOTE for everybody EXCEPT Mac users:**  There is a slight chance that virtualization is disabled in your BIOS/UEFI.
If VirtualBox complains in the steps below then you need to enable virtualization.  The way to do this is unique 
to every laptop, but usually entails restarting your computer, 
waiting for the initial screen to flash, then quickly hitting the `Del` or `Esc` keys to enter SETUP.
When in doubt, ask me.

Now that VirtualBox and Vagrant are installed, you need to open a command-line interface ("Terminal" in OSX, 
"Command Prompt" in Windows).
In Windows click on the search button and type `cmd`.  In OSX open up `Applications->Utilities->Terminal`.

Once open, type the following commands (if any single command fails then ask me before proceeding):

```sh
mkdir msbx5420vagrant
cd msbx5420vagrant
curl -O https://raw.githubusercontent.com/sstirlin/MSBX5420Spring2019/master/Vagrantfile
vagrant plugin install vagrant-disksize
vagrant up
```

**NOTE for Windows users:**  If the `curl` command above failed then manually browse
to https://raw.githubusercontent.com/sstirlin/MSBX5420Spring2019/master/Vagrantfile and right-click on the
page (it should look like a bunch of code).
Choose `Save As` and download it to the `msbx5420vagrant` folder that we just created.  Make sure to name the file
`Vagrantfile` (NO EXTENSION!!!).  You can then just skip the `curl` download step.  **Beware** that some
browsers (e.g. Chrome) will add a `.txt` extension anyway.  You'll need to rename it to remove the extension.

The `vagrant up` command should run for a long time (45 minutes to an hour).  Once it finishes 
your VM will be started, however it will not be in a usable state.  You need to restart it.

Type the following commands into your command prompt (NOT in the VM) to restart it:

```sh
vagrant halt
vagrant up
```

When your VM boots (could take a few minutes) you will be presented with a login prompt.  Choose the `vagrant` user.
The password is `vagrant`.  Congratulations!  You have a functioning Linux virtual machine now.

When you are done with your VM for the day you can suspend it:
```sh
vagrant suspend
```
or even bring it down hard:
```sh
vagrant halt
```
