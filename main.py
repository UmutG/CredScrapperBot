import discord
import codecs
from pytz import timezone, all_timezones


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('/start_scanner'):       
            text_channel_list = []
            for server in client.guilds:
                for channel in server.channels:
                    if str(channel.type) == 'text':
                        text_channel_list.append(channel)
            for channel_name in text_channel_list:
                with codecs.open(f'logs/{channel_name}.log', 'a', 'utf-8') as f:
                    async for message in channel_name.history(limit=200, oldest_first=True):
                        f.write(f'{message.created_at.astimezone(timezone("Asia/Istanbul")).strftime( "%Y-%m-%d %X")} | #{message.channel} | {message.author} => {message.content}\n')
                    f.close()

        if message.content.startswith(''):
            print(f'{message.created_at.astimezone(timezone("Asia/Istanbul")).strftime( "%Y-%m-%d %X")} | #{message.channel} | {message.author} => {message.content}')
            

intents = discord.Intents.default()
intents.message_content = True

with open('.env', 'r') as f:
    bot_token = f.read()
    f.close()

client = MyClient(intents=intents)
client.run(bot_token)
