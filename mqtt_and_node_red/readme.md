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

### Import the first flow

Go to the Node-RED Site and import a flow from the clipboard.

```
[{"id":"ca0de6c2.93ef68","type":"mqtt in","z":"4f594ac7.c0c694","name":"TestMessage","topic":"test","qos":"2","broker":"f56708d.defa2f8","x":76,"y":706,"wires":[["680a3aa6.e2f884"]]},{"id":"a21fd729.382908","type":"template","z":"4f594ac7.c0c694","name":"css","field":"style","fieldType":"msg","format":"html","syntax":"mustache","template":"table {\n    color: #333;\n    font-family: Helvetica, Arial, sans-serif;\n    width: 100%;\n    border-collapse: collapse;\n    border-spacing: 0;\n}\nh1 {\n    color: #333;\n    font-family: Helvetica, Arial, sans-serif;\n}\ntd, th {\n    border: 1px solid transparent;\n    /* No more visible border */\n    height: 30px;\n    transition: all 0.3s;\n    /* Simple transition for hover effect */\n}\nth {\n    background: #DFDFDF;\n    /* Darken header a bit */\n    font-weight: bold;\n}\ntd {\n    background: #FAFAFA;\n    text-align: center;\n}\n\n/* Cells in even rows (2,4,6...) are one color */\n\ntr:nth-child(even) td {\n    background: #F1F1F1;\n}\n\n/* Cells in odd rows (1,3,5...) are another (excludes header cells)  */\n\ntr:nth-child(odd) td {\n    background: #FEFEFE;\n}\ntr td:hover {\n    background: #666;\n    color: #FFF;\n}\n\n/* Hover cell effect! */","x":419,"y":783,"wires":[["c9edfb8f.0fdfa8"]]},{"id":"680a3aa6.e2f884","type":"json","z":"4f594ac7.c0c694","name":"","property":"payload","action":"","pretty":false,"x":252,"y":740,"wires":[["a21fd729.382908"]]},{"id":"c9edfb8f.0fdfa8","type":"debug","z":"4f594ac7.c0c694","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":594,"y":756,"wires":[]},{"id":"f56708d.defa2f8","type":"mqtt-broker","z":"","name":"MQTT Broker","broker":"localhost","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"willTopic":"","willQos":"0","willPayload":"","birthTopic":"","birthQos":"0","birthPayload":""}]
```

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
