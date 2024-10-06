import discord
from discord.ext import tasks, commands
from discord import app_commands
from discord.utils import get

class Bot(commands.Bot): 
    def __init__(self, command_prefix, self_bot, model):
        commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot, intents=discord.Intents.all())
        self.prefix = command_prefix
        self.model = model
        self.add_commands()

    def add_commands(self): 
        @self.tree.command(name="status")
        async def status(ctx):
            await ctx.channel.send("Bot is online!")

        @self.tree.command(name="clear_history")
        async def clear_history(ctx): 
            self.model.clear_history()
            await ctx.channel.send("History is cleared!")

        @self.event
        async def on_message(message): 
            if message.author.bot:
                return
    
            if message.content.startswith(self.prefix):
                await message.channel.send(self.model.reply(message.content[1:], message.author.name))

    async def on_ready(self):
        print(f"Bot {self.user.display_name} is connected to server.")