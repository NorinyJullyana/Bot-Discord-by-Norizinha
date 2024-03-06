import discord
from discord.ext import commands
from discord import app_commands

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

# Configuração do bot
bot = commands.Bot(command_prefix="!", intents=permissoes)


# Evento de on_ready
@bot.event
async def on_ready():
  await bot.tree.sync()
  print(f"Bot conectado como {bot.user}")


#sincronizar comandos
@bot.command()
async def sincronizar(ctx: commands.Context):
  if ctx.author.id == #id do author:
    server = discord.Object(id= #id do servidor)
    sincs = await bot.tree.sync(guild=server)
    await ctx.reply(f"{len(sincs)}) comandos sincronizados")
  else:
    await ctx.reply('Apenas a Norizinha pode usar esse comando!!!',
                    ephemeral=True)


# Olá ^^
@bot.tree.command(description='Responde o usuário com Olá ^^')
async def ola(interact: discord.Interaction):
  await interact.response.send_message(f"Olá, {interact.user.display_name} ^^")


# bem vindo
@bot.event
async def on_member_join(membro: discord.Member):
  canal = bot.get_channel(#id do canal)

  if canal:
    msg = discord.Embed(title=f'{membro.display_name} Entrou no servidor ^^')
    msg.description = "Seja bem vindo!!!"
    msg.color = discord.Color.pink()
    msg.set_image(
        url=
        'https://i.pinimg.com/originals/ef/cb/fd/efcbfd46599132b10cfaea251cf00984.gif'
    )
    await canal.send(embed=msg)
  else:
    print(
        "Canal não encontrado. Verifique o ID do canal ou as permissões do bot."
    )


# Adeus
@bot.event
async def on_member_remove(membro: discord.Member):
  canal = bot.get_channel(#id do canal)

  if canal:
    msg = discord.Embed(title=f'{membro.display_name} Saiu do servidor...')
    msg.description = "Adeus meu chapa :c"
    msg.color = discord.Color.pink()
    msg.set_image(
        url='https://media.tenor.com/w5EFZpYKe8MAAAAC/anime-anime-funny.gif')
    await canal.send(embed=msg)
  else:
    print(
        "Canal não encontrado. Verifique o ID do canal ou as permissões do bot."
    )


#adeus comando
@bot.command()
async def adeus(interact: discord.Interaction):
  canal = bot.get_channel(#id do canal)

  if canal:
    msg = discord.Embed(
        title=f'{interact.author.display_name} Saiu do servidor...')
    msg.description = "Adeus meu chapa :c"
    msg.color = discord.Color.pink()
    msg.set_image(
        url='https://media.tenor.com/w5EFZpYKe8MAAAAC/anime-anime-funny.gif')

    await canal.send(embed=msg)
  else:
    print(
        "Canal não encontrado. Verifique o ID do canal ou as permissões do bot."
    )


cargos = {
    "Engenharia de Software": #id do cargo,
    "Análise e Desenvolvimento de Sistemas":  #id do cargo
}


@bot.command()
async def cargo(ctx: commands.Context):
  if ctx.author.id == #id do author:

    async def select_resposta(interact: discord.Interaction):
      escolha = interact.data['values'][0]
      curso_escolhido = cargos[escolha]
      membro = await ctx.guild.fetch_member(interact.user.id)
      role = ctx.guild.get_role(curso_escolhido)

      if role:
        await membro.add_roles(role)
        await interact.response.send_message(
            f"Você escolheu o curso {escolha}", ephemeral=True)
      else:
        await interact.response.send_message(
            "Desculpe, ocorreu um erro. Por favor, tente novamente.",
            ephemeral=True)

    menuCursos = discord.ui.Select(placeholder='Selecione seu curso!!!')
    opcoes = [
        discord.SelectOption(label='Engenharia de Software',
                             value='Engenharia de Software'),
        discord.SelectOption(label='Análise e Desenvolvimento de Sistemas',
                             value='Análise e Desenvolvimento de Sistemas')
    ]

    menuCursos.options = opcoes
    menuCursos.callback = select_resposta
    view = discord.ui.View()
    view.add_item(menuCursos)
    await ctx.send('Escolha seu curso:', view=view)
  else:
    await ctx.reply('Apenas a Norizinha pode usar esse comando!!!',
                    ephemeral=True)


bot.run(
    "#token do seu bot")
