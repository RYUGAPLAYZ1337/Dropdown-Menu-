import discord#made by sanemicodeZ
from discord.ext import commands#made by sanemicodeZ
class optionssanemi(discord.SelectOption):#made by sanemicodeZ
    def __init__(self, *, label, emoji=None, description=None):#made by sanemicodeZ
        super().__init__(label=label, emoji=emoji, description=description)#made by sanemicodeZ
class SamDropdown(discord.ui.Select):#made by sanemicodeZ
    def __init__(self):#made by sanemicodeZ
        options = [#made by sanemicodeZ
            optionssanemi(label="Home", emoji="<:Async_home:1239446100738445332>"),#made by sanemicodeZ
            optionssanemi(label="Anti-Nuke", emoji="<:Async_antinuke:1243099690422239262>"),#made by sanemicodeZ
            optionssanemi(label="Utility", emoji="<:Async_utility:1227986493335797901>"),#made by sanemicodeZ
            optionssanemi(label="Moderation", emoji="<:Async_mod:1243100467362267216>"),#made by sanemicodeZ
            optionssanemi(label="Games", emoji="<:Async_games:1243101018024054845> "),#made by sanemicodeZ
            optionssanemi(label="Music", emoji="<:Async_music:1243495167005294593> "),#made by sanemicodeZ
            optionssanemi(label="Giveaway", emoji="<:Async_giveway:1243099265132138565> "),#made by sanemicodeZ
            optionssanemi(label="Selfroles", emoji="<:Async_customrole:1239446889741680704>  "),#made by sanemicodeZ
            optionssanemi(label="Fun", emoji="<:Async_fun1:1243500881740173372>   ")#made by sanemicodeZ
        ]#made by sanemicodeZ
        #made by sanemicodeZ
#made by sanemicodeZ
        super().__init__(placeholder="Please select a page.", options=options, min_values=1, max_values=1)
    async def callback(self, interaction: discord.Interaction):
        view = self.view
        option_value = self.values[0]#made by sanemicodeZ
        #made by sanemicodeZ
#made by sanemicodeZ#made by sanemicodeZ
        #made by sanemicodeZ
        #made by sanemicodeZ
        #made by sanemicodeZ
        botavatar = interaction.client.user.avatar.url if interaction.client.user.avatar else interaction.client.user.default_avatar.url
        if option_value == "Anti-Nuke":                  
            view.embed.title = "**__Anti-Nuke__**"
            view.embed.description = "`antinuke antiban`, `antinuke antibot`, `antinuke antichannel-create`, `antinuke antichannel-delete`, `antinuke antichannel-update, antinuke antikick, antinuke antiprune, antinuke antirole-create`, `antinuke antirole-delete`, `antinuke antirole-update`, `antinuke antiserver`, `antinuke antiwebhook`, `antinuke disable`, `antinuke enable`, `antinuke punishment`, `antinuke recovery`, `antinuke status`, `antinuke whitelist add`, `antinuke whitelist remove`, `antinuke whitelist reset`, `antinuke whitelist show`, `antinuke whitelist`, `antinuke`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • Antinuke(soon)", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
        elif option_value == "Home":
            view.embed.title = "Hi, I'm Async"
            view.embed.description = "• Prefix for this server is `.`\n• Total commands: 280 | Usable by you (here): 272\n• [Get Async](https://discord.gg/SFm9B4ZyNW)\n• Type `.help <command | module>` for more info.\n```py\n<> - Required | [] - Optional```"
           
            view.embed.clear_fields()
            view.embed.set_thumbnail(url="https://media.discordapp.net/attachments/1189150446951071834/1243098613253537813/image.png?ex=66503d4d&is=664eebcd&hm=3624b9c798d66ad013f570bd8cb06de271feffbb0cb9f4e33fda9ac45a4076ad&=&format=webp&quality=lossless&width=556&height=544")
            view.embed.add_field(name="**__Main__**", value="<:Async_automod:1239445147276673026>  `:` AntiNuke\n<:Async_customrole:1239446889741680704>  `:` Selfroles\n<:Async_ticket:1239447463409225770>  `:` Tickets\n<:Async_giveway:1243099265132138565>  `:` Giveaways\n<:Async_antinuke:1243099690422239262>  `:` Automod\n<:Async_welcome:1243100089858134017>  `:` Welcomer")
            
            view.embed.add_field(name="**__Extra__**", value="<:Async_logs:1239445659103268877>  `:` Logging\n<:Async_mod:1243100467362267216> `:` Media\n<:Async_automod:1239445147276673026>  `:` Moderation\n<:Async_games:1243101018024054845>  `:` Games\n<:Async_utility:1227986493335797901>  `:` Utility \n<:Async_music:1243495167005294593> `:` Music")
            view.embed.set_footer(text="Made with 💖 by Async Developers.")


        elif option_value == "Utility":
            view.embed.title = "**__Utility__**"
            view.embed.description =  "`afk`, `av`, `channelinfo`, `membercount`, `ping`, `serverbanner`, `serverinfo`,`Channelinfo`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • Utility", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
            
        
        elif option_value == "Moderation":
            view.embed.title = "**__Moderation__**"
            view.embed.description =  "`Lock`,`lockall`,`unlock`,`unlockall `,`mute`,`unmute`,`ban`,`unban`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • Moderation", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
            
        elif option_value == "Games":
            view.embed.title = "**__Games__**"
            view.embed.description = "`battleship`,`chess`, `connect4`, `guess`, `hangman`, `memory`, `rps`, `tictactoe`, `twenty48`, `typerace`, `wordle`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • Games", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
        
            
        
        elif option_value == "Music":
            view.embed.title = "**__Music__**"
            view.embed.description = "`Soon`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • Music", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
        elif option_value == "Giveaway":
            view.embed.title = "**__Giveway__**"
            view.embed.description = "`Soon`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • Giveway", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
        elif option_value == "Selfroles":
            view.embed.title = "**__Selfroles__**"
            view.embed.description = "`Soon`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • SelfRoles", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
           

        elif option_value == "Fun":
            view.embed.title = "**__Fun__**"
            view.embed.description = "` waifu `,`slap `,`hug `,`compliment `,`neko`,`pat`,`calc`,`Ac`,`solve`"
            self.view.embed.clear_fields()
            view.embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
            view.embed.set_footer(text="Async • Fun", icon_url=botavatar)
            view.embed.set_thumbnail(url=botavatar)
        await interaction.response.edit_message(embed=self.view.embed)

        
        
        
        
        
