import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime

# Notification Consumer for enrolled students and teachers
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):  
        self.user_group_name = f'notifications_{self.scope["user"].username}'

        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )

    async def user_notification(self, event):
        notification_type = event.get('notification_type', 'generic')
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
            'notification_type': notification_type
        }))

# Chat consumer for the room chat in each course
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        username = self.scope['user'].username 
        join_message = f"{username} has joined the chat room."
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': join_message
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{username}: {message} ({timestamp})"

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': formatted_message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))