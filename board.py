# import the pygame module, so you can use it
import pygame


class Board():
    def __init__(self,board_heigth,board_weigth,screen):
        self.board = pygame.transform.scale(pygame.image.load("images/board/chess board.jpg").convert_alpha(),(board_heigth,board_weigth))
        screen.fill("white")
        screen.blit(self.board, (0,0))
        self.my_piece = {}
        self.enemy_piece = {}

    def add_pieces(self,type_color,screen,pieces):
        # King,Queen,Bishop,Knigth,Rook,Pawn
        self.my_piece["king0"] = pieces[0](screen,type_color)
        self.my_piece["queen0"] = pieces[1](screen,type_color)
        for number_of_piece in ["0","1"]:
            self.my_piece["bishop"+number_of_piece] = pieces[2](screen,type_color)
            self.my_piece["knigth"+number_of_piece] = pieces[3](screen,type_color)
            self.my_piece["rook"+number_of_piece] = pieces[4](screen,type_color)
            
        for index in range(8):
            self.my_piece["pawn"+str(index)] = pieces[5](screen,type_color)
        # To set all of pieces in your default place.
        [piece_obj.default_pos(piece_name) for piece_name,piece_obj in self.my_piece.items()]
        self.add_enemy_pieces(type_color,screen,pieces)
    
    def add_enemy_pieces(self,type_color,screen,pieces):
        type_color = "white" if type_color != "white" else "black"
        self.enemy_piece["king0"] = pieces[0](screen,type_color)
        self.enemy_piece["queen0"] = pieces[1](screen,type_color)
        for number_of_piece in ["0","1"]:
            self.enemy_piece["bishop"+number_of_piece] = pieces[2](screen,type_color)
            self.enemy_piece["knigth"+number_of_piece] = pieces[3](screen,type_color)
            self.enemy_piece["rook"+number_of_piece] = pieces[4](screen,type_color)
        for index in range(8):
            self.enemy_piece["pawn"+str(index)] = pieces[5](screen,type_color)
        [obj.default_pos(n,120) if "pawn" in n else obj.default_pos(n,20) for n,obj in self.enemy_piece.items()]