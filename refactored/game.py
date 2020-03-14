from color import Color
from player import BasePlayer, Enemy
import random
import pygame

class Screen:
	def __init__(self, width=800, height=600, background_color=Color.BLACK, font_type="monospace", font_size=35, clock_tick=30):
		self.width = width
		self.height = height
		self.background_color = background_color
		self.screen = pygame.display.set_mode((width, height))
		self.font = pygame.font.SysFont(font_type, font_size)
		self.clock = pygame.time.Clock()
		self.clock_tick = clock_tick

	def refresh_background(self):
		self.screen.fill(self.background_color)

	def draw_score_label(self, score, color=Color.YELLOW):
		text = f"Score: {score}"
		label = self.font.render(text, 1, color)
		self.screen.blit(label, (self.width-200, self.height-40))

	def draw_enemies(self, enemy_list):
		for enemy in enemy_list:
			enemy.draw(self.screen)

	def draw_player(self, player):
		player.draw(self.screen)

	def update_screen(self, enemy_list, player, score):
		self.refresh_background()
		self.draw_enemies(enemy_list)
		self.draw_player(player)
		self.draw_score_label(score)

		self.clock.tick(self.clock_tick)
		pygame.display.update()

class Game:
	def __init__(self, speed=10, score=0, max_enemies=10, delay=0.1):
		self.speed = speed
		self.score = score
		self.max_enemies = max_enemies
		self.delay = delay

		self.enemy_list = []

	def set_level(self):
		if self.score < 20:
			self.speed = 5
		elif self.score < 40:
			self.speed = 8
		elif self.score < 60:
			self.speed = 12
		else:
			self.speed = 15

	def drop_enemies(self, screen_width):
		delay = random.random()
		if len(self.enemy_list) < self.max_enemies and delay < self.delay:
			random_x = random.randint(0, screen_width-Enemy.size)
			new_enemy = Enemy(random_x, 0)
			self.enemy_list.append(new_enemy)

	def update_enemy_positions(self, screen_height):
		updated_enemy_list = []
		for enemy in self.enemy_list:
			if enemy.y >= 0 and enemy.y < screen_height:
				enemy.y += self.speed
				updated_enemy_list.append(enemy)
			else: # Enemy is no longer on screen, increase score
				self.score += 1
		self.enemy_list = updated_enemy_list

	def collision_check(self, player):
		for enemy in self.enemy_list:
			if enemy.detect_collision(player):
				return True
		return False