

class Config:

	def __init__(self):

		#GAME CONFIG
		self.title = "Battleship War"
		self.row = 5
		self.column = 5


		#WINDOW CONFIG
		base = 125
		ratio = 5
		self.side = base * ratio
		self.screen = f"{self.side}x{self.side}+500+500"

		
		self.init_img = "img/logo.png"
		self.final_img = "img/final.jpeg"
		self.win_img = "img/wrong.png"

		self.login_img = "img/init.png"

	