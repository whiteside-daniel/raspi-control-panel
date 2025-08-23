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
