import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600,600))

def main():
    pygame.init()

    #Fenster
    pygame.display.set_caption("Cookie Clicker")

    #Cookie
    cookie = pygame.image.load("Cookie.jpg")
    cookie = pygame.transform.scale(cookie, (100,100))
    screen.blit(cookie, (300, 300))
    
    Cookies = 0
    #Button
    quit = button(screen, (200, 200), "Quit")
    anzeige = button(screen, (0, 0), ("Cookies " + str(Cookies)))
    click = button(screen, (500,0), "Click")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit.collidepoint(pygame.mouse.get_pos()):
                    running = False
                elif click.collidepoint(pygame.mouse.get_pos()):
                    Cookies += 1
                    anzeige = button(screen, (0, 0), ("Cookies " + str(Cookies)))
        pygame.display.update()

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))
    
main()
