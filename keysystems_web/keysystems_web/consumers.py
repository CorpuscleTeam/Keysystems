# import json
# from channels.generic.websocket import WebsocketConsumer
#
# import logging
#
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         logging.warning(">>>>>>>>>>>>>>>>ChatConsumer connect")
#         self.accept()
#
#     def disconnect(self, close_code):
#         logging.warning(">>>>>>>>>>>>>>>>ChatConsumer disconnect")
#         pass
#
#     def receive(self, *, text_data):
#         logging.warning(">>>>>>>>>>>>>>>>ChatConsumer receive")
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
