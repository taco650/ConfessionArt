import pygame
import os
import sys

def main():
    #Game Constants
    TIME_FOR_DECSISION = 10


    #initialize modules
    pygame.init()

    font = pygame.font.Font("LOUDNOISESKEW.ttf", 200)
    
    #load eerie song and play it indefinately
    pygame.mixer.music.load('Shadowlands3-Machine by Kevin MacLeod.ogg')
    pygame.mixer.music.play(-1)
    
    #creat image variables
    logo = pygame.image.load("logo32x32.png")
    alivePic = pygame.image.load("alive1.jpg")
    
    deadPic = pygame.image.load("dead1.jpg")
    backgrounds = [alivePic, deadPic]
    
    #create window title 
    pygame.display.set_caption("minimal program")
    #set icon image
    pygame.display.set_icon(alivePic)
    #set window size
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #pygame.NOFRAME
   
    #set to False to exit game
    running = True
    pygame.display.set_icon(logo)
    
    width, height = pygame.display.get_surface().get_size()

    text = font.render("You lose.", True, (255, 0, 0) )
    

    #screen.blit(pygame.transform.scale(backgrounds[0], (width, height)), (0,0))
   

    startTime = pygame.time.get_ticks()
    while running:
        if pygame.time.get_ticks()  > startTime + TIME_FOR_DECSISION * 1000:
            pygame.mixer.music.load('wickedlaugh1.wav')
            pygame.mixer.music.play()
            screen.blit(pygame.transform.scale(backgrounds[1], (width, height)), (0,0))
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    running = False
                if event.key == pygame.K_1:
                    
                    screen.blit(text,
                                        ((width - text.get_width()) // 2, (height- text.get_height()) // 2))
                    pygame.display.flip()



if __name__ == "__main__":
    main()
    #used to restart program infinitely
    #os.execv(sys.executable, ['python'] + sys.argv)
