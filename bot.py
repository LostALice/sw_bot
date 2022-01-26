#Code by Aki.no.Alice@TyrantRex

from discord.ext import commands
from datetime import date
from os import getenv
import discord,json


client = commands.Bot(command_prefix="-")
member_list = {}
id_list = {}

def render(members) -> str:
    txt = "成員:\n"
    for member in members:
        txt += f"{members.index(member)+1}.{member :>3}\n"
    return txt

#on ready
@client.event
async def on_ready():
    print("Soul Worker bot ready!",flush=True)

#招募 daze!
@client.command(help="招募",aliases=["r","R"])
async def recruit(ctx):
    global msg,embed
    embed = discord.Embed(title=f"晚上招募{date.today()}",color=discord.Color.from_rgb(255, 255, 255))

    embed.add_field(name="1️⃣:女王[22:40]",value="成員:",inline=False)
    embed.add_field(name="2️⃣:太陽[23:00]",value="成員:",inline=False)
    embed.add_field(name="3️⃣:英八[太陽後]",value="成員:",inline=False)

    emoji = ["1️⃣","2️⃣","3️⃣"]
    msg = await ctx.channel.send("@here",embed=embed)
    for e in emoji:
        await msg.add_reaction(emoji=e)

#on removing reaction
@client.event
async def on_raw_reaction_remove(payload):
    global msg,embed,id_list

    guild = client.get_guild(payload.guild_id)
    user = await guild.fetch_member(payload.user_id)
    user = user.display_name
    _id = str(payload.message_id)

    try:
        with open(f"./json/{int(_id)}id.json","r+",encoding="utf-8") as f:
            id_list = json.load(f)
    except:
        pass

    if payload.user_id == 922860477057474571:
        return

    if str(payload.emoji) == "1️⃣":
        if payload.user_id in id_list[_id][0]["queen"]:
            id_list[_id][0]["queen"].remove(payload.user_id)
        member_list = []
        for i in id_list[_id][0]["queen"]:
            user = await guild.fetch_member(i)
            user = user.display_name
            member_list.append(user)
        embed.remove_field(0)
        embed.insert_field_at(0,name="1️⃣:女王[22:40]",value=render(member_list),inline=False)
        await msg.edit(embed=embed)

    if str(payload.emoji) == "2️⃣":
        if payload.user_id in id_list[_id][0]["sun"]:
            id_list[_id][0]["sun"].remove(payload.user_id)
        member_list = []
        for i in id_list[_id][0]["sun"]:
            user = await guild.fetch_member(i)
            user = user.display_name
            member_list.append(user)
        embed.remove_field(1)
        embed.insert_field_at(1,name="2️⃣:太陽[23:00]",value=render(member_list),inline=False)
        await msg.edit(embed=embed)

    if str(payload.emoji) == "3️⃣":
        if payload.user_id in id_list[_id][0]["prime"]:
            id_list[_id][0]["prime"].remove(payload.user_id)
        member_list = []
        for i in id_list[_id][0]["prime"]:
            user = await guild.fetch_member(i)
            user = user.display_name
            member_list.append(user)
        embed.remove_field(2)
        embed.insert_field_at(2,name="3️⃣:英八[太陽後]",value=render(member_list),inline=False)
        await msg.edit(embed=embed)

    print(date.today(),id_list,flush=True)

    with open(f"./json/{int(_id)}id.json","w+",encoding="utf-8") as f:
        f.write(json.dumps(id_list,ensure_ascii=False))

#on adding reaction
@client.event
async def on_raw_reaction_add(payload):
    global msg,embed,id_list

    guild = client.get_guild(payload.guild_id)
    _id = str(payload.message_id)

    try:
        with open(f"./json/{int(_id)}id.json","r+",encoding="utf-8") as f:
            id_list = json.load(f)
    except:
        id_list = {}
        id_list[_id] = [
            {
                "queen": [],
                "sun": [],
                "prime": []
            }
        ]

    if payload.user_id == 922860477057474571:
        return

    if str(payload.emoji) == "1️⃣":
        if not payload.user_id in id_list[_id][0]["queen"]:
            id_list[_id][0]["queen"].append(payload.user_id)
        member_list = []
        for i in id_list[_id][0]["queen"]:
            user = await guild.fetch_member(i)
            user = user.display_name
            member_list.append(user)
        embed.remove_field(0)
        embed.insert_field_at(0,name="1️⃣:女王[22:40]",value=render(member_list),inline=False)
        await msg.edit(embed=embed)

    if str(payload.emoji) == "2️⃣":
        if not payload.user_id in id_list[_id][0]["sun"]:
            id_list[_id][0]["sun"].append(payload.user_id)
        member_list = []
        for i in id_list[_id][0]["sun"]:
            user = await guild.fetch_member(i)
            user = user.display_name
            member_list.append(user)
        embed.remove_field(1)
        embed.insert_field_at(1,name="2️⃣:太陽[23:00]",value=render(member_list),inline=False)
        await msg.edit(embed=embed)

    if str(payload.emoji) == "3️⃣":
        if not payload.user_id in id_list[_id][0]["prime"]:
            id_list[_id][0]["prime"].append(payload.user_id)
        member_list = []
        for i in id_list[_id][0]["prime"]:
            user = await guild.fetch_member(i)
            user = user.display_name
            member_list.append(user)
        embed.remove_field(2)
        embed.insert_field_at(2,name="3️⃣:英八[太陽後]",value=render(member_list),inline=False)
        await msg.edit(embed=embed)

    print(date.today(),id_list,flush=True)

    with open(f"./json/{int(_id)}id.json","w+",encoding="utf-8") as f:
        f.write(json.dumps(id_list,ensure_ascii=False))

if __name__ == "__main__":
    client.run(getenv("token"))
