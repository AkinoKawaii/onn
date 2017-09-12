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
    await client.change_presence( game=discord.Game( name="Onika Studio", type = 1))

@client.event
async def on_message(message):
    random_color = colors()
 #   if message.content.startswith('=ok'):
     #   await client.send_message(message.channel,'ok')
    if message.content.startswith('order'):
        await client.send_message(message.channel,"""```         
Official bot from OS by Akino
```""")  
    elif message.content.startswith('o!stat'):
        try:
            if message.channel.id !='274387797140570112':
                coloursman = int(random_color['color'])
                if message.content == 'o!stat':
                    discord.Member = None
                    author = message.author
                    if not discord.Member :
                        discord.Member = message.author
                    roles = [x.name for x in discord.Member.roles if x.name != "@everyone"]
                    if not roles: roles = ["None"]
                    data = "\n"
                    data += "Name: {}\n".format(escape_mass_mentions(str(discord.Member)))
                    data += "Nickname: {0}\n".format(discord.Member.display_name)
                    data += "ID: {}\n".format(discord.Member.id)
                    passed = (message.timestamp - discord.Member.created_at).days
                    data += "Created: {} days ago.\n".format(passed)
                    passed = (message.timestamp - discord.Member.joined_at).days
                    data += "Joined: {} days ago\n".format(passed)
                    data += "Server: {}\n".format(discord.Member.server)
                    data += "Status: {}\n".format(discord.Member.status)
                    data += "Playing: {}\n".format(discord.Member.game)
                    data += "Bot Account: {}\n".format(discord.Member.bot)
                    data += "Roles: {}\t".format(", ".join(roles))
                    data += "**({0})**\n".format(len(roles))
                    data += "Top Role: {}\n\n".format(discord.Member.top_role)
                
                    user_em = discord.Embed(
                    description=data)
                    user_em.set_author(
                    name="Your Status :")
                    user_em.set_image(url = discord.Member.avatar_url)
                    user_em.color=coloursman
                
                    await client.send_message(message.channel,embed = user_em)          
          
                else:
                    check_tagger = re.findall('o!stat\s(.*)',message.content)
        
                    hilol_ = ' '.join(check_tagger)
                    no1is = re.sub(r'[^\w]', ' ', hilol_)
                    thisiscool = no1is.replace(' ','')
                
                    member_id = message.author.server.get_member(user_id = thisiscool)
                    
                    discord.Member = member_id 
                    roles = [x.name for x in discord.Member.roles if x.name != "@everyone"]
                    if not roles: roles = ["None"]
                    data = "\n"
                    data += "Name: {}\n".format(escape_mass_mentions(str(discord.Member)))
                    data += "ID: {}\n".format(discord.Member.id)
                    passed = (message.timestamp - discord.Member.created_at).days
                    data += "Created: {} days ago\n".format(passed)
                    passed = (message.timestamp - discord.Member.joined_at).days
                    data += "Joined: {} days ago\n".format(passed)
                    data += "Server: {}\n".format(discord.Member.server)
                    data += "Status: {}\n".format(discord.Member.status)
                    data += "Playing: {}\n".format(discord.Member.game)
                    data += "Bot Account: {}\n".format(discord.Member.bot)
                    data += "Roles: {}\t".format(", ".join(roles))
                    data += "**({0})**\n".format(len(roles))
                    data += "Top Role: {}\n\n".format(discord.Member.top_role)
                    user_em = discord.Embed(
                    description=data)
                    user_em.set_author(
                    name="User Status :")
                    user_em.set_image(url = discord.Member.avatar_url)
                    user_em.color=coloursman
                
                    await client.send_message(message.channel,embed = user_em)
  
        except Exception as e: print (str(e))
                  
    elif message.content.startswith('!say'):
        if message.content == '!say':return
        else:
            text = re.findall('!say\s(.*)',message.content)
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
