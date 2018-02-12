import click
class character:
	def __init__(self, name, race):
		self.name = name
		self.race = race


class npc(character):
	def __init__(self, name, race, phys_feature, archetype, location, statblock):
		#character.__init__(self, name, race)
		self.phys_feature = phys_feature
		self.archetype = archetype
		self.location = location
		self.statblock = statblock