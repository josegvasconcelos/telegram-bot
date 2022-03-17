import os
from dotenv import load_dotenv
import random
import telebot


load_dotenv()
API_KEY: str = os.environ.get("API_KEY")

pery_jokes: list = ["Qual o dev que põe medo em todo mundo?\n\nO Perygoso.",
                    "O que fazer quando um dev sobe código quebrado em produção?\n\nChamar a Perycia.",
                    "Qual a maior diferença entre um dev junior e um dev senior?\n\nA exPeryência.",
                    "O que o dev foi fazer no SESMT?\n\nPegar seus EPerys e fardamentos.",
                    "Qual a cidade natal dos devs?\n\nPerymirim.",
                    "Como se mede a circunferência abdominal de um dev?\n\nCalculando o Perymetro."]

bot: telebot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["piadaComPery"])
def pery_joke(message) -> None:
    pery_joke_text = random.choice(pery_jokes)
    bot.send_message(message.chat.id, pery_joke_text)


@bot.message_handler(commands=["start"])
def start(message) -> None:
    start_text = '''
Clica no link ou digita no chat o comando que quiser executar:
/piadaComPery
'''
    bot.send_message(message.chat.id, start_text)


@bot.message_handler()
def default_answer(message) -> None:
    default_text = '''
Fala tu, aqui é o Zevas!

Clica no link ou digita /start pra batermos um papo.
'''
    bot.send_message(message.chat.id, default_text)


bot.polling()
