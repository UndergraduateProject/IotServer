import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
import requests as rq
import socketio
src = 'http://140.117.71.98:8000/api/Humidtemp/'


#socket
sio = socketio.Client()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './reactpageagent-rehl-e8f6c376b8ef.json'
DIALOGFLOW_PROJECT_ID = 'reactpageagent-rehl'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'ni_chatbot'

#text_to_be_analyzed = "hi"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)

def get_response(text_to_be_analyzed="ni_chatbot"):
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input) # dialogflow database

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        #print(response)
    except InvalidArgument as e:
        print(e)
        raise
    return response


# display
def temperature():
    res = rq.get(src)
    data = res.json()
    count = data["count"]
    url = src + str(count)
    res = rq.get(url)
    data = res.json()
    temperature = data['temperature']
    msg = response.query_result.fulfillment_text + str(temperature)
    sio.emit('chatbot', msg)
    print(response.query_result.fulfillment_text, temperature)

def humidity():
    res = rq.get(src)
    data = res.json()
    count = data["count"]
    url = src + str(count)
    res = rq.get(url)
    data = res.json()
    humidity = data['humidity']
    msg = response.query_result.fulfillment_text + str(humidity)
    sio.emit('chatbot', msg)
    print(response.query_result.fulfillment_text, humidity)

# action
def action_watering():
    print("action_watering ")

def action_light():
    print("action_watering")
    
def action_fan():
    print("action_fan")

#information 
def get_output(response):
    print("input text:", response.query_result.query_text)
    #print("intent:", response.query_result.intent.display_name)
    #print("intent's confidence:", response.query_result.intent_detection_confidence)
    print("response:", response.query_result.fulfillment_text)    

@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on("chatbot")
def on_message(data):
    print("message" ,data)
    global response
    response = get_response(data)
    # get_output(response)
    print("keyword: ", response.query_result.intent.display_name)
    #command+shift+p -> interpreter-> copy bin/python
    keyword = response.query_result.intent.display_name
    confidence = response.query_result.intent_detection_confidence

    if keyword == "temperature":
        temperature()
    elif keyword == "lighting": 
        humidity()
    elif keyword == "open lighting": 
        action_light()
    elif keyword == "open fan":
        action_fan()
    elif keyword == "open watering":
        action_watering()
    elif keyword == "Default Fallback Intent":
        sio.emit("chatbot", "Sorry, what was that?")
        print("Sorry, what was that?")
    else:
        sio.emit('chatbot', response.query_result.fulfillment_text)

    

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

sio.connect("http://140.117.71.98:4001")

while True:
    None