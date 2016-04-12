class Player:
	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last
		self.stats = [0] * 18

	def getName(self):
		name = self.firstname + " " + self.lastname
		return name

class Quarterback(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)
		self.categories = ['G',	'GS', 'Comp', 'PAtt', 'PPct',	'PYds',
				   'PAvg', 'PTD', 'Int', 'Sck', 'SckY', 'Rate', 
				   'RAtt', 'RYds', 'RAvg', 'RTD', 'FUM', 'Lost']

class RunningBack(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)
		self.categories = ['G', 'RAtt', 'RYds',	'RAvg',
				   		   'RLng', 'RTD', 'Rec', 'RecYds', 'RecAvg', 'RecLng', 
				   		   'RecTD','FUM', 'Lost']


class FullBack(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class WideReceiver(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)
		self.categories = ['G', 'GS', 'Rec', 'RecYds', 'RecAvg', 'RecLng', 
				   'RecTD', 'RAtt', 'RYds', 'RAvg', 
				   'RLng', 'RTD', 'FUM', 'Lost']

class TightEnd(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)
		self.categories = ['G', 'GS', 'Rec', 'RecYds', 'RecAvg', 'RecLng', 
						   'RecTD', 'RAtt', 'RYds', 'RAvg', 
						   'RLng', 'RTD', 'FUM', 'Lost']

class TightEnd(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class OffensiveTackle(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class Guard(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class Center(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class DefensiveTackle(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class DefensiveEnd(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class MiddleLineBacker(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class OutsideLineBacker(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class CornerBack(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class FreeSafety(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class StrongSafety(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class Kicker(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)

class Punter(Player):
	def __init__(self, first, last):
		Player.def__init__(first, last)
