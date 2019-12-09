MechLiv
==========

Play mechanical keyboard sound in your System Tray.


## Installation
MechLiv is distributed as a python package. Do the following to install:

``` sh
sudo pip install mechliv
OR
sudo easy_install mechliv
OR
#Download Source and cd to it
sudo python setup.py install
```

After that, you can run `mechliv` from anywhere and it will run. You can
now add it to your OS dependent session autostart method. In Ubuntu, you can
access it via: 

1. System > Preferences > Sessions  
(OR)
2. System > Preferences > Startup Applications 

depending on your Ubuntu Version. Or put it in `~/.config/openbox/autostart` 
if you are running OpenBox.
On PopOs install this to display AppIndicator https://extensions.gnome.org/extension/615/appindicator-support/

### Upgrade
The latest stable version is [![the one on PyPi](https://pypip.in/v/mechliv/badge.png)](https://pypi.python.org/pypi/mechliv/)

You can check which version you have installed with `mechliv --version`.

To upgrade, run `pip install -U mechliv`. In some cases (Ubuntu), you might
need to clear the pip cache before upgrading:

`sudo rm -rf /tmp/pip-build-root/mechliv`

MechLiv will automatically check the latest version on startup, and inform you if there is an update available.

## Features
1. Play mechanical keyboard sound.

### Troubleshooting

If the app indicator fails to show in Ubuntu versions, consider installing 
python-appindicator with

`sudo apt-get install python-appindicator python-gtk2`

### Development

To develop on MechLiv, or to test out experimental versions, do the following:

- Clone the project
- Run `(sudo) python setup.py develop` in the MechLiv root directory
- Run `mechliv` with the required command line options from anywhere.

## Author Information
- Artiya Thinkumpang (<artiya4u@gmail.com>)

## Licence
Licenced under the [MIT Licence](http://nemo.mit-license.org/).

