###########################################################################
###########################################################################
##########                         _      _____  ##########################
##########   ___  __ _ _ __ ___   /_\     \_   \ ##########################
##########  / __|/ _` | '_ ` _ \ //_\\     / /\/ ##########################
##########  \__ \ (_| | | | | | /  _  \_/\/ /__  ##########################
##########  |___/\__,_|_| |_| |_\_/ \_(_)____(_) ##########################
#########################################################2021##############
###########################################################################
import discord, ffmpeg
from discord.ext import commands
from youtube_dl import YoutubeDL
##############################################################################################
class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.music_queue = [ ]
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
        self.vc = ""
##############################################################################################
    def search_yt(self, item): #should maybe use async...
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False
        return {'source': info['formats'][0]['url'], 'title': info['title']}
##############################################################################################
    def play_next(self): #should probably also use async...
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False
##############################################################################################
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']
            if self.vc == "" or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()
            else:
                self.vc = await self.bot.move_to(self.music_queue[0][1])
            print(self.music_queue)
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False
##############################################################################################
#####################
### USER COMMANDS ###
#####################
##############################################################################################
    @commands.command()
    async def play(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("You aren't in a voice channel, do that first.")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Couldn't find a viable match. Try again.")
            else:
                await ctx.send("Song added to queue.")
                self.music_queue.append([song, voice_channel])
                if self.is_playing == False:
                    await self.play_music()
##############################################################################################
    @commands.command()
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"
        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("The queue is empty.")
##############################################################################################
    @commands.command()
    async def skip(self, ctx):
        if self.vc != "":
            self.vc.pause() #WAS self.vc.stop(), but it was clearing the queue...
            await self.play_next() #WAS play_music
##############################################################################################
    @commands.command()
    async def dc(self, ctx):
        await self.vc.disconnect()
##############################################################################################
    @commands.command()
    async def pause(self, ctx):
        await self.vc.pause()
##############################################################################################
    @commands.command()
    async def resume(self, ctx):
        await self.vc.resume()
##############################################################################################
    @commands.command()
    async def clear(self, ctx):
        await self.vc.stop()
##############################################################################################
##############################################################################################
