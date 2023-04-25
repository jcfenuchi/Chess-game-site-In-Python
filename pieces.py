import pygame

class Rook():
    def __init__(self,screen, color):
        self.rook = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Rook.png"),(60,60))
        self.color = color
        self.screen = screen
        self.posX = self.posY = None
        self.rect = None
        self.clicked = False
        self.move = False
    
    def default_pos(self,name,y=750):
        ''' Func to move the piece by your name in the board'''
        num_of_piece = int((name[-1]))
        self.posY = y
        if num_of_piece == 0:
            self.posX = 50   
        elif num_of_piece == 1:
            self.posX = 750
        self.screen.blit(self.rook,(self.posX,self.posY))

    def update(self, event_list):
        self.rect = self.rook.get_rect(center = (self.posX, self.posY))        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.move = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.move = False
            elif event.type == pygame.MOUSEMOTION and self.move:
                self.set_pos(*pygame.mouse.get_pos())
        pygame.draw.rect(self.screen, (255, 0, 0), self.rook.get_rect(center = (self.posX, self.posY)), 1)
                    
    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
        print(self.posX,self.posY,"-----------")

    def blit(self):
        self.screen.blit(self.rook,self.rook.get_rect(center = (self.posX, self.posY)))
        
class Bishop():
    def __init__(self,screen, color):
        self.bishop = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Bishop.png").convert_alpha(),(60,60))
        self.screen = screen
        self.color = color
        self.posX = self.posY = None
        self.rect = None
        self.clicked = False
        self.move = False
    
    def default_pos(self,name,y=750):
        ''' Func to move the piece by your name in the board'''
        num_of_piece = int((name[-1]))
        self.posY = y
        if num_of_piece == 0:
            self.posX = 250
        elif num_of_piece == 1:
            self.posX = 550
        self.screen.blit(self.bishop,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
    
    def blit(self):
        self.screen.blit(self.bishop,self.bishop.get_rect(center = (self.posX, self.posY)))

    def update(self, event_list):
        self.rect = self.bishop.get_rect(center = (self.posX, self.posY))        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.move = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.move = False
            elif event.type == pygame.MOUSEMOTION and self.move:
                self.set_pos(*pygame.mouse.get_pos())
        pygame.draw.rect(self.screen, (255, 0, 0), self.bishop.get_rect(center = (self.posX, self.posY)), 1)


class King():
    def __init__(self,screen, color):
        self.king = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/King.png").convert_alpha(),(60,60))
        self.screen = screen
        self.color = color
        self.posX = self.posY = None
        self.rect = None
        self.clicked = False
        self.move = False
    
    def default_pos(self,_onlyOne,y=750):
        ''' Func to move the piece by your name in the board'''
        self.posX,self.posY = (450,y)
        self.screen.blit(self.king,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
    
    def blit(self):
        self.screen.blit(self.king,self.king.get_rect(center = (self.posX, self.posY)))

    def update(self, event_list):
        self.rect = self.king.get_rect(center = (self.posX, self.posY))        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.move = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.move = False
            elif event.type == pygame.MOUSEMOTION and self.move:
                self.set_pos(*pygame.mouse.get_pos())
        pygame.draw.rect(self.screen, (255, 0, 0), self.king.get_rect(center = (self.posX, self.posY)), 1)


class Queen():
    def __init__(self,screen, color):
        self.queen = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Queen.png").convert_alpha(),(60,60))
        self.screen = screen
        self.color = color
        self.posX = self.posY = None
        self.rect = None
        self.clicked = False
        self.move = False

    def default_pos(self,_onlyOne,y=750):
        ''' Func to move the piece by your name in the board'''
        self.posX,self.posY = (350,y)
        self.screen.blit(self.queen,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
    
    def blit(self):
        self.screen.blit(self.queen,self.queen.get_rect(center = (self.posX, self.posY)))

    def update(self, event_list):
        self.rect = self.queen.get_rect(center = (self.posX, self.posY))        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.move = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.move = False
            elif event.type == pygame.MOUSEMOTION and self.move:
                self.set_pos(*pygame.mouse.get_pos())
        pygame.draw.rect(self.screen, (255, 0, 0), self.queen.get_rect(center = (self.posX, self.posY)), 1)


class Pawn():
    def __init__(self,screen, color):
        self.pawn = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Pawn.png").convert_alpha(),(60,60))
        self.screen = screen
        self.color = color
        self.posX = self.posY = None
        self.rect = None
        self.clicked = False
        self.move = False
    
    def default_pos(self,name,y=650):
        ''' Func to move the piece by your name in the board'''
        self.posY = y
        num_of_piece = int(name[-1])
        for index in range(8):
            if num_of_piece == index:
                self.posX = (100*index + 50)
        self.screen.blit(self.pawn,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
    
    def blit(self):
        self.screen.blit(self.pawn, self.pawn.get_rect(center = (self.posX, self.posY)))

    def update(self, event_list):
        self.rect = self.pawn.get_rect(center = (self.posX, self.posY))        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.move = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.move = False
            elif event.type == pygame.MOUSEMOTION and self.move:
                self.set_pos(*pygame.mouse.get_pos())
        pygame.draw.rect(self.screen, (255, 0, 0), self.pawn.get_rect(center = (self.posX, self.posY)), 1)


class Knigth():
    def __init__(self,screen, color):
        self.knigth = pygame.transform.scale(pygame.image.load(f"images/pieces/{color}/Knigth.png").convert_alpha(),(60,60))
        self.screen = screen
        self.color = color
        self.posX = self.posY = None
        self.rect = None
        self.clicked = False
        self.move = False
    
    def default_pos(self,name,y=750):
        ''' Func to move the piece by your name in the board'''
        num_of_piece= int(name[-1])
        self.posY = y
        if num_of_piece == 0:
            self.posX = 150
        elif num_of_piece == 1:
            self.posX = 650
        self.screen.blit(self.knigth,(self.posX,self.posY))

    def set_pos(self,posX,posY):
        ''' Move the piece to X Y'''
        self.posX,self.posY = (posX,posY)
    
    def blit(self):
        self.screen.blit(self.knigth,self.knigth.get_rect(center = (self.posX, self.posY)))

    def update(self, event_list):
        self.rect = self.knigth.get_rect(center = (self.posX, self.posY))        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.move = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.move = False
            elif event.type == pygame.MOUSEMOTION and self.move:
                self.set_pos(*pygame.mouse.get_pos())
        pygame.draw.rect(self.screen, (255, 0, 0), self.knigth.get_rect(center = (self.posX, self.posY)), 1)