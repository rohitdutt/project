# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        #self.room_name = self.scope['url_route']['kwargs']['room_name']['userName']
        self.room_name = 'myroom'
        self.room_group_name = 'chat_%s' % self.room_name
        print("connected")
        print(self.room_group_name,"__________",self.channel_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        #print(self.room_group_name,self.channel_name)
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(

            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        userName= text_data_json['userName']
        pic="{%static 'myimg/logo.png'%}"
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'userName':userName,
                'pic':pic
            })
        '''
        self.send(text_data=json.dumps({
            'message': message
        }))
        '''
    # Receive message from room group

    def chat_message(self, event):
        message = event['message']
        userName=event['userName']
        pic=event['pic']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'userName':userName,
            'pic':pic,

        }))
'''
class privatchat(WebsocketConsumer):
    def connect(self):

        self.username = userName
        #self.room_name = 'myroom'
        #self.otheruser=self.scope['otheruser']
        print(username,otheruser)
        self.room_group_name = 'chat_%s' % self.username+self.otheruser
        print("connectedaaaaaaaaaaa")
        print(self.room_group_name,"__________",self.channel_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        #print(self.room_group_name,self.channel_name)
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(

            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        userName= text_data_json['userName']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'userName':userName
            })
        self.send(text_data=json.dumps({
            'message': message
        }))
    # Receive message from room group

    def chat_message(self, event):
        message = event['message']
        userName=event['userName']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'userName':userName
        }))
'''
