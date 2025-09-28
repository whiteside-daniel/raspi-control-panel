# raspi-control-panel

## Flask Server
Basic flask server serving to localhost:5000 and rendering basic html. Flask is preinstalled on the distro of linux for Raspberry Pi 5

## MySQL
Basic installation of maria-db

```
sudo apt install mariadb-server
sudo mysql_secure_installation
```

put your MySQL password and username into the .env file

## Relay Drivers
Helpful note: relays must be grounded to activate (therefore sometimes 0 means on depending on the context). This was quite confusing for a while

## Raspi Configuration
### Power Supply Configurations
`sudo nano /boot/firmware/config.txt`

add the following lines
```
# Allow 5amp power supply (external)
usb_max_current_enable=1
```

### Boot Raspi in Kiosk mode
First - make sure your python script is executable
`chmod +x /path/to/your/script.py`

Then create a desktop autostart entry
`sudo nano /etc/xdg/autostart/startup.desktop`

Add the following Content:
```
[Desktop Entry]
Type=Application
Name=Startup
Exec=/bin/bash -c 'python3 /path/to/your/script.py & sleep 5 && chromium-browser --kiosk --no-sandbox --disable-infobars --disable-session-crashed-bubble --disable-restore-session-state http://localhost:5000'
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
```

Then make sure the startup script has permissions:
`sudo chmod 664 /etc/xdg/autostart/startup.desktop`
Validate permissions:
`cat /etc/xdg/autostart/startup.desktop`

You can cleanup performance with these commands:
```
sudo systemctl disable bluetooth
sudo systemctl disable cups
sudo systemctl disable avahi-daemon
```
