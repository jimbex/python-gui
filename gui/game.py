import pygame
pygame.init()

Jump = False
jumpcount = 10

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 220
y = 220
width = 40
height = 60
vel = 20


run = True

while  run:
	pygame.time.delay(100)

	for  event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		pass

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 0:
		x -= vel

	if keys[pygame.K_RIGHT] and x < 450:
		x += vel
	if not Jump:
		if keys[pygame.K_UP] and y > 0:
			y -= vel

		if keys[pygame.K_DOWN] and y < 440:
			y += vel
		
		if keys[pygame.K_SPACE]:
			Jump = True

	else:
		if jumpcount >= -10:
			neg = 1

			if jumpcount < 0:
				neg = -1

			y -= (jumpcount ** 2) * neg * 0.5
			jumpcount -= 1

		else:
			Jump = False
			jumpcount = 10
		







	win.fill((0, 0, 0))

	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()
	

pygame.quit()