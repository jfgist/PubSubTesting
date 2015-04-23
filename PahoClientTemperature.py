import paho.mqtt.client as paho
import json, time

# device credentials
device_id        = '<DEVICE_ID>'      # * set your device id (will be the MQTT client username)
device_secret    = '<DEVICE_SECRET>'  # * set your device secret (will be the MQTT client password)
random_client_id = '<CLIENT_ID>'      # * set a random client_id (max 23 char)

# --------------- #
# Callback events #
# --------------- #

# connection event
def on_connect(client, data, flags, rc):
    print('Connected, rc: ' + str(rc))

# subscription event
def on_subscribe(client, userdata, mid, gqos):
    print('Subscribed: ' + str(mid))

# received message event
def on_message(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json.loads(json_data)['properties'][0]['value']

    # confirm changes to Leylan
    client.publish(out_topic, json_data)


# ------------- #
# MQTT settings #
# ------------- #

# create the MQTT client
client = paho.Client(client_id=random_client_id, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

# device topics
in_topic  = 'devices/' + device_id + '/get'  # receiving messages
out_topic = 'devices/' + device_id + '/set'  # publishing messages

# client connection
client.username_pw_set(device_id, device_secret)  # MQTT server credentials
client.connect("178.62.108.47")                   # MQTT server address
client.subscribe(in_topic, 0)                     # MQTT subscribtion (with QoS level 0)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = client.loop()
    button_payload = 'off'
    if led_status == GPIO.HIGH:
    temperature = 11

    payload = { 'properties': [{ 'id': '54033694bdd5392354000006', 'value': temperature }] }
    client.publish(out_topic, json.dumps(payload))
    time.sleep(20)

print('rc: ' + str(rc))
