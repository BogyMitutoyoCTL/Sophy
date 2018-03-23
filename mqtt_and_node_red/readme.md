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

```json
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
    <div id="duration"><span class="text">Duration:</span> <span class="value">3.15155s</span></div>
    <div id="average_speed"><span class="text">Average Speed:</span> <span class="value">0.24555km/h</span></div>
    <div id="distance"><span id="text">Distance:</span> <span id="value">120m</span></div>
</div>
```

### CSS to display in new speed

```css
#data {
    position:fixed;
    top: 50%;
    left: 50%;
    width:30em;
    height:18em;
    margin-top: -9em; /*set to a negative number 1/2 of your height*/
    margin-left: -15em; /*set to a negative number 1/2 of your width*/
    border: 3px solid #ccc;
    background-color: yellow;
}

#duration {
    text-color: black
    text-size: 42px
}

#average_speed {
    text-color: black
    text-size: 42px
}

#distance {
    text-color: black
    text-size: 42px
}
```
### Flow in Node-RED to display speeds and highscore list...

```
[
    {
        "id": "4f594ac7.c0c694",
        "type": "tab",
        "label": "Aquasol",
        "disabled": false,
        "info": ""
    },
    {
        "id": "a9082fa1.80b2b",
        "type": "ui_template",
        "z": "4f594ac7.c0c694",
        "group": "e013fb5.b351a08",
        "name": "Highscore",
        "order": 0,
        "width": "0",
        "height": "0",
        "format": "<style>{{msg.style}}</style>\n<h2>Highscorelist</h2>\n<table>\n<tbody>\n<tr>\n<td><span class=\"title\">Name</span></td>\n<td><span class=\"title\">Duration</span></td>\n<td><span class=\"title\">Average Speed</span></td>\n<td><span class=\"title\">Distance</span></td>\n</tr>\n<tr ng-repeat=\"obj in msg.payload.list\">\n<td><span class=\"value\">{{obj.name}}</span></td>\n<td><span class=\"value\">{{obj.duration}}s</span></td>\n<td><span class=\"value\">{{obj.speed}}km/h</span></td>\n<td><span class=\"value\">{{obj.distance}}m</span></td>\n</tr>\n</tbody>\n</table>\n",
        "storeOutMessages": false,
        "fwdInMessages": true,
        "templateScope": "local",
        "x": 889,
        "y": 573,
        "wires": [
            []
        ]
    },
    {
        "id": "9a11f024.fb3ff",
        "type": "template",
        "z": "4f594ac7.c0c694",
        "name": "css",
        "field": "style",
        "fieldType": "msg",
        "format": "html",
        "syntax": "mustache",
        "template": "table {\n    color: #333;\n    font-family: Helvetica, Arial, sans-serif;\n    width: 100%;\n    border-collapse: collapse;\n    border-spacing: 0;\n}\nh1 {\n    color: #333;\n    font-family: Helvetica, Arial, sans-serif;\n}\ntd, th {\n    border: 1px solid transparent;\n    /* No more visible border */\n    height: 30px;\n    transition: all 0.3s;\n    /* Simple transition for hover effect */\n}\nth {\n    background: #DFDFDF;\n    /* Darken header a bit */\n    font-weight: bold;\n}\ntd {\n    background: #FAFAFA;\n    text-align: center;\n}\n\n/* Cells in even rows (2,4,6...) are one color */\n\ndiv:nth-child(even) td {\n    background: #F1F1F1;\n}\n\n/* Cells in odd rows (1,3,5...) are another (excludes header cells)  */\n\ndiv:nth-child(odd) td {\n    background: #FEFEFE;\n}\ntr td:hover {\n    background: #666;\n    color: #FFF;\n}\n\n/* Hover cell effect! */",
        "x": 599,
        "y": 421,
        "wires": [
            [
                "a9082fa1.80b2b"
            ]
        ]
    },
    {
        "id": "195dda7.0d42f26",
        "type": "json",
        "z": "4f594ac7.c0c694",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 444,
        "y": 396,
        "wires": [
            [
                "4c5b604c.21f51",
                "9a11f024.fb3ff"
            ]
        ]
    },
    {
        "id": "4c5b604c.21f51",
        "type": "debug",
        "z": "4f594ac7.c0c694",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 604,
        "y": 551,
        "wires": []
    },
    {
        "id": "ca0de6c2.93ef68",
        "type": "mqtt in",
        "z": "4f594ac7.c0c694",
        "name": "new Speed Message",
        "topic": "newSpeed",
        "qos": "2",
        "broker": "f56708d.defa2f8",
        "x": 206,
        "y": 120,
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
        "x": 437,
        "y": 128,
        "wires": [
            [
                "c9edfb8f.0fdfa8",
                "9ea6a885.9073c8",
                "6852096a.7dc838"
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
        "x": 893,
        "y": 36,
        "wires": []
    },
    {
        "id": "e1ffa5f9.7c4d98",
        "type": "ui_toast",
        "z": "4f594ac7.c0c694",
        "position": "top left",
        "displayTime": "1",
        "highlight": "",
        "outputs": 0,
        "ok": "OK",
        "cancel": "",
        "topic": "",
        "name": "...",
        "x": 893,
        "y": 215,
        "wires": []
    },
    {
        "id": "7a18cc2b.7837c4",
        "type": "ui_template",
        "z": "4f594ac7.c0c694",
        "group": "d5d137e.fa291c8",
        "name": "Speed",
        "order": 0,
        "width": "0",
        "height": "0",
        "format": "<style>{{msg.style}}</style>\n<div id=\"data\">\n    <div id=\"duration\"><span class=\"text\">Duration:</span> <span class=\"value\">{{msg.payload.duration}}s</span></div>\n    <div id=\"average_speed\"><span class=\"text\">Average Speed:</span> <span class=\"value\">{{msg.payload.speed}}km/h</span></div>\n    <div id=\"distance\"><span class=\"text\">Distance:</span> <span class=\"value\">{{msg.payload.distance}}m</span></div>\n</div>",
        "storeOutMessages": false,
        "fwdInMessages": true,
        "templateScope": "local",
        "x": 881,
        "y": 114,
        "wires": [
            []
        ]
    },
    {
        "id": "9ea6a885.9073c8",
        "type": "template",
        "z": "4f594ac7.c0c694",
        "name": "css",
        "field": "style",
        "fieldType": "msg",
        "format": "html",
        "syntax": "mustache",
        "template": "#data {\n    position:fixed;\n    top: 50%;\n    left: 50%;\n    width:30em;\n    height:18em;\n    margin-top: -9em; /*set to a negative number 1/2 of your height*/\n    margin-left: -15em; /*set to a negative number 1/2 of your width*/\n    border: 3px solid #ccc;\n    background-color: lightgrey;\n}\n\n#duration {\n    background-color:yellow;\n}\n\n#average_speed {\n    background-color:green;\n}\n\n#distance {\n    text-color:orange;\n}\n\n.text {\n    font-size:44px;\n}\n\n.value {\n    font-size:44px;\n}",
        "x": 682,
        "y": 118,
        "wires": [
            [
                "7a18cc2b.7837c4",
                "b3e9c0f9.8a33f"
            ]
        ]
    },
    {
        "id": "b3e9c0f9.8a33f",
        "type": "function",
        "z": "4f594ac7.c0c694",
        "name": "New Values",
        "func": "msg.payload = \"New Values...\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 740,
        "y": 219,
        "wires": [
            [
                "e1ffa5f9.7c4d98"
            ]
        ]
    },
    {
        "id": "501194f7.5df3ac",
        "type": "inject",
        "z": "4f594ac7.c0c694",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 206,
        "y": 214,
        "wires": [
            [
                "4f0e13b9.27201c"
            ]
        ]
    },
    {
        "id": "4f0e13b9.27201c",
        "type": "function",
        "z": "4f594ac7.c0c694",
        "name": "Random",
        "func": "duration = (Math.random() * 10.0).toPrecision(3)\nspeed = (Math.random() * 1.0).toPrecision(3)\ndistance = (Math.random() * 20.0).toPrecision(2)\nmsg.payload = '{\"duration\": ' + duration + ', \"speed\": ' + speed + ', \"distance\": ' + distance + '}'\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 361,
        "y": 261,
        "wires": [
            [
                "680a3aa6.e2f884"
            ]
        ]
    },
    {
        "id": "c4c6c4cb.a9e7f8",
        "type": "inject",
        "z": "4f594ac7.c0c694",
        "name": "Highscore",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 112,
        "y": 556,
        "wires": [
            [
                "c310f1fa.25245"
            ]
        ]
    },
    {
        "id": "43c61600.429dbc",
        "type": "ui_ui_control",
        "z": "4f594ac7.c0c694",
        "name": "Switch",
        "x": 772,
        "y": 278,
        "wires": [
            []
        ]
    },
    {
        "id": "6852096a.7dc838",
        "type": "function",
        "z": "4f594ac7.c0c694",
        "name": "to Tab Speeds",
        "func": "msg.payload = 'Speeds'\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 564,
        "y": 270,
        "wires": [
            [
                "43c61600.429dbc",
                "518ea2cd.963afc"
            ]
        ]
    },
    {
        "id": "518ea2cd.963afc",
        "type": "delay",
        "z": "4f594ac7.c0c694",
        "name": "",
        "pauseType": "delay",
        "timeout": "3",
        "timeoutUnits": "seconds",
        "rate": "1",
        "nbRateUnits": "1",
        "rateUnits": "second",
        "randomFirst": "1",
        "randomLast": "5",
        "randomUnits": "seconds",
        "drop": false,
        "x": 528,
        "y": 349,
        "wires": [
            [
                "7afd7d03.b16d24"
            ]
        ]
    },
    {
        "id": "8961db6a.777f88",
        "type": "ui_ui_control",
        "z": "4f594ac7.c0c694",
        "name": "Switch",
        "x": 842,
        "y": 394,
        "wires": [
            []
        ]
    },
    {
        "id": "7afd7d03.b16d24",
        "type": "function",
        "z": "4f594ac7.c0c694",
        "name": "to Tab Highscore",
        "func": "msg.payload = 'Highscore'\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 703,
        "y": 345,
        "wires": [
            [
                "8961db6a.777f88"
            ]
        ]
    },
    {
        "id": "312580a5.b27db",
        "type": "mqtt in",
        "z": "4f594ac7.c0c694",
        "name": "new Highscore Message",
        "topic": "newHighscore",
        "qos": "2",
        "broker": "f56708d.defa2f8",
        "x": 197,
        "y": 328,
        "wires": [
            [
                "195dda7.0d42f26"
            ]
        ]
    },
    {
        "id": "c310f1fa.25245",
        "type": "function",
        "z": "4f594ac7.c0c694",
        "name": "Fixed Highscore",
        "func": "var name1 = \"James Brown\"\nmsg.payload = '{\"list\": [{\"start_time\": 1521816916.2528725, \"py/object\": \"HighScoreEntry.HighScoreEntry\", \"duration\": 0.19170522689819336, \"speed\": 37.557661397639514, \"stop_time\": 1521816916.4445777, \"distance\": 2000, \"name\": \"' + name1 + '\", \"record_date\": {\"py/object\": \"datetime.date\", \"__reduce__\": [{\"py/type\": \"datetime.date\"}, [\"B+IDFw==\"]]}}, {\"start_time\": 1521816918.4935858, \"py/object\": \"HighScoreEntry.HighScoreEntry\", \"duration\": 0.21306467056274414, \"speed\": 33.792556884177166, \"stop_time\": 1521816918.7066505, \"distance\": 2000, \"name\": \"Hans\", \"record_date\": {\"py/object\": \"datetime.date\", \"__reduce__\": [{\"py/type\": \"datetime.date\"}, [\"B+IDFw==\"]]}}, {\"start_time\": 1521816656.9219244, \"py/object\": \"HighScoreEntry.HighScoreEntry\", \"duration\": 0.335817813873291, \"speed\": 21.440196745240755, \"stop_time\": 1521816657.2577422, \"distance\": 2000, \"name\": \"Hans\", \"record_date\": {\"py/object\": \"datetime.date\", \"__reduce__\": [{\"py/type\": \"datetime.date\"}, [\"B+IDFw==\"]]}}], \"py/object\": \"HighScoreList.HighScoreList\", \"max_age\": {\"py/reduce\": [{\"py/type\": \"datetime.timedelta\"}, {\"py/tuple\": [1, 0, 0]}, null, null, null]}, \"max_count\": 3}';\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 264,
        "y": 464,
        "wires": [
            [
                "195dda7.0d42f26"
            ]
        ]
    },
    {
        "id": "e013fb5.b351a08",
        "type": "ui_group",
        "z": "4f594ac7.c0c694",
        "name": "Highscore",
        "tab": "9cb6dd64.64118",
        "disp": false,
        "width": "3",
        "collapse": false
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
    },
    {
        "id": "d5d137e.fa291c8",
        "type": "ui_group",
        "z": "",
        "name": "Tabelle",
        "tab": "6c59aefb.2d2a1",
        "disp": false,
        "width": "17",
        "collapse": false
    },
    {
        "id": "9cb6dd64.64118",
        "type": "ui_tab",
        "z": "",
        "name": "Highscore",
        "icon": "dashboard",
        "order": 2
    },
    {
        "id": "6c59aefb.2d2a1",
        "type": "ui_tab",
        "z": "",
        "name": "Speeds",
        "icon": "dashboard",
        "order": 3
    }
]
```
