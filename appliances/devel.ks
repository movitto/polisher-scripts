# originally from http://www.thincrust.net/kickstarts/baseAppliance-f10.ks 

#version=DEVEL
# Firewall configuration
firewall --disabled
repo --name=f12 --mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=fedora-12&arch=$basearch
repo --name=f12-updates --mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=updates-released-f12&arch=$basearch
repo --name=thincrust --baseurl=http://www.thincrust.net/repo/noarch/
repo --name=polisher-devel --baseurl=file:///home/mmorsi/workspace/polisher/artifacts/repos/devel

# Network information
network  --bootproto=dhcp --device=eth0 --onboot=on

# System authorization information
auth --useshadow --enablemd5

# System keyboard
keyboard us

# System language
lang en_US.UTF-8

# SELinux configuration
selinux --disabled

# System timezone
timezone  US/Eastern

# System bootloader configuration
bootloader --append="acpi=force" --location=mbr --timeout=1

# Disk partitioning information
part /  --fstype="ext3" --ondisk=sda --size=1500 --bytes-per-inode=4096

%post
  #%include /usr/share/appliance-tools/base-post.ks

  /sbin/chkconfig --level 35 ace on
  mkdir /etc/sysconfig/ace
  echo base_appliance >> /etc/sysconfig/ace/appliancename
%end

%packages --excludedocs --nobase --instLangs=en:fr
@core
@base-x
@gnome-desktop
acpid
base_appliance
bash
chkconfig
dhclient
e2fsprogs
grub
iputils
kernel
lokkit
passwd
rootfiles
vim-minimal
yum
-authconfig
-checkpolicy
-dmraid
-ed
-fedora-logos
-fedora-release-notes
-kbd
-kpartx
-kudzu
-libselinux
-libselinux-python
-lvm2
-mdadm
-mkinitrd
-policycoreutils
-prelink
-rhpl
-selinux-policy*
-setserial
-tar
-usermode
-wireless-tools


 # polisher generated packages
 ruby        # provides gem and rake as well
 ruby-activerecord
 ruby-cairo
 rubygem-daemons
 rubygem-rack
 ruby-gnome2
 ruby-mysql
 puppet
 # TODO readd gemcutter, mongrel, (figure out why they are causing problems), 
%end

