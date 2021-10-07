from TCPmodClient import *
import pygame
from pygame.locals import *
pygame.init()
canvas = pygame.display.set_mode((1360, 660))
pygame.display.set_caption("Galaxy Search")
SearchBar = pygame.image.load("SearchBar.png")
def main():
	basicFont = pygame.font.SysFont(None, 25)
	while True:
		displaying = basicFont.render("create", True, (0,0,0), (255,255,255))
		canvas.fill((255, 255, 255))
		canvas.blit(SearchBar, (0, 0))
		canvas.blit(displaying, (0, 635))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				if pygame.Rect(0, 635, 150, 25).colliedpoint(position):
					text = Create()
					handle_request(("10.0.0.147", 80), "SEARCH")
				if pygame.Rect(0, 0, 1360, 30).collidepoint(position):
					search = Search()
					if search == None:
						continue
					else:
						urls = handle_request(("10.0.0.147", 80), "SEARCH", search)
						url = UrlPage(urls)
						text = handle_request(("10.0.0.147", 80), "GET_TEXT", url)
						DisplayURL(text)
		pygame.display.update()
def Search():
	text = ""
	shifted = False
	basicFont = pygame.font.SysFont(None, 25)
	breakout = False
	while not breakout:
		canvas.fill((255, 255, 255))
		displaying = basicFont.render(text, True, (0,0,0), (255,255,255))
		canvas.blit(displaying, (10, 7))
		canvas.blit(SearchBar, (0, 0))
		for event in pygame.event.get():
			if event.type == QUIT:
				return None
			if event.type == MOUSEBUTTONDOWN:
				breakout = True
			if event.type == KEYUP:
				if event.key == K_RSHIFT or event.key == K_LSHIFT:
					shifted = False
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					return text
				if event.key == K_RSHIFT or event.key == K_LSHIFT:
					shifted = True
					continue
				if event.key == K_BACKSPACE:
					text = text[0:len(text)-1]
				if len(text) == 50:
					continue
				if event.key == K_SPACE:
					text += ' '
				if shifted == True:
					if event.key == K_a:
						text += 'A'
					if event.key == K_b:
						text += 'B'
					if event.key == K_c:
						text += 'C'
					if event.key == K_d:
						text += 'D'
					if event.key == K_e:
						text += 'E'
					if event.key == K_f:
						text += 'F'
					if event.key == K_g:
						text += 'G'
					if event.key == K_h:
						text += 'H'
					if event.key == K_i:
						text += 'I'
					if event.key == K_j:
						text += 'J'
					if event.key == K_k:
						text += 'K'
					if event.key == K_l:
						text += 'L'
					if event.key == K_m:
						text += 'M'
					if event.key == K_n:
						text += 'N'
					if event.key == K_o:
						text += 'O'
					if event.key == K_p:
						text += 'P'
					if event.key == K_q:
						text += 'Q'
					if event.key == K_r:
						text += 'R'
					if event.key == K_s:
						text += 'S'
					if event.key == K_t:
						text += 'T'
					if event.key == K_u:
						text += 'U'
					if event.key == K_v:
						text += 'V'
					if event.key == K_w:
						text += 'W'
					if event.key == K_x:
						text += 'X'
					if event.key == K_y:
						text += 'Y'
					if event.key == K_z:
						text += 'Z'
					if event.key == K_1:
						text += '!'
					if event.key == K_2:
						text += '@'
					if event.key == K_3:
						text += '#'
					if event.key == K_4:
						text += '$'
					if event.key == K_5:
						text += '%'
					if event.key == K_6:
						text += '^'
					if event.key == K_7:
						text += '&'
					if event.key == K_8:
						text += '*'
					if event.key == K_9:
						text += '('
					if event.key == K_0:
						text += ')'
				if shifted == False:
					if event.key == K_a:
						text += 'a'
					if event.key == K_b:
						text += 'b'
					if event.key == K_c:
						text += 'c'
					if event.key == K_d:
						text += 'd'
					if event.key == K_e:
						text += 'e'
					if event.key == K_f:
						text += 'f'
					if event.key == K_g:
						text += 'g'
					if event.key == K_h:
						text += 'h'
					if event.key == K_i:
						text += 'i'
					if event.key == K_j:
						text += 'j'
					if event.key == K_k:
						text += 'k'
					if event.key == K_l:
						text += 'l'
					if event.key == K_m:
						text += 'm'
					if event.key == K_n:
						text += 'n'
					if event.key == K_o:
						text += 'o'
					if event.key == K_p:
						text += 'p'
					if event.key == K_q:
						text += 'q'
					if event.key == K_r:
						text += 'r'
					if event.key == K_s:
						text += 's'
					if event.key == K_t:
						text += 't'
					if event.key == K_u:
						text += 'u'
					if event.key == K_v:
						text += 'v'
					if event.key == K_w:
						text += 'w'
					if event.key == K_x:
						text += 'x'
					if event.key == K_y:
						text += 'y'
					if event.key == K_z:
						text += 'z'
					if event.key == K_1:
						text += '1'
					if event.key == K_2:
						text += '2'
					if event.key == K_3:
						text += '3'
					if event.key == K_4:
						text += '4'
					if event.key == K_5:
						text += '5'
					if event.key == K_6:
						text += '6'
					if event.key == K_7:
						text += '7'
					if event.key == K_8:
						text += '8'
					if event.key == K_9:
						text += '9'
					if event.key == K_0:
						text += '0'
		pygame.display.update()
def UrlPage(txt):
	
main()
