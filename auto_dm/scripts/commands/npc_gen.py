import click
import npc


@click.command()
@click.option('--manual', default = False, help='Manually create an NPC')
def create(manual):
	if(manual):
		click.echo('Generating an NPC')
	else:
		click.echo('Creating an NPC')
		npc_type = click.prompt('NPC type ', type=bool)
		name = click.prompt('Name ', type=str)
		race = click.prompt('Race ', type=str)
		test = NPC(name, race)
		print test