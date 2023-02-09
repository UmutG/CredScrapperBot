import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    """
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        """
    
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True

with open('.env', 'r') as f:
    bot_token = f.read()
    f.close()

client = MyClient(intents=intents)
client.run(bot_token)

