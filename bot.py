import vk_api
from config import vkapitoken
from vk_api.longpoll import VkLongPoll, VkEventType
import chatreq

bh = vk_api.VkApi(token = vkapitoken)
give = bh.get_api()
longpoll = VkLongPoll(bh)

print('running...')

def send_message(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
       if event.to_me:
          message = event.text.lower()
          id = event.user_id
          send_message(id, str(chatreq.chat_request(message))) 