import paho.mqtt.client as paho
import Adafruit_DHT

def on_publish(client, userdata, mid):       
        print("mid: "+str(mid))
        
client = paho.Client()
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 26)
    data = "Humidity: "+str(humidity)+ " | " + "Temperature: "+ " | "+ str(temperature)
    client.publish("rpi/mess", str(data), qos=1)
