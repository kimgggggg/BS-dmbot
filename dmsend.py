
# 봉순#6959 : MASS DM BOT SOURCE


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('DM봇')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #742723086037680250
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="★★제목★★", value=msg, inline=True)
                        embed.set_footer(text="https://open.kakao.com/o/gR7DGEKc")
                        await i.send(embed=embed)
                except:
                    pass


client.run('Nzg1Nzg4MDIxNDU0NjY3Nzc2.X888Hw.XA1qkN04lYgMyecOBiZumXbb9aU')
