import vk_api
import config 
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from dispatcher import dp
from dispatcher import bot

class Main:

    def two_factor(self):
        code = input('Code? ')
        return code, True

    def register(self):
        vk_session = vk_api.VkApi(config.login, config.password, auth_handler=self.two_factor)

        vk_session.auth()

        vk = vk_session.get_api()

        print('ok!')        




    def example(self):
        
        vk_session = vk_api.VkApi(token=config.vk_api_token)
        vk = vk_session
        longpoll = VkLongPoll(vk)
        
        for event in longpoll.listen():
            
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                
                
                if event.text == 'Привет' or event.text == 'привет': 
                    api = vk.get_api()
                    name = api.users.get(user_ids = event.user_id)
                    if event.from_user: 
                        api.messages.send( 
                            user_id=event.user_id,
                            random_id = 123456,
                            message='Привки', 
                            
                )
                    elif event.from_chat: 
                        api.messages.send( 
                            chat_id=event.chat_id,
                            random_id = 123456,
                            message='Привет', 
                        
                ) 

    async def message(self, chat_id):
        
        vk_session = vk_api.VkApi(token=config.vk_api_token)
        vk = vk_session
        longpoll = VkLongPoll(vk)
        vk_api2 = vk_session.get_api()

        for event in longpoll.listen():
            
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                user_get=vk_api2.users.get(user_ids = (event.peer_id))
                user_get=user_get[0]
                first_name=user_get['first_name']
                last_name=user_get['last_name']
                full_name=first_name+" "+last_name
                message = f'{full_name}\n {event.text}'
                await bot.send_message(chat_id, message)
