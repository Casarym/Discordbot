import discord
from discord import Option
from discord.ext import commands
import discord.utils

# бот для команд, выданы все намерения
bot = commands.Bot(intents=discord.Intents.all())

# подробнее про это событие: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#async-def-on_ready
@bot.event
async def on_ready():
	print(f'{bot.user} запущен и готов к работе!\n')

# подробнее про это событие: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#async-def-on_message
@bot.slash_command(name='test', description='Удаляет контекст и выводит сообщение "Успешный тест!"')
async def test(ctx):
# список свойств и методов контекста можно найти в документации по запросу context
        await ctx.respond('Успешный тест!')



@bot.slash_command(name='obideli', description='Поддерживает в трудную минуту')
async def obideli(ctx):
    a = str(ctx.author)
    await ctx.respond(f'Не обижайся, {ctx.author.mention}')

#@bot.slash_command(name='gvrole', description='Дает роль')
#async def gvrole(ctx,role4: discord.Role,
#                 choice: Option(str, description="роль", required=True, choices=["test"])
#                                ):
#        author = ctx.author
#        guild = bot.get_guild
        #role_1 = ctx.guild.get_role(1146026956534583326)
        #role3 = get(author.server.roles, name="test")
        #for arg in choice:
                #role_id = discord.utils.get(guild.roles,name="test")
#        await author.add_roles(role4)
#        await ctx.respond('Готово')

@bot.slash_command(name='giverole', description='Дает роль')
async def addrole(ctx, member: discord.Member = None, *, role: discord.Role = None):
    #guild = ctx.get_guild
    #role = discord.utils.get(guild.server.roles,name="Администратор")
    try:
        if role == None:
            await ctx.send(f'Provide a role to add')
            return

        if member == None:
            await ctx.send(f'Provide a member to add a role')
            return

        await member.add_roles(role)
        await ctx.send(f"Successfully added role, {role} to {member.name}")
    except discord.errors.Forbidden:
        await ctx.send("Sorry, i dont have enough permissions")

@bot.event
async def on_message(message):
        if message.author.bot:
                return
        await bot.process_commands(message)

@bot.slash_command(name='activity', description='Смотрит активность')
async def activity(ctx, user: discord.Member):
    #try:
    for activity in user.activities:
        if activity.type == discord.ActivityType.playing:
            await ctx.send(f"{user.name} is playing {activity.name}")
            return
    await ctx.send(f"{user.name} is not playing anything.")
    # except discord.NotFound:
    #     await ctx.send("User not found.")


@bot.slash_command(name='members', description='Смотрит пользователей')
async def members(ctx):
    memers = commands.Bot(intents=discord.Intents.all())
    for guild in bot.guilds:
        for member in guild.members:
            print(member)  # or do whatever you wish with the member detail
            for activity in members.activities:
                if activity.type == discord.ActivityType.playing:
                    await ctx.send(f"{members.name} is playing {activity.name}")
                    return
    await ctx.send(memers)
    return

@bot.slash_command(name='join_vc', description='Заходит в голосовой канал')
async def join(ctx):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            filename = await YTDLSource.from_url("https://www.youtube.com/watch?v=6nukE7WZc6w", loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")
# запускаем бота
bot.run('token')
