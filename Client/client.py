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
				if pygame.Rect(0, 635, 150, 25).collidepoint(position):
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
					continue
				if len(text) == 50:
					continue
				text+= event.unicode
		pygame.display.update()
def UrlPage(txt):
	pass
main()
