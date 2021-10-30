import requests
import json
import socketio

serverToken = 'AAAA-8iZSAo:APA91bFvUo6XC9h_IjAxOP9WCpGSfC-xJDhiu9IjCHUhn7Zk_bxhe1zvic2fj2AybNTmeS8aCY5ZcZ9eV_URayfsUyVNNoQBw9hzMMFPjzgXnPx9698MlwaKIS6h03CgAV2slGew1kAO'
deviceToken = 'ekaZCz5SKVc:APA91bFL733_FghXVduc4RWJNqwAEjNcnixZOdMFeb9cq2Frto2yo4TcVWN1sdSe1KOXXO_cXvPzxYghd1xluJim2PdFchMHhXBFkbjqS3XV2k8XMKK7nBM1LiHMS_JFw18K9MkI-Zjs'

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on("message")
def on_message(data):
  print("notification")
  body = {
            'notification': data,
            'to':
                deviceToken,
            'priority': 'high',
          #   'data': dataPayLoad,
          }
  response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
  print(response.status_code)
  print(response.json())

    

@sio.on('disconnect')
def on_disconnect():
    # print('disconnected from server')
    pass

sio.connect("http://140.117.71.98:4001")

while True:
    None
  