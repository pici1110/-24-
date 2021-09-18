import discord
import ds

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('login')
    print(client.user.id)
    print('-----------------------------------')
    game = discord.Game("동식이다냥")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("동식아 들어와"):
        await message.channel.send("집에 들어간다냥")
    if message.content.startswith("동식아 사랑해"):
        await message.channel.send("나도 사랑한다냥")
    if message.content.startswith("동식아 뭐해?"):
        await message.channel.send("젤리 빨래 한다냥")
    if message.content.startswith("동식아 행복해?"):
        await message.channel.send("완전 행복하다냥!")
    if message.content.startswith("동식아 발"):
        await message.channel.send("여기 있다냥")
    if message.content.startswith("동식아 손"):
        await message.channel.send("여기 있다냥!")
    if message.content.endswith("동식아"):
        await message.channel.send("냥?")
    if message.content.startswith("동식아 안녕"):
        await message.channel.send("안녕하다냥")
    if message.content.startswith("동식아 쓰담쓰담"):
        await message.channel.send("기분 좋다냥")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
