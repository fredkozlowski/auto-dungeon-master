import click
from ..classes import character


@click.group()
def pc():
    """Manages heroes"""

@pc.command()
@click.option('--manual', default = False, help='Manually create an NPC')
def create(manual):
	"""Creates a new heroes"""
	click.echo('Creating a hero')
	npc_type = click.prompt('NPC type ', type=bool)
	name = click.prompt('Name ', type=str)
	race = click.prompt('Race ', type=str)
	test = NPC(name, race)
	print(test)
		
@pc.command()
def generate():
	"""Randomly generates a new hero"""
	click.echo('Generating a hero')