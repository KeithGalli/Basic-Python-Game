import pygame
from player import HumanPlayer
from game import Screen, Game

def main():
	pygame.init()
	
	screen = Screen(height=1000)
	player = HumanPlayer(screen.width/2, screen.height-2*HumanPlayer.size)
	game = Game()
	
	game_over = False
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.x -= player.size
				elif event.key == pygame.K_RIGHT:
					player.x += player.size

		game.drop_enemies(screen.width)
		game.update_enemy_positions(screen.height)
		game.set_level()

		screen.update_screen(game.enemy_list, player, game.score)

		if game.collision_check(player):
			game_over = True
			break


if __name__ == '__main__':
	main()