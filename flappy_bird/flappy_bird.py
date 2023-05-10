import pygame, sys, random


def draw_floor():
	screen.blit(floor_surface,(floor_x_pos,700))
	screen.blit(floor_surface,(floor_x_pos+576,700))

def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos-250))
	return bottom_pipe,top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 700:
			screen.blit(pipe_surface, pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe, pipe)

def check_collisions(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			return False

	if bird_rect.top <= -100 or bird_rect.bottom >= 700:
		return False

	return True	

def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird,-bird_movement * 3,1)
	return new_bird

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
pygame.display.set_caption('FlappyBird')

#Game variables
gravity = 0.25
bird_movement = 0
game_activity = True


bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,312))

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [200,300,400,500,600]


while True:
	#image of player 1
	#background image
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_activity:
				bird_movement = 0
				bird_movement -= 6

			if event.key == pygame.K_SPACE and game_activity == False:
				game_activity = True
				pipe_list.clear()
				bird_rect.center = (100,312)
				bird_movement = 0

		if event.type == SPAWNPIPE:
			pipe_list.extend(create_pipe())
			#print(pipe_list)

	screen.blit(bg_surface,(0,0))

	if game_activity:

		#bird
		bird_movement += gravity
		rotated_bird = rotate_bird(bird_surface)
		bird_rect.centery += bird_movement
		screen.blit(rotated_bird, bird_rect)
		game_activity = check_collisions(pipe_list)

		#pipes
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)



	#floor
	floor_x_pos -= 1
	draw_floor()
	if floor_x_pos <= -576:
		floor_x_pos = 0
	screen.blit(floor_surface,(floor_x_pos,700))


	pygame.display.update()
	clock.tick(120)