class SamView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.embed = discord.Embed()
        self.add_item(SamDropdown())

        


class button1ok(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.link, label="Vote!", url="https://discord.gg/SFm9B4ZyNW")

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Redirecting you to our server!")


class GhostyView(discord.ui.View):
    def __init__(self, ctx: commands.Context):
        super().__init__()
        self.ctx = ctx
        vote = discord.ui.Button(label="Invite Me!", style=discord.ButtonStyle.danger, 
        url="https://discord.com/oauth2/authorize?client_id=1227127704760090716&permissions=8&scope=bot")
        self.add_item(vote)
        url = "https://discord.gg/SFm9B4ZyNW"
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label="Support Server!", url=url))
        self.add_item(button1ok())
        self.add_item(SamDropdown())
        self.embed = discord.Embed(title="Test Dropdown Menu",  color=discord.Color.green(), description="Choose from the dropdown menu below.")

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['h','HELP','menu'])
    async def helpx(self, ctx: commands.Context):
        member = ctx.author
        embed = discord.Embed(
            title="Hi, I'm Async", 
            description="• Prefix for this server is `$`\n• Total commands: 280 | Usable by you (here): 272\n• [Get Async](https://discord.com/oauth2/authorize?client_id=1227127704760090716&permissions=8&scope=bot) | [Support server](https://discord.gg/SFm9B4ZyNW) | [Vote me](https://discord.gg/SFm9B4ZyNW)\n• Type `$help <command | module>` for more info.\n```py\n<> - Required | [] - Optional```", 
             color=discord.Color.green()
        )
        embed.set_author(
            name=f"{member}",
            icon_url=member.avatar.url if member.avatar else member.default_avatar.url
        )
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.add_field(name="**__Main__**", value="<:Async_automod:1239445147276673026>  `:` AntiNuke\n<:Async_customrole:1239446889741680704>  `:` Selfroles\n<:Async_ticket:1239447463409225770> `:` Tickets\n<:Async_giveway:1243099265132138565>  `:` Giveaways\n<:Async_antinuke:1243099690422239262>  `:` Automod\n<:Async_welcome:1243100089858134017>  `:` Welcomer")
        embed.add_field(name="**__Extra__**", value="<:Async_logs:1239445659103268877>  `:` Logging\n<:Async_mod:1243100467362267216>  `:` Media\n<:Async_automod:1239445147276673026> `:` Moderation\n<:Async_games:1243101018024054845> `:` Games\n<:Async_utility:1227986493335797901>  `:` Utility\n <:Async_music:1243495167005294593> `:`Music")
        embed.set_footer(text="Made with 💖 by Async Development.", icon_url="https://media.discordapp.net/attachments/1189150446951071834/1243098613253537813/image.png?ex=66503d4d&is=664eebcd&hm=3624b9c798d66ad013f570bd8cb06de271feffbb0cb9f4e33fda9ac45a4076ad&=&format=webp&quality=lossless&width=537&height=525")
        message = await ctx.send(embed=embed, view=GhostyView(ctx))

async def setup(bot):
    await bot.add_cog(Help(bot))