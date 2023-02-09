import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith(''):
            print(f'{message.created_at.strftime("%Y-%m-%d %H:%M:%S")} | {message.author} => {message.content}')
            

intents = discord.Intents.default()
intents.message_content = True

with open('.env', 'r') as f:
    bot_token = f.read()
    f.close()

client = MyClient(intents=intents)
client.run(bot_token)
