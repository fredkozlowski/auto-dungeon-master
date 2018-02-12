import click
from .commands import charactergen


@click.group()
def cli():
    """auto_dungeon_master

    Lorem Ipsum
    """
    
cli.add_command(charactergen.npcgroup)
cli.add_command(charactergen.pc)