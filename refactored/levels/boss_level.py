import sys
sys.path.insert(0, '../')
import pygame
from player import HumanPlayer
from screen import Screen
from game import Game, HardGame, BossGame
from main import play_game

if __name__ == "__main__":
	pygame.init()

	screen = Screen(width=1000, height=1400)
	player = HumanPlayer(screen.width/2, screen.height-100)
	game = BossGame()

	play_game(screen, player, game)