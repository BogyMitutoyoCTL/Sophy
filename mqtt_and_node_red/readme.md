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

First update and install mosquitto and clients...
```bash
sudo apt update
sudo apt upgrade
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
[
    {
        "id": "ca0de6c2.93ef68",
        "type": "mqtt in",
        "z": "4f594ac7.c0c694",
        "name": "TestMessage",
        "topic": "test",
        "qos": "2",
        "broker": "f56708d.defa2f8",
        "x": 76,
        "y": 706,
        "wires": [
            [
                "680a3aa6.e2f884"
            ]
        ]
    },
    {
        "id": "680a3aa6.e2f884",
        "type": "json",
        "z": "4f594ac7.c0c694",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 252,
        "y": 740,
        "wires": [
            [
                "c9edfb8f.0fdfa8"
            ]
        ]
    },
    {
        "id": "c9edfb8f.0fdfa8",
        "type": "debug",
        "z": "4f594ac7.c0c694",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 594,
        "y": 756,
        "wires": []
    },
    {
        "id": "f56708d.defa2f8",
        "type": "mqtt-broker",
        "z": "",
        "name": "MQTT Broker",
        "broker": "localhost",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": true,
        "keepalive": "60",
        "cleansession": true,
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": ""
    }
]
```
To activate that flow, you have to click at the red DEPLOY Button.

### Install some mqtt helpers for python

The paho package helps us to send mqtt data out of our python apps
```bash
sudo apt-get install python3-pip
sudo pip3 install paho-mqtt
```
### Test to send something to the mqtt server

Try to use the mosquitto_pub command to send data from the console to the mqtt server
```bash
mosquitto_pub -h localhost -t test -m '{"string":"Hello World!"}'
```
Verify if the message is displayed in Node-RED "Debug" window...

### Testprogram to send data with python

we use an editor to write the first python mqtt sender...

```bash
vi demo_mqtt_publish.py 
```

```python
#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time

# Create client instance and connect to localhost
client = mqtt.Client()
client.connect("localhost",1883,60)

#data
json_data = '{"string":"Hello World!"}'

client.publish("test", json_data);
client.disconnect();
```
and go...
```bash
chmod +x ./demo_mqtt_publish.py
./demo_mqtt_publish.py 
```

### HTML to display new speed

```html
<div id="data">
    <div id="duration"><span class="text">Duration:</span> <span class="value">3.15155ms</span></div>
    <div id="average_speed"><span class="text">Average Speed:</span> <span class="value">0.24555ms</span></div>
    <div id="distance"><span id="text">Distance:</span> <span id="value">120m</span></div>
</div>
```
