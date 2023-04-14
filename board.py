# import the pygame module, so you can use it
import pygame


class Board():
    def __init__(self,board_heigth,board_weigth,screen):
        self.board = pygame.transform.scale(pygame.image.load("images/board/chess board.jpg").convert_alpha(),(board_heigth,board_weigth))
        screen.fill("white")
        screen.blit(self.board, (0,0))
        self.all_piece = {}

    def add_pieces(self,type_color,screen,pieces):
        # King,Queen,Bishop,Knigth,Rook,Pawn
        self.all_piece["king0"] = pieces[0](screen,type_color)
        self.all_piece["queen0"] = pieces[1](screen,type_color)
        self.all_piece["bishop0"] = pieces[2](screen,type_color)
        self.all_piece["bishop1"] = pieces[2](screen,type_color)
        self.all_piece["knigth0"] = pieces[3](screen,type_color)
        self.all_piece["knigth1"] = pieces[3](screen,type_color)
        self.all_piece["rook0"] = pieces[4](screen,type_color)
        self.all_piece["rook1"] = pieces[4](screen,type_color)
        for index in range(8):
            self.all_piece["pawn"+str(index)] = pieces[5](screen,type_color)
        # To set all of pieces in your default place.
        [piece_obj.default_pos(piece_name) for piece_name,piece_obj in self.all_piece.items()]