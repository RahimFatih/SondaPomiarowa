#!/usr/bin/python3
from paho.mqtt import client as mqtt_client
import random
import time


def connect_mqtt(broker_ip,broker_port,user_name,user_password,user_id):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(user_id)
    client.username_pw_set(user_name, user_password)
    client.on_connect = on_connect
    client.connect(broker_ip,int(broker_port))
    return client


def publish(client,topic,msg):
    time.sleep(1)
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")



if __name__ == '__main__':
    conf = {}
    with open("conf",'r') as f:
        for line in f:
            conf.update({line.split(' ')[0]:line.split(' ')[1].replace('\n','')})
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    client = connect_mqtt(conf["mosquitto_broker_ip"],conf["mosquitto_broker_port"],conf["mosquitto_user_name"],conf["mosquitto_user_passwd"],client_id)
    client.loop_start()
    publish(client,"python/mqtt","temp: 23")