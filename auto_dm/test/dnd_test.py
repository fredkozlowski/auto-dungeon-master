import click
from click.testing import CliRunner
from auto_dm.scripts.dnd import cli


def test_command_dnd():
	runner = CliRunner()
	result = runner.invoke(cli, ['npc', 'generate'])
	assert result.exit_code == 0
	assert result.output == 'Generating an NPC\n'