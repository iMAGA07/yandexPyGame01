# import pygame module in this program 
import pygame 

def main():
    # activate the pygame library 
    # initiate pygame and give permission 
    # to use pygame's functionality. 
    pygame.init() 

    # define the RGB value for white, 
    # green, blue colour . 
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    red = (255, 0, 0)
    black = (0, 0, 0)

    # assigning values to X and Y variable 
    X = 600
    Y = 400

    # create the display surface object 
    # of specific dimension..e(X, Y). 
    display_surface = pygame.display.set_mode((X, Y)) 

    # set the pygame window name 
    pygame.display.set_caption('GAME') 

    # create a font object. 
    # 1st parameter is the font file 
    # which is present in pygame. 
    # 2nd parameter is size of the font 
    font = pygame.font.Font('freesansbold.ttf', 32) 
    font1 = pygame.font.Font('freesansbold.ttf', 20) 

    # create a text suface object, 
    # on which text is drawn on it. 
    text = font.render('Game from r1chter1 and iMAGA', True, green, blue) 
    text2 = font1.render("Quiz",True,black)
    text3 = font1.render("Games",True,black)

    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect() 

    # set the center of the rectangular object. 
    textRect.center = (X // 2, 100) 

    button = pygame.Rect(100, 300, 110, 40)
    button2 = pygame.Rect(375, 300, 110, 40)

    # infinite loop 
    while True : 

        # completely fill the surface object 
        # with white color 
        display_surface.fill(white) 

        # copying the text surface object 
        # to the display surface object 
        # at the center coordinate. 

        pygame.draw.rect(display_surface, [255, 0, 0], button)
        pygame.draw.rect(display_surface, [255, 0, 0], button2)
        display_surface.blit(text, textRect)
        display_surface.blit(text2,(125,310))
        display_surface.blit(text3,(390,310))

        # iterate over the list of Event objects 
        # that was returned by pygame.event.get() method. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    pass
                if button2.collidepoint(mouse_pos):
                    pass


        pygame.display.update()
    
    pygame.quit()
    sys.exit

if __name__ == '__main__':
    main()