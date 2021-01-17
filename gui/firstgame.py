import pygame

pygame.init()

win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("First Game")

ax = 10
ay = 200
bx = 760
by = 200
cx = 400
cy = 250
width = 30
height = 100
vel = 1


running = True

while running:
	for event in pygame.event.get():
		if cy > 480:
			cx -= vel
			cy -= vel



		if event.type == pygame.QUIT:
			running = False
	cx += vel
	cy += vel


	win.fill((0, 0, 0))
	paddle_a = pygame.draw.rect(win, (0, 255, 0), (ax, ay, width, height))

	paddle_b = pygame.draw.rect(win, (0, 255, 0), (bx, by, width, height))

	ball = pygame.draw.circle(win, (0, 255, 0), (cx, cy), 10)

	pygame.display.update()

