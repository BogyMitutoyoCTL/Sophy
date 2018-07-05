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

Go to the Node-RED Site and import a flow from the clipboard (Burger Menu, Import, Clipboard).

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

![image](https://user-images.githubusercontent.com/3775529/42264861-2bec56f6-7f72-11e8-99b6-622e60828bae.png)

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
"Hello World" should appear again in the debug window....

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

Before importing this flow, install the UI nodes (Burger Menu, Manage Palette, Palette, Install, node-red-dashboard)

```json
[
    {
        "id": "ea3fc4f2.ca0968",
        "type": "tab",
        "label": "Aquasol",
        "disabled": false,
        "info": ""
    },
    {
        "id": "305f3645.e6b6fa",
        "type": "ui_template",
        "z": "ea3fc4f2.ca0968",
        "group": "87cd78ea.8a4c68",
        "name": "Highscore",
        "order": 0,
        "width": "0",
        "height": "0",
        "format": "<style>{{msg.style}}</style>\n<h1>Highscorelist</h1>\n<table>\n<tbody>\n<tr>\n<td><span class=\"title\">Rank</span></td>\n<td><span class=\"title\">Name</span></td>\n<td><span class=\"title\">Duration</span></td>\n<td><span class=\"title\">Average Speed</span></td>\n<td><span class=\"title\">Distance</span></td>\n</tr>\n<tr ng-repeat=\"obj in msg.payload.list\">\n<td><span class=\"value\">{{obj.rank}}</span></td>\n<td><span class=\"value\">{{obj.name}}</span></td>\n<td><span class=\"value\">{{obj.duration}} sec</span></td>\n<td><span class=\"value\">{{obj.speed}} m/sec</span></td>\n<td><span class=\"value\">{{obj.distance}} m</span></td>\n</tr>\n</tbody>\n</table>\n",
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
        "id": "34b503a5.889eac",
        "type": "template",
        "z": "ea3fc4f2.ca0968",
        "name": "css",
        "field": "style",
        "fieldType": "msg",
        "format": "html",
        "syntax": "mustache",
        "template": "table {\n    color: #333;\n    font-family: Helvetica, Arial, sans-serif;\n    font-size: 30px;\n    width: 100%;\n    border-collapse: collapse;\n    border-spacing: 0;\n}\nh1 {\n    color: #333;\n    font-family: Helvetica, Arial, sans-serif;\n}\ntd, th {\n    border: 1px solid transparent;\n    /* No more visible border */\n    height: 30px;\n    transition: all 0.3s;\n    /* Simple transition for hover effect */\n}\nth {\n    background: #DFDFDF;\n    /* Darken header a bit */\n    font-weight: bold;\n}\ntd {\n    background: #FAFAFA;\n    text-align: center;\n}\n\n/* Cells in even rows (2,4,6...) are one color */\n\ndiv:nth-child(even) td {\n    background: #F1F1F1;\n}\n\n/* Cells in odd rows (1,3,5...) are another (excludes header cells)  */\n\ndiv:nth-child(odd) td {\n    background: #FEFEFE;\n}\ntr td:hover {\n    background: #666;\n    color: #FFF;\n}\n\n/* Hover cell effect! */",
        "x": 695,
        "y": 476,
        "wires": [
            [
                "305f3645.e6b6fa"
            ]
        ]
    },
    {
        "id": "4bbc408c.570a9",
        "type": "json",
        "z": "ea3fc4f2.ca0968",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 444,
        "y": 396,
        "wires": [
            [
                "b6cd2a00.9b18f8",
                "94101cff.21b65"
            ]
        ]
    },
    {
        "id": "94101cff.21b65",
        "type": "debug",
        "z": "ea3fc4f2.ca0968",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "x": 658,
        "y": 419,
        "wires": []
    },
    {
        "id": "6c9da5d4.a1605c",
        "type": "mqtt in",
        "z": "ea3fc4f2.ca0968",
        "name": "new Speed Message",
        "topic": "newSpeed",
        "qos": "2",
        "broker": "8148060c.347b58",
        "x": 206,
        "y": 120,
        "wires": [
            [
                "75f8b147.eb03e"
            ]
        ]
    },
    {
        "id": "75f8b147.eb03e",
        "type": "json",
        "z": "ea3fc4f2.ca0968",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 437,
        "y": 128,
        "wires": [
            [
                "8e1f8b0e.6cca18",
                "d6a59694.1eb128",
                "bacf627c.d9378"
            ]
        ]
    },
    {
        "id": "8e1f8b0e.6cca18",
        "type": "debug",
        "z": "ea3fc4f2.ca0968",
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
        "id": "3e66cb6f.ab1814",
        "type": "ui_toast",
        "z": "ea3fc4f2.ca0968",
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
        "id": "f7d55276.8c506",
        "type": "ui_template",
        "z": "ea3fc4f2.ca0968",
        "group": "7e2298f1.493228",
        "name": "Speed",
        "order": 0,
        "width": "0",
        "height": "0",
        "format": "<style>{{msg.style}}</style>\n<div id=\"data\">\n    <div id=\"duration\"><span class=\"text\">Duration:</span> <span class=\"value\">{{msg.payload.duration}} sec</span></div>\n    <div id=\"average_speed\"><span class=\"text\">Average Speed:</span> <span class=\"value\">{{msg.payload.speed}} m/sec</span></div>\n    <div id=\"distance\"><span class=\"text\">Distance:</span> <span class=\"value\">{{msg.payload.distance}} m</span></div>\n</div>",
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
        "id": "a57f569.40ae9a8",
        "type": "template",
        "z": "ea3fc4f2.ca0968",
        "name": "css",
        "field": "style",
        "fieldType": "msg",
        "format": "html",
        "syntax": "mustache",
        "template": "#data {\n    position:fixed;\n    top: 50%;\n    left: 50%;\n    width:50em;\n    height:18em;\n    margin-top: -9em; /*set to a negative number 1/2 of your height*/\n    margin-left: -15em; /*set to a negative number 1/2 of your width*/\n    border: 3px solid #ccc;\n    background-color: lightgrey;\n}\n\n#duration {\n    background-color:yellow;\n}\n\n#average_speed {\n    background-color:aquamarine;\n}\n\n#distance {\n    text-color:orange;\n}\n\n.text {\n    font-size:44px;\n}\n\n.value {\n    font-size:44px;\n}",
        "x": 682,
        "y": 118,
        "wires": [
            [
                "f7d55276.8c506",
                "f658d5bf.481458"
            ]
        ]
    },
    {
        "id": "f658d5bf.481458",
        "type": "function",
        "z": "ea3fc4f2.ca0968",
        "name": "New Values",
        "func": "msg.payload = \"New Values...\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 740,
        "y": 219,
        "wires": [
            [
                "3e66cb6f.ab1814"
            ]
        ]
    },
    {
        "id": "e06a7a01.9969c8",
        "type": "inject",
        "z": "ea3fc4f2.ca0968",
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
                "31b0e3ec.d6b5ec"
            ]
        ]
    },
    {
        "id": "31b0e3ec.d6b5ec",
        "type": "function",
        "z": "ea3fc4f2.ca0968",
        "name": "Random",
        "func": "duration = (Math.random() * 10.0).toPrecision(3)\nspeed = (Math.random() * 1.0).toPrecision(3)\ndistance = (Math.random() * 20.0).toPrecision(2)\nmsg.payload = '{\"duration\": ' + duration + ', \"speed\": ' + speed + ', \"distance\": ' + distance + '}'\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 361,
        "y": 261,
        "wires": [
            [
                "75f8b147.eb03e"
            ]
        ]
    },
    {
        "id": "a0484699.b57aa8",
        "type": "inject",
        "z": "ea3fc4f2.ca0968",
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
                "8ffd1135.bec8d"
            ]
        ]
    },
    {
        "id": "44fed1da.5c8e",
        "type": "ui_ui_control",
        "z": "ea3fc4f2.ca0968",
        "name": "Switch",
        "x": 772,
        "y": 278,
        "wires": [
            []
        ]
    },
    {
        "id": "d6a59694.1eb128",
        "type": "function",
        "z": "ea3fc4f2.ca0968",
        "name": "to Tab Speeds",
        "func": "msg.payload = 'Speeds'\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 564,
        "y": 270,
        "wires": [
            [
                "44fed1da.5c8e",
                "9fe88e11.78aa2"
            ]
        ]
    },
    {
        "id": "9fe88e11.78aa2",
        "type": "delay",
        "z": "ea3fc4f2.ca0968",
        "name": "",
        "pauseType": "delay",
        "timeout": "5",
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
                "b3944292.5b09d"
            ]
        ]
    },
    {
        "id": "ecf6243a.f1c3d8",
        "type": "ui_ui_control",
        "z": "ea3fc4f2.ca0968",
        "name": "Switch",
        "x": 842,
        "y": 394,
        "wires": [
            []
        ]
    },
    {
        "id": "b3944292.5b09d",
        "type": "function",
        "z": "ea3fc4f2.ca0968",
        "name": "to Tab Highscore",
        "func": "msg.payload = 'Highscore'\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 703,
        "y": 345,
        "wires": [
            [
                "ecf6243a.f1c3d8"
            ]
        ]
    },
    {
        "id": "3422f4b8.11de0c",
        "type": "mqtt in",
        "z": "ea3fc4f2.ca0968",
        "name": "new Highscore Message",
        "topic": "newHighscore",
        "qos": "2",
        "broker": "8148060c.347b58",
        "x": 197,
        "y": 328,
        "wires": [
            [
                "4bbc408c.570a9"
            ]
        ]
    },
    {
        "id": "8ffd1135.bec8d",
        "type": "function",
        "z": "ea3fc4f2.ca0968",
        "name": "Fixed Highscore",
        "func": "var name1 = \"Herbert Brown\";\nmsg.payload = '{\"list\": [{\"start_time\": 1521816916.2528725, \"py/object\": \"HighScoreEntry.HighScoreEntry\", \"duration\": 0.19170522689819336, \"speed\": 37.557661397639514, \"stop_time\": 1521816916.4445777, \"distance\": 2000, \"name\": \"' + name1 + '\", \"record_date\": {\"py/object\": \"datetime.date\", \"__reduce__\": [{\"py/type\": \"datetime.date\"}, [\"B+IDFw==\"]]}}, {\"start_time\": 1521816918.4935858, \"py/object\": \"HighScoreEntry.HighScoreEntry\", \"duration\": 0.21306467056274414, \"speed\": 33.792556884177166, \"stop_time\": 1521816918.7066505, \"distance\": 2000, \"name\": \"Hans\", \"record_date\": {\"py/object\": \"datetime.date\", \"__reduce__\": [{\"py/type\": \"datetime.date\"}, [\"B+IDFw==\"]]}}, {\"start_time\": 1521816656.9219244, \"py/object\": \"HighScoreEntry.HighScoreEntry\", \"duration\": 0.335817813873291, \"speed\": 21.440196745240755, \"stop_time\": 1521816657.2577422, \"distance\": 2000, \"name\": \"Hans\", \"record_date\": {\"py/object\": \"datetime.date\", \"__reduce__\": [{\"py/type\": \"datetime.date\"}, [\"B+IDFw==\"]]}}], \"py/object\": \"HighScoreList.HighScoreList\", \"max_age\": {\"py/reduce\": [{\"py/type\": \"datetime.timedelta\"}, {\"py/tuple\": [1, 0, 0]}, null, null, null]}, \"max_count\": 3}';\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 264,
        "y": 464,
        "wires": [
            [
                "4bbc408c.570a9"
            ]
        ]
    },
    {
        "id": "b6cd2a00.9b18f8",
        "type": "function",
        "z": "ea3fc4f2.ca0968",
        "name": "formatData",
        "func": "var data = msg.payload; \nfor (i = 0; i < msg.payload.list.length; i++) \n{ \n    msg.payload.list[i].rank = i+1;\n    msg.payload.list[i].duration = msg.payload.list[i].duration.toFixed(4);\n    msg.payload.list[i].speed = msg.payload.list[i].speed.toFixed(5);\n    msg.payload.list[i].distance = msg.payload.list[i].distance.toFixed(4);\n}\nvar newMsg = {payload: data };\nreturn [ msg, newMsg ];\n",
        "outputs": 2,
        "noerr": 0,
        "x": 487,
        "y": 624,
        "wires": [
            [
                "34b503a5.889eac"
            ],
            [
                "f87050c0.c0e08"
            ]
        ]
    },
    {
        "id": "f87050c0.c0e08",
        "type": "debug",
        "z": "ea3fc4f2.ca0968",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 704,
        "y": 777,
        "wires": []
    },
    {
        "id": "bacf627c.d9378",
        "type": "function",
        "z": "ea3fc4f2.ca0968",
        "name": "formatData",
        "func": "msg.payload.duration = msg.payload.duration.toFixed(4);\nmsg.payload.speed = msg.payload.speed.toFixed(5);\nmsg.payload.distance = msg.payload.distance.toFixed(4);\nreturn msg\n",
        "outputs": 1,
        "noerr": 0,
        "x": 586,
        "y": 174,
        "wires": [
            [
                "a57f569.40ae9a8"
            ]
        ]
    },
    {
        "id": "87cd78ea.8a4c68",
        "type": "ui_group",
        "z": "ea3fc4f2.ca0968",
        "name": "Highscore",
        "tab": "fc406816.5a7808",
        "disp": false,
        "width": "17",
        "collapse": false
    },
    {
        "id": "8148060c.347b58",
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
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "willTopic": "",
        "willQos": "0",
        "willPayload": ""
    },
    {
        "id": "7e2298f1.493228",
        "type": "ui_group",
        "z": "",
        "name": "Tabelle",
        "tab": "cdc262a2.5bd2b",
        "disp": false,
        "width": "17",
        "collapse": false
    },
    {
        "id": "fc406816.5a7808",
        "type": "ui_tab",
        "z": "",
        "name": "Highscore",
        "icon": "dashboard",
        "order": 2
    },
    {
        "id": "cdc262a2.5bd2b",
        "type": "ui_tab",
        "z": "",
        "name": "Speeds",
        "icon": "dashboard",
        "order": 3
    }
]
```
