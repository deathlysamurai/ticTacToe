import pygame

#setup pygame and window
pygame.init()
WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Window")

#colors
WHITE = (255, 255, 255)

#setup clock
FPS = 60
clock = pygame.time.Clock()

#setup game loop
def main():
    
    run = True
    while run:
        clock.tick(FPS)
        draw_lines()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    
def draw_lines():
    pygame.draw.line(win, WHITE, (WIDTH/3, 0), (WIDTH/3, HEIGHT))
    pygame.draw.line(win, WHITE, (2*(WIDTH/3), 0), (2*(WIDTH/3), HEIGHT)) 
    pygame.draw.line(win, WHITE, (0, HEIGHT/3), (WIDTH, HEIGHT/3))
    pygame.draw.line(win, WHITE, (0, 2*(HEIGHT/3)), (WIDTH, 2*(HEIGHT/3)))
    pygame.display.update()
    

main()
pygame.quit()