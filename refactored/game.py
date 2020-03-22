import random
from player import Enemy, LargeEnemy, KeithEnemy

class Game:
	Enemy = Enemy
	def __init__(self, speed=10, score=0, max_enemies=10, delay=0.1):
		self.speed = speed
		self.score = score
		self.max_enemies = max_enemies
		self.delay = delay

		self.enemy_list = []

	def drop_enemies(self, screen_width):
		delay = random.random()
		if len(self.enemy_list) < self.max_enemies and delay < self.delay:
			random_x = random.randint(0, screen_width)
			y_pos = 0
			enemy = self.Enemy(random_x, y_pos)
			self.enemy_list.append(enemy)

	def update_enemy_positions(self, screen_height):
		new_enemy_list = []
		for enemy in self.enemy_list:
			if enemy.y >= 0 and enemy.y < screen_height:
				enemy.y += self.speed
				new_enemy_list.append(enemy)
			else:
				self.score += 1
		self.enemy_list = new_enemy_list

	def set_level(self):
		if self.score < 20:
			self.speed = 5
		elif self.score < 40:
			self.speed = 8
		elif self.score < 60:
			self.speed = 12
		else:
			self.speed = 15

	def collision_check(self, player):
		for enemy in self.enemy_list:
			if enemy.detect_collision(player):
				return True
		return False

class HardGame(Game):
	Enemy = LargeEnemy

	def set_level(self):
		self.speed = self.score/5 + 1

class BossGame(Game):
	Enemy = KeithEnemy

