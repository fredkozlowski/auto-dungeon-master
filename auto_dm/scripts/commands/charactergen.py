import click
from ..classes import character, npc


@click.group()
def npcgroup():
    """Manages NPCs"""

@npcgroup.command()
@click.option('--sblock', is_flag = True, help='Give the NPC a stat block')
def create(sblock):
	"""Creates a new NPC"""
	click.echo('Creating an NPC')
	name = click.prompt('Name ', type=str)
	race = click.prompt('Race ', type=str)
	phys_feature = click.prompt('Physical feature ', type=str)
	archetype = click.prompt('Archetype ', type=str)
	location = click.prompt('Location ', type=str)
	if(sblock):
		statblock = click.prompt('Stat block ', type=str)
		temp_npc = npc(name, race, phys_feature, archetype, location, statblock)
	else:
		temp_npc = npc(name, race, phys_feature, archetype, location)
	click.echo(temp_npc.__str__)
		
@npcgroup.command()
def generate():
	"""Randomly generates a new NPC"""
	click.echo('Generating an NPC')
	
	
@click.group()
def pc():
    """Manages heroes"""

@pc.command()
@click.option('--manual', default = False, help='Manually create a player character')
def create(manual):
	"""Creates a new player character"""
	click.echo('Creating a hero')
	npc_type = click.prompt('NPC type ', type=bool)
	name = click.prompt('Name ', type=str)
	race = click.prompt('Race ', type=str)
	temp_pc = npc(name, race)
	print(temp_pc)
		
@pc.command()
def generate():
	"""Randomly generates a new hero"""
	click.echo('Generating a hero')