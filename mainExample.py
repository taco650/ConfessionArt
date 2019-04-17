import pygame

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    logo = pygame.image.load("logo32x32.png")
    alivePic = pygame.image.load("alive1.jpg")
    deadPic = pygame.image.load("dead1.jpg")
    
    pygame.display.set_caption("minimal program")
    pygame.display.set_icon(alivePic)
    screen = pygame.display.set_mode((700,700))
    #pygame.NOFRAME

    running = True
    buttonStates = []
    for x in range(0,10):
        buttonStates.append(False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            pygame.display.set_icon(alivePic)
            pygame.time.wait(2000)
            pygame.display.set_icon(deadPic)
            pygame.time.wait(4000)
            running = False

if __name__ == "__main__":
    main()
