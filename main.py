# import the pygame module, so you can use it
import pygame
from pieces import King,Queen,Bishop,Knigth,Rook,Pawn
from board import Board

 
# define a main function
def main():
    # create a surface on screen that has the size of 800 x 800
    heigth = 800
    weigth = 800
    screen = pygame.display.set_mode((heigth,weigth))
    clock = pygame.time.Clock()
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    icon = pygame.image.load("images/logo_chess.png")
    pygame.display.set_icon(icon)   
    
    #create a Board
    board = Board(heigth,weigth,screen=screen)
    # add pieces in the board
    board.add_pieces("black",screen,(King,Queen,Bishop,Knigth,Rook,Pawn))
    [print(n,o,f"the position is x={o.posX},y={o.posY} my_color={o.color}") for n,o in board.my_piece.items()]
    [print(n,o, f"the position is x={o.posX},y={o.posY} my_color={o.color}") for n,o in board.enemy_piece.items()]

    #create pieces

    #ver cordenadas PARA VER CORDENADAS DESCOMENTE ISSO
    #car = pygame.transform.scale(pygame.image.load("images/pieces/white/Pawn.png").convert_alpha(),(60,60))
    #pos_x_car = 630
    #pos_y_car = 600
    
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        #ver cordenadas PARA VER CORDENADAS DESCOMENTE ISSO
        #screen.blit(car,(pos_x_car,pos_y_car))
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_UP]:
        #    pos_y_car += 1
        #if keys[pygame.K_DOWN]:
        #    pos_y_car -= 1
        #if keys[pygame.K_LEFT]:
        #    pos_x_car += 1
        #if keys[pygame.K_RIGHT]:
        #    pos_x_car -= 1
        #print(pos_x_car,pos_y_car)
        
        
        # flip() the display to put your work on screen
        pygame.display.flip()
        

        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # limits FPS to 60
        dt = clock.tick(60) / 1000
    pygame.quit()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()