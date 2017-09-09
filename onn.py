import discord
import asyncio
import re
import random
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence( game=discord.Game( name="Onika Studio", type = 1))
    
###############SAY###############
@client.event
async def on_message(message):
        if message.content.startswith('.say'):
        if message.content == '.say':return
        else:
            text = re.findall('.say\s(.*)',message.content)
            refined = ' '.join(text)
            await client.send_message(message.channel, '{0}'.format(refined))

##########streamer##########
@client.event
async def on_member_update(before, after):
        server = after.server
        member = after
        if before.name != after.name:
            embed = discord.Embed(description='From {0.name} ({0.id}) to {1.name}'.format(before, after))
            embed.set_author( name='Name Changed', icon_url=member.avatar_url)
            await client.send_message(after.server, embed=embed)
        if before.nick != after.nick:
            embed = discord.Embed(description='From {0.nick} ({0.id}) to {1.nick}'.format(before, after))
            embed.set_author( name='Name Changed', icon_url=member.avatar_url)
            await client.send_message(after.server, embed=embed)
        if before.roles != after.roles:
            if len(before.roles) > len(after.roles):
                for role in before.roles:
                    if role not in after.roles:
                        embed = discord.Embed(description='{0.display_name} ({0.id}) lost the {1.name} role'.format(before, role))
                        embed.set_author(name='Role removed', icon_url=member.avatar_url)
                        await client.send_message(after.server, embed=embed)
            elif len(before.roles) < len(after.roles):
                for role in after.roles:
                    if role not in before.roles:
                        embed = discord.Embed(description='{0.display_name} ({0.id}) got the {1.name} role'.format(before, role))
                        embed.set_author(name='Role applied', icon_url=member.avatar_url)
                        await client.send_message(after.server, embed=embed)

##########join and leave##########
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
 
@client.event
async def on_member_remove(member):
    server = member.server
    fmt = '{0.mention} has left {1.name}!'
    await client.send_message(server, fmt.format(member, server))
 
@client.event
async def on_member_ban(member):
    server = member.server
    fmt = '{0.member} has been banned'
    await client.send_message(server, fmt.format(member, server))
    
    print('Starting....')
client.run('MzU1OTI5NDc4NTI3OTc1NDQ1.DJT83w.jKKQEydYZs9x0d9xOmhJeCtSRT8')
