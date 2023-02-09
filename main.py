import discord
import codecs
from pytz import timezone, all_timezones
from datetime import datetime
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('/start_scanner') or message.content.startswith('/startscanner'):       
            text_channel_list = []

            currentDateAndTime = datetime.now().strftime("%Y_%m_%d-%H_%M" )
            try:
                os.system(f"mkdir -p logs/{currentDateAndTime}");print(f'\033[93m logs/{currentDateAndTime} has been created.\033[0m')
            except Exception as e:
                print("Error:", e)

            for server in client.guilds:
                for channel in server.channels:
                    if str(channel.type) == 'text':
                        text_channel_list.append(channel)
            for channel_name in text_channel_list:

                async for message in channel_name.history(limit=200, oldest_first=True):

                    with open('keywords.data', "r") as x:
                        keyword_data=x.read()
                        keywordlist = list(keyword_data.split("\n"))
                    for keyword in keywordlist:
                        if keyword in message.content:
                            #print(astimezone(timezone("Asia/Istanbul")).strftime( "%Y-%m-%d %X"))

                            
                            with codecs.open(f'logs/{currentDateAndTime}/{channel_name}.log', 'w', 'utf-8') as f:
                                f.write(f'{message.created_at.astimezone(timezone("Asia/Istanbul")).strftime( "%Y-%m-%d %X")} | #{message.channel} | {message.author} => {message.content}\n')

        if message.content.startswith(''):
            print(f'{message.created_at.astimezone(timezone("Asia/Istanbul")).strftime( "%Y-%m-%d %X")} | #{message.channel} | {message.author} => {message.content}')
            

intents = discord.Intents.default()
intents.message_content = True

with open('.env', 'r') as f:
    bot_token = f.read()
    f.close()

client = MyClient(intents=intents)
client.run(bot_token)
