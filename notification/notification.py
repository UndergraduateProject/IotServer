import requests as eq
import json
import socketio

serverToken = 'AAAA-8iZSAo:APA91bFvUo6XC9h_IjAxOP9WCpGSfC-xJDhiu9IjCHUhn7Zk_bxhe1zvic2fj2AybNTmeS8aCY5ZcZ9eV_URayfsUyVNNoQBw9hzMMFPjzgXnPx9698MlwaKIS6h03CgAV2slGew1kAO'
deviceToken = 'ekaZCz5SKVc:APA91bFL733_FghXVduc4RWJNqwAEjNcnixZOdMFeb9cq2Frto2yo4TcVWN1sdSe1KOXXO_cXvPzxYghd1xluJim2PdFchMHhXBFkbjqS3XV2k8XMKK7nBM1LiHMS_JFw18K9MkI-Zjs'



sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on("notification")
def on_message(data):
  body = {
            'notification': data,
            'to':
                deviceToken,
            'priority': 'high',
          #   'data': dataPayLoad,
          }
  headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }
  response = rq.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
  token_url = 'http://140.117.71.98:8000/user/login/'
  warning_url = "http://140.117.71.98:8000/api/WarningRecord/"
  token_data = {'username': 'admin', 'password': 'rootroot'}
  res = rq.post(token_url, token_data)
  res = json.loads(res.text)
  headers= {'Authorization': res['token']}
  res = rq.post(warning_url, data = data, headers = headers)
  print(response.status_code)
  print(response.json())

    

@sio.on('disconnect')
def on_disconnect():
    # print('disconnected from server')
    pass

sio.connect("http://140.117.71.98:4001")

while True:
    None
  