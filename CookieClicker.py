import pygame

def main():
    pygame.init()

    #Fenster
    pygame.display.set_caption("Cookie Clicker")
    screen = pygame.display.set_mode((600,600))

    #Cookie
    cookie = pygame.image.load("Cookie.jpg")
    cookie = pygame.transform.scale(cookie, (100,100))
    screen.blit(cookie, (50,50))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
if __name__=="__main__":
    main()
