---
:tags: dev
---

# After ITR Install
:original-url: https://docs.google.com/document/d/1ooMIQVOEQq6QzegE2QzsFadvYhRnto4eCaAQpz02Wj0/edit


## JRC Tasks
1. +Phone external access (8-, 0-)
1. +domain-email
1. +coffe (not from DR)
1. +INSTALL: VirtualBox + Extensions Pack
1. +INSTALL: Adobe Reader updated
1. +INSTALL: greek lang
1. TerminalServers
1. ChromeEarthPlugin
1. +Intranet password
1. +Entrance Permit
1. +Update Notepad++
1. INSTALL: Google-earth
1. INSTALL: d:\Downloads\SharePointFoundation.exe
1. INSTALL: http://visualhg.codeplex.com/
1. INSTALL: GIMP
1. INSTALL: 7z
1. +GPG: http://www.gpg4win.org/

## After WIN install
1. TotalCmmander (enable operations-logging)
1. WinCDEmu
1. Notepad++ (& config TotalCommaner)
1. Dropbox
1. TotroiseHg (/Svn)
1. putty/puttySFTP
1. UnxUtils: http://unxutils.sourceforge.net/ & http://sourceforge.net/projects/unxutils/files/1. latest/download
1. WinSCP
1. WinPython (32 | 64) bit, Python3 or 2
1. LiClipse
1. python-cmd-prompt: pip install distribute

## After LINUX install
### EC2
```bash
sudo apt-get install colordiff traceroute mc multitail htop apt-file
```

Download and install `browsh` (instead of `lynx`): https://www.brow.sh/docs/introduction/

## Dropbox:
https://www.dropbox.com/install?os=lnx
http://ubuntuserverguide.com/2012/06/how-to-install-and-configure-dropbox-on-ubuntu-server-12-04.html


## LINUX
sudo: /etc/group:sudo | wheel)

### Not in UBUNTU
```bash
apt-get install apache2 vim screen apt-file aptitude htop mc mercurial arp-scan gpm hping3 finger build-essential colordiff debsums p7zip distcc distcc-pump dlocate nmap traceroute iodine etherape kismet ethtool festival fuse-utils gawk git gnome-tweak-tool imagemagick lynx multitail coffeescript mumble nodejs openssh-server php5 powertop remmina samba synaptic tftpd tidy unetbootin unrar user-setup vinagre vlan vlc wakeonlan wine winetricks wireshark gnome-shell gimp dconf-tools alacarte gbrainy gftp gir1.2-gtop gparted hplip-gui chromium-browser
```

### Headless UBUNTU (JRC)
```bash
java-7-headless python php5 lynx colordiff mc htop traceroute screen apt-file mercurial  multitail hping3 finger debsums p7zip dlocate gawk git tidy unrar user-setup
```

NO: imagemagick

###  Lubuntu in VBox
```bash
sudo apt-get install virtualbox-ose-guest-utils

sudo apt-get install apache2 apt-file aptitude arp-scan build-essential  coffeescript colordiff  debsums distcc distcc-pump dlocate etherape ethtool festival finger fuse-utils gawk  gftp gimp  git gpm hping3  htop imagemagick iodine kismet lynx mc mercurial multitail mumble nmap nodejs openssh-server p7zip php5  samba screen  synapse tftpd tidy traceroute unetbootin unrar  vim vinagre vlan vlc wakeonlan wine winetricks
```

### Not in APTOSID
```bash
apt-get install update-manager-gnome update-notifier software-properties-gtk dnsutils bootlogd lightdm multitail volumeicon-alsa flashplugin-nonfree pm-utils
```

### SID(LXFCE)  in VBox
```bash
apt-get install gpm vim bash-completion chromium screen apt-file htop mc mercurial arp-scan gpm hping3 finger build-essential colordiff debsums p7zip dlocate mlocate nmap iodine etherape kismet festival gawk wakeonlan imagemagick debian-keyring byobu xfce4-settings zenmap
```

### VBox
```bash
sudo apt-get  dkms virtualbox-ose-guest-x11
```

### Ubuntu
```bash
apt-get install libmtp-runtime ## Stops minor boot log error
```

## COMMERCIAL
```bash
apt-get install dropbox google-talkplugin skype grive

echo "MANUAL INSTALL: teamviewer7 heimdal"

echo "Gnome-shell-exts: disable corners, alt-tab, sys-mon, shellshape"

echo "Add greek-lang pack, flag, xcb options"
XKBLAYOUT="us,gr"
XKBVARIANT="euro"
XKBOPTIONS="terminate:ctrl_alt_bksp,grp:shift_caps_toggle,grp_led:scroll"
sudo dpkg-reconfigure console-setup ## Greek, trerminus 14
echo "Remove xorg drivers"

echo "SSD optimazations, swappiness"

echo "Setup vim autosave position /etc/vim/*"

# Openbox menu for reboot/Shutfdown & sudoers
# Openbox volumeicon-xxx
```

## Gnome-Shell
### Session timeout
gpg-key
koyote cp


## `~/bashrcs`
```bash
# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Prompt
LightBlue='\[\e[01;38;5;74m\]'
Grey='\[\e[0;37m\]'
White='\[\e[0;97m\]'
PS1="$LightBlue\u@\h $Grey\w $LightBlue\$ $White"

# History search
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

### History append rather than overwrite
# don't put duplicate lines or lines starting with space in the history.
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend
PROMPT_COMMAND="history -a;$PROMPT_COMMAND"
# attempt to save all lines of a multiple-line command in the same history entry
shopt -s cmdhist
# save multi-line commands to the history with embedded newlines
shopt -s lithist

# Store always & everything.
# From http://jesrui.sdf-eu.org/remember-all-your-bash-history-forever.html
#HISTSIZE=10000
#HISTFILESIZE=20000
HISTSIZE=-1
HISTFILESIZE="no truncation (if not numeric)"
#Ignore 1-char cmds
HISTIGNORE=?:?


### Color manpages (Arch style)
export LESS_TERMCAP_mb=$'\E[01;31m'
export LESS_TERMCAP_md=$'\E[01;38;5;74m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[38;5;246m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[04;38;5;146m'

### Color common commands
alias ls='ls --color=auto'
alias grep='grep --color=auto'
```

### `.inputrc`
```bash
"\e[A": history-search-backward
"\e[B": history-search-forward

"\e[1;5C": forward-word
"\e[1;5D": backward-word
"\e[1;5C": forward-word
"\e[1;5D": backward-word
"\e\e[C": forward-word
"\e\e[D": backward-word
"\C-x\C-r": re-read-init-file
```

## MyServices README example:
```
#########################
Root dir for PyPi server.
#########################
:maintainer: konstantinos.anagnostopoulos@ext.jrc.ec.europa.eu (ankostis@gmail.com)
:created:   2014-Sept

This is a PyPI compatible package index server :https://pypi.python.org/pypi/pypiserver


Folder contents
===============
There should be these in the ``pypi-server``'s home-dir::

    +--packages/                    ## Uploaded/mirrored python-packages stored there.
    +--venv-3/                      ## Virtual-environement that the pypi-server runs under.
        +--lib/python3.4/site-packages/pypiserver/_app.py       ## Has the Welcome message.
    +--pypy-server.sh           ## Server start-up shell-script invoked by `/etc/init/pypiserver.conf` upstart-service.
    +--.htaccess                ## Upload user/password.
```