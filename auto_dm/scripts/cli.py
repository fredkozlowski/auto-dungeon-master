# This should be the class for reading in a csv of random npc names
# and creating a npc object

import click


@click.command()
@click.option('--create', default = False, help='Manually create an NPC')
def hello(create):
	if(create):
		click.echo('Generating an NPC')
	else:
		click.echo('Creating an NPC')