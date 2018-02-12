from .character import character
class npc(character):
	def __init__(name, race, phys_feature, archetype, location):
		Character.__init__(name, race)
		this.phys_feature = phys_feature
		this.archetype = archetype
		this.location = location