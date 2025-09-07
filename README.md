# raspi-control-panel
This project is for a Raspberry Pi microcomputer using GPIO to control relay circuits and analog sensors (temperature, battery voltage).

## Flask Server
I have setup a basic flask server, serving to localhost:5000 and rendering basic html. Flask is preinstalled on the distro of linux for Raspberry Pi 5. Simply navigate to the project directory and run `python3 server.py` and then visit `localhost:5000`.

## MySQL
Basic installation of maria-db

```
sudo apt update
sudo apt upgrade
sudo apt install mariadb-server
sudo mysql_secure_installation
```

put your MySQL password and username into the .env file. See the db_handler.py file for configurations for the database. Database is setup to track critical metrics like voltage over time and state of relays. You can use this later to build the advanced dashboard and stream realtime metrics. 

## Relay Drivers
Helpful note: relays must be grounded to activate (therefore sometimes 0 means on depending on the context). This was quite confusing for a while