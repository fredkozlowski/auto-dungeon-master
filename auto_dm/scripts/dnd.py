import click
from .commands import npcgen
from .commands import pcgen


@click.group()
def cli():
    """auto_dungeon_master

    Lorem Ipsum
    """
    
cli.add_command(npcgen.npc)
cli.add_command(pcgen.pc)