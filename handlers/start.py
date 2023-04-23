from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from dispatcher import dp
from aiogram import types
from main import Main
import vk_api
import config 
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

vk = Main()

@dp.message_handler(Command('start'))
async def on_start(message: types.Message):

    await message.answer('Привет, ' + str(message.from_user.full_name) + '\nЭто бот, который пересылает сообщения из твоей лички в вк прям сюда')  
    await vk.message(message.chat.id)
