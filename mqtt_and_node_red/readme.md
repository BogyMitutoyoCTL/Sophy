# Howto install mosquitto mqtt broker and node-red on a raspberry pi

## Overview

### What is mosquitto mqtt broker?

Mosquitto is a MQTT server/broker. MQTT is a lightweight protocol that uses a publish/subscribe model.

* https://en.wikipedia.org/wiki/MQTT
* https://test.mosquitto.org/

### What is node-red?

Node-RED is a web-based programming tool to easy create data flows while wiring nodes.

* https://nodered.org/
* https://en.wikipedia.org/wiki/Node-RED

## How to install on a raspberry pi with raspbian 

### Here are the steps (for debian stretch) to install mosquitto mqtt server:

First install mosquitto and clients...
```bash
sudo apt install mosquitto
sudo apt install mosquitto-clients 
```
then check if the server is running...
```bash
/etc/init.d/mosquitto status
```
that should give you something like that:
```bash
● mosquitto.service - LSB: mosquitto MQTT v3.1 message broker
   Loaded: loaded (/etc/init.d/mosquitto; generated; vendor preset: enabled)
   Active: active (running) since Wed 2018-03-21 11:05:48 GMT; 6h ago
     Docs: man:systemd-sysv-generator(8)
    Tasks: 1 (limit: 4915)
   CGroup: /system.slice/mosquitto.service
           └─2455 /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf

Mar 21 11:05:48 raspberry systemd[1]: Starting LSB: mosquitto MQTT v3.1 message broker...
Mar 21 11:05:48 raspberry mosquitto[2449]: Starting network daemon:: mosquitto.
Mar 21 11:05:48 raspberry systemd[1]: Started LSB: mosquitto MQTT v3.1 message broker.
```
Great - mosquitto is running on your system....

### Here are the steps (for debian stretch) to install node-red:

This could be done as the user pi. No sudo is needed.
```bash
pi@raspberry:~ $
```
Go to your home directory and run the install script:
```bash
cd ~
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
```
run the update script..
```bash
update-nodejs-and-nodered
```
make node-red to start always during system boot
```bash
sudo systemctl enable nodered.service
sudo service nodered restart
```
Open the node-red webpage:
http://127.0.0.1:1880

### Install some mqtt helpers for python

The paho package helps us to send mqtt data out of our python apps
```bash
sudo apt-get install python3-pip
sudo pip3 install paho-mqtt
```
### Test to send something to the mqtt server

Try to use the mosquitto_pub command to send data from the console to the mqtt server
```bash
mosquitto_pub -h localhost -t test -m "Hello World!"
```
