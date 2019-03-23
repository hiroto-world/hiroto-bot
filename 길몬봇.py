import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='길몬봇 대화중', type=1))


@client.event
async def on_message(message):
    if message.content.startswith('길몬아 안녕'):
        await client.send_message(message.channel, "안녕하세요!")

    if message.content.startswith('!주사위'):
         roll = message.content.split(" ")
         rolld = roll[1].split("d")
         dice = 0
         for i in range(1, int(rolld[0])+1):
             dice = dice + random.randint(1, int(rolld[1]))
         await client.send_message(message.channel, str(dice))

    if message.content.startswith('!골라'):
         choice = message.content.split(" ")
         choicenumber = random.randint(1, len(choice)-1)
         choiceresult = choice[choicenumber]
         await client.send_message(message.channel, choiceresult)

    if message.content.startswith('!뭐먹지'):
        food = "짜장면 짬뽕 라면 밥 굶기"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!메모장쓰기'):
        file = open("길몬봇메모장.txt", "w")
        file.write("안녕하세요")
        file.write("인삿말")
        file.close()

    if message.content.startswith("!메모장읽기"):
        file = open("길몬봇메모장.txt")
        await client.send_message(message.channel, file.read())
        file.close()


client.run('NTUxOTU4ODMyNjU0MzE5NjI3.D14k-A.J-Yh7j3Mf_tyu_DvnGEvvwb4poI')