print("hello world")
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Wczytywanie tokenu bota ze zmiennych środowiskowych
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN_SECRET")

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True


# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
bot = commands.Bot(command_prefix='$', intents=intents)

# Informacja bota o zalogowaniu sie w terminalu
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

# Komendy bota piszemy w ten sposób
@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem {bot.user}')

# A tu przykład komendy, która akceptuje również argument podany przez użytkownika po wpisaniu komendy
# W tym wypadku $laugh 5 wyświetli nam 'hahahahaha', ponieważ count wtedy przyjmuje wartość 5
@bot.command()
async def laugh(ctx, count = 3):
    await ctx.send("ha" * count)

bot.run(token=TOKEN)
