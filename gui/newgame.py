# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load()
    #pygame.display.set_icon(logo)

    x = 200
    y = 200
    vel = 20
    pygame.display.set_caption("minimal program")

    image = pygame.image.load('premium-pulldown-img.png')
    image2 = pygame.image.load('play-curiosity-inner-child-card.png')

     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500,500))

    
    screen.blit(image2, (0, 0))
    
    
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
        	keys = pygame.key.get_pressed()

        	if keys[pygame.K_LEFT] and x > 0:
        		x -= vel
        	if keys[pygame.K_RIGHT]:
        		x += vel
        	if keys[pygame.K_UP]:
        		y -= vel
        	if keys[pygame.K_DOWN]:
        		y += vel
            # only do something if the event is of type QUIT
        	if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
        		running = False
        screen.blit(image2, (0, 0))
        screen.blit(image, (x, y))

        pygame.display.flip()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
