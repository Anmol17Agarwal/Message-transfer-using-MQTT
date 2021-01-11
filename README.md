# Message-transfer-using-MQTT

### What is MQTT Protocol?
Message Queuing Telemetry Transport is a lightweight messaging protocol that provides resource-constrained network clients with a simple way to distribute telemetry information.
The protocol, which uses a publish/subscribe communication pattern, is used for machine-to-machine (M2M) communication and plays an important role in the internet of things (IoT).
The MQTT protocol surrounds two subjects: a client and a broker. An MQTT broker is a server, while the clients are the connected devices. When a device -- or client -- wants to send data to a server -- or broker-- it is called a publish. When the operation is reversed, it is called a subscribe.

![alt text](https://i.ytimg.com/vi/EIxdz-2rhLs/maxresdefault.jpg)

### Installing MQTT Library
Just run the following command to download MQTT library in RPI
```
sudo pip3 install paho-mqtt
```
