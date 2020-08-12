import telepot
from ChatBotAPI import Chatbot 

telegram =  telepot.Bot("1142730357:AAEFLK4rNplnLuEoDZhIFcR50BsVztn_cjc")
bot = Chatbot("Santin")

def recebendoMsg(Msg):
    frase = bot.escutar(frase=Msg['text'])
    resp  = bot.pensar(frase)
    bot.falar(resp)
    #chatID = msg['chat]']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(Msg)
    telegram.sendMessage(chatID,resp)
    #print(Msg['text']) 
   

telegram.message_loop(recebendoMsg)

while True:
     pass