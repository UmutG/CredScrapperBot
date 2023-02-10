import discord
import codecs
from pytz import timezone, all_timezones
from datetime import datetime
import time
import os
import sys



def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, u"█"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('/startscanner'):
            if message.author.id == 448224340530561043 or message.author.id == 637386194283659314 or message.author.id == 839183314833244210 or message.author.id == 257935638018523136:
                text_channel_list = []
                
                # Getting user messages and creating folder with current time
                try:
                    print(message.author);currentDateAndTime = datetime.now().strftime("%Y_%m_%d-%H_%M" )
                    os.system(f"mkdir -p logs/{currentDateAndTime}");print(f'\033[93mlogs/{currentDateAndTime} has been created.\033[0m')
                except Exception as e:
                    print("Error:", e)

                for server in client.guilds:
                    for channel in server.channels:
                        if str(channel.type) == 'text':
                            text_channel_list.append(channel)

                for channel_name in progressbar(text_channel_list):
                    time.sleep(0.1)

                    async for message in channel_name.history(limit=None, oldest_first=True):
                        
                        with open('keywords.data', "r") as x:
                            keyword_data=x.read()
                            keywordlist = list(keyword_data.split("\n"))
                        
                        for keyword in keywordlist:                            
                            if keyword in message.content:
                                with codecs.open(f'logs/{currentDateAndTime}/{channel_name}.log', 'w', 'utf-8') as f:
                                    # Getting user messages with time zone
                                    f.write(f'{message.created_at.astimezone(timezone("Asia/Istanbul")).strftime( "%Y-%m-%d %X")} | #{message.channel} | {message.author} => {message.content}\n')
            print(f'\033[93m===== SCAN COMPLETED =====\033[0m')
        
        if message.content.startswith(''):
            print(f'{message.created_at.astimezone(timezone("Asia/Istanbul")).strftime( "%Y-%m-%d %X")} | #{message.channel} | {message.author} => {message.content}')

intents = discord.Intents.default()
intents.message_content = True

with open('.env', 'r') as f:
    bot_token = f.read()

client = MyClient(intents=intents)
client.run(bot_token)