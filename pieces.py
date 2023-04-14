import pygame

class Rook():
    def __init__(self,screen, color):
        self.rook = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Rook.png").convert_alpha(),(60,60))
        self.screen = screen
        self.posX = self.posY = None
    
    def default_pos(self,name):
        ''' Func to move the piece by your name in the board'''
        num_of_piece = int((name[-1]))
        self.posY = 725
        if num_of_piece == 0:
            self.posX = 20
            self.screen.blit(self.rook,(self.posX,self.posY))
        elif num_of_piece == 1:
            self.posX = 720
            self.screen.blit(self.rook,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
        self.screen.blit(self.rook,(self.posX,self.posY))


class Bishop():
    def __init__(self,screen, color):
        self.bishop = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Bishop.png").convert_alpha(),(60,60))
        self.screen = screen
        self.posX = self.posY = None
    
    def default_pos(self,name):
        ''' Func to move the piece by your name in the board'''
        num_of_piece = int((name[-1]))
        self.posY = 725
        if num_of_piece == 0:
            self.posX = 220
            self.screen.blit(self.bishop,(self.posX,self.posY))
        elif num_of_piece == 1:
            self.posX = 520
            self.screen.blit(self.bishop,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
        self.screen.blit(self.bishop,(self.posX,self.posY))

class King():
    def __init__(self,screen, color):
        self.king = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/King.png").convert_alpha(),(60,60))
        self.screen = screen
        self.posX = self.posY = None
    
    def default_pos(self,_onlyOne):
        ''' Func to move the piece by your name in the board'''
        self.posX,self.posY = (420,725)
        self.screen.blit(self.king,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
        self.screen.blit(self.king,(self.posX,self.posY))

class Queen():
    def __init__(self,screen, color):
        self.queen = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Queen.png").convert_alpha(),(60,60))
        self.screen = screen
        self.posX = self.posY = None
    
    def default_pos(self,_onlyOne):
        ''' Func to move the piece by your name in the board'''
        self.posX,self.posY = (325,725)
        self.screen.blit(self.queen,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
        self.screen.blit(self.queen,(self.posX,self.posY))

class Pawn():
    def __init__(self,screen, color):
        self.pawn = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Pawn.png").convert_alpha(),(60,60))
        self.screen = screen
        self.posX = self.posY = None
    
    def default_pos(self,name):
        ''' Func to move the piece by your name in the board'''
        num_of_piece = int(name[-1])
        self.posY = 625
        if num_of_piece == 0:
            self.posX = 20
            self.screen.blit(self.pawn,(self.posX,self.posY))
        elif num_of_piece == 1:
            self.posX = 120
            self.screen.blit(self.pawn,(self.posX,self.posY))
        elif num_of_piece == 2:
            self.posX = 220
            self.screen.blit(self.pawn,(self.posX,self.posY))
        elif num_of_piece == 3:
            self.posX = 320
            self.screen.blit(self.pawn,(self.posX,self.posY))
        elif num_of_piece == 4:
            self.posX = 420
            self.screen.blit(self.pawn,(self.posX,self.posY))
        elif num_of_piece == 5:
            self.posX = 520
            self.screen.blit(self.pawn,(self.posX,self.posY))
        elif num_of_piece == 6:
            self.posX = 620
            self.screen.blit(self.pawn,(self.posX,self.posY))
        elif num_of_piece == 7:
            self.posX = 720
            self.screen.blit(self.pawn,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
        self.screen.blit(self.pawn,(self.posX,self.posY))

class Knigth():
    def __init__(self,screen, color):
        self.knigth = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Knigth.png").convert_alpha(),(60,60))
        self.screen = screen
        self.posX = self.posY = None
    
    def default_pos(self,name):
        ''' Func to move the piece by your name in the board'''
        num_of_piece= int(name[-1])
        self.posY = 725
        if num_of_piece == 0:
            self.posX = 120
            self.screen.blit(self.knigth,(self.posX,self.posY))
        elif num_of_piece == 1:
            self.posX = 620
            self.screen.blit(self.knigth,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
        self.screen.blit(self.knigth,(self.posX,self.posY))
