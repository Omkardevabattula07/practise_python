import base64
import json
from asgiref.sync import sync_to_async
from django.core.files.base import ContentFile
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message ,Room

class chatconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
            
        )
        
    async def receive (self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type','text')
        
        if message_type == 'text':
            message = data['message']
            await self.save_message(self.room_name,message)
            