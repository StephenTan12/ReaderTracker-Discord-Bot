import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!Novels':
        embed = discord.Embed(title='List of Novels', description='lawjgwlekg', color=0x00ff00)
        embed.add_field(name='I shall seal the heavans', value='hi')
        await message.channel.send(embed=embed)

client.run(os.getenv('TOKEN'))