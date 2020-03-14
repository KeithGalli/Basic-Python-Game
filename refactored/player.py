from color import Color
import pygame

class BasePlayer:
	def __init__(self, x, y, size=50, color=Color.RED):
		self.x = x
		self.y = y
		self.size = size
		self.color = color

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

	def detect_collision(self, other):
		if (other.x >= self.x and other.x < (self.x + self.size)) or (self.x >= other.x and self.x < (other.x + other.size)):
			if (other.y >= self.y and other.y < (self.y + self.size)) or (self.y >= other.y and self.y < (other.y + other.size)):
				return True
		return False

class Enemy(BasePlayer):
	size = 50
	def __init__(self, x, y):
		super().__init__(x, y, size=self.size, color=Color.BLUE)

class HumanPlayer(BasePlayer):
	size = 75
	def __init__(self, x, y):
		super().__init__(x, y, size=self.size, color=Color.RED)