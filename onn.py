import discord
import asyncio
import re
import random
client = discord.Client()
def colors():
    list_colors = [{'color':"16777215"},{'color':"16711680"},{'color':"0"},{'color':"255"},{'color':"8388736"},{'color':"65535"},{'color':"8421504"},{'color':"8421504"},{'color':"10040319"}]
    random_color = random.choice(list_colors)
    random_color['color']
    return random_color
def escape_mass_mentions(text):
    words = {
        "@everyone": "@\u200beveryone",
        "@here": "@\u200bhere"
    }
    for k, v in words.items():
        text = text.replace(k, v)
    return text

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence( game=discord.Game( name="Onika Studio", type = 0))

@client.event
async def on_message(message):
    random_color = colors()
 #   if message.content.startswith('=ok'):
     #   await client.send_message(message.channel,'ok')
    if message.content.startswith('.say'):
        if message.content == '.say':return
        else:
            text = re.findall('.say\s(.*)',message.content)
            refined = ' '.join(text)
            await client.send_message(message.channel, '{0}'.format(refined))
            
#######################################after-before#######################################
    
@client.event
async def on_member_update(before, after):
        server = after.server
        member = after
        if before.name != after.name:
            fmt = ':pushpin: `{0.name}` *changed name to* `{1.name}`'
            await client.send_message(after.server, fmt.format(before, after))
        if before.nick != after.nick:
            fmt = ':pushpin: `{0.nick}` *changed nick to* `{1.nick}`'
            await client.send_message(after.server, fmt.format(before, after))
            if len(before.roles) > len(after.roles):
                for role in before.roles:
                    if role not in after.roles:
                        fmt =':warning: `{0.display_name}` *lost the* `{1.name` *role* :warning:'
                        await client.send_message(after.server, fmt.format(before, role))
            elif len(before.roles) < len(after.roles):
                for role in after.roles:
                    if role not in before.roles:
                         fmt =':warning: `{0.display_name}` *got the* `{1.name}` *role* :warning:'
                         await client.send_message(after.server, fmt.format(before, role))
                        
@client.event
async def on_member_remove(member):
    server = member.server
    fmt = ':fire: someone leave the {1.name} server'
    await client.send_message(server, fmt.format(member, server))
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Hi {0.mention} welcome to {1.name} have fun with us!:smile::v:'
    await client.send_message(server, fmt.format(member, server))
    
###################################Delete message###################################
@client.event
async def on_message(message):
    if message.content.startswith('!clear'):
        tmp = await client.send_message(message.channel, 'Clearing messages...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    
    print('Starting....')
client.run('MzU1OTI5NDc4NTI3OTc1NDQ1.DJT83w.jKKQEydYZs9x0d9xOmhJeCtSRT8')
