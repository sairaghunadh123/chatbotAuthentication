from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize chatbot
chatbot = ChatBot('My Chatbot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
