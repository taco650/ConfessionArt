import pygame
import os
import sys

def main():
    #Game Constants
    TIME_FOR_DECSISION = 40
    LOST_POPUP = 2


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
    pygame.display.set_caption("Confession Art")
    #set icon image
    pygame.display.set_icon(alivePic)
    #set window size
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #pygame.NOFRAME
   
    #set to False to exit game
    running = True
    pygame.display.set_icon(logo)
    
    width, height = pygame.display.get_surface().get_size()

    text = font.render("You lose.", True, (255, 0, 0) )
    

    screen.fill((0,0,0))
    screen.blit(pygame.transform.scale(backgrounds[0], (width, height)), (0,0))
    pygame.display.flip()
   
    lostTrigger = 0
    startTime = pygame.time.get_ticks()
    while running:
        if lostTrigger == -1 or (lostTrigger == 0  and pygame.time.get_ticks()  > startTime + TIME_FOR_DECSISION * 1000):
            screen.blit(pygame.transform.scale(backgrounds[1], (width, height)), (0,0))
            pygame.display.flip()
            lostTrigger = 1
            startTime = pygame.time.get_ticks()
        
        if lostTrigger == 1 and pygame.time.get_ticks()  > startTime + LOST_POPUP * 1000:
            #screen.blit(pygame.transform.scale( backgrounds[1], (width, height)), (0,0))
            screen.blit(text,
                            ((width - text.get_width()) // 2, (height- text.get_height()) // 2))
            pygame.display.flip()
            pygame.mixer.music.load('wickedlaugh1.wav')
            pygame.mixer.music.play(1)
            lostTrigger = 2
            startTime = pygame.time.get_ticks()
        
        if lostTrigger == 2 and pygame.time.get_ticks()  > startTime + 1 * 1000:
            
            screen.blit(vertical((width, height+20), (0, 0, 0, 125), (0, 0, 0, 0)),  (0,0))
            screen.blit(text,
                            ((width - text.get_width()) // 2, (height- text.get_height()) // 2))
            pygame.display.flip()
            
            if pygame.time.get_ticks()  > startTime + 5 * 1000:
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    lostTrigger = -1
                if event.key == pygame.K_1:
                    lostTrigger = -1
                if event.key == pygame.K_2:
                    lostTrigger = -1
                if event.key == pygame.K_3:
                    lostTrigger = -1
                if event.key == pygame.K_4:
                    lostTrigger = -1 
                if event.key == pygame.K_5:
                    lostTrigger = -1
                if event.key == pygame.K_6:
                    lostTrigger = -1
                if event.key == pygame.K_7:
                    lostTrigger = -1
                if event.key == pygame.K_8:
                    lostTrigger = -1
                if event.key == pygame.K_9:
                    lostTrigger = -1
                if event.key == pygame.K_HOME:
                    running = False
                    
                   


def vertical(size, startcolor, endcolor):
    """
    Draws a vertical linear gradient filling the entire surface. Returns a
    surface filled with the gradient (numeric is only 2-3 times faster).
    """
    height = size[1]
    bigSurf = pygame.Surface((1,height)).convert_alpha()
    dd = 1.0/height
    sr, sg, sb, sa = startcolor
    er, eg, eb, ea = endcolor
    rm = (er-sr)*dd
    gm = (eg-sg)*dd
    bm = (eb-sb)*dd
    am = (ea-sa)*dd
    for y in range(height):
        bigSurf.set_at((0,y),
                        (int(sr + rm*y),
                         int(sg + gm*y),
                         int(sb + bm*y),
                         int(sa + am*y))
                      )
    pygame.time.delay(20)
    return pygame.transform.scale(bigSurf, size)

if __name__ == "__main__":
    main()
    #used to restart program infinitely
    os.execv(sys.executable, ['python'] + sys.argv)
