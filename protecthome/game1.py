import pygame,math,random,time
from pygame.locals import *
pygame.init()
pygame.mixer.init()
width,height=640,640
screen=pygame.display.set_mode((width,height))
keys=[False,False,False,False]
playerpos=[100,100]
acc=[0,0]
arrows=[]
start=100
end=0
badguys=[[597,30]]
healthvalues=100
castle_list=[(0,30),(0,135),(0,240),(0,345)]
player=pygame.image.load('pictures/@~ZN0`F62918P2M3@KXR0GN.png')
bg=pygame.image.load('pictures/1UGG(X[Q`0CII~BC]W6QKQ9.png')
aw=pygame.image.load('pictures/1.png')
grass=pygame.image.load('pictures/5969d42932159.jpg')
castle=pygame.image.load('pictures/%(S%RAJ0DB@LPF2RJNX{5ZU.png')
health=pygame.image.load('pictures/9[V%3{A~1O7XNPCQHE$)1(0.png')
healthbar = pygame.image.load("pictures/PSE6P4UQE6N(N7IW7D`JXPX.png")
# hit = pygame.mixer.Sound("video/高梨康治 - FAIRY TAIL メインテーマ (1).wav")
# enemy = pygame.mixer.Sound("video/高梨康治 - FAIRY TAIL メインテーマ (1).wav")
# shoot = pygame.mixer.Sound("video/高梨康治 - FAIRY TAIL メインテーマ (1).wav")
# hit.set_volume(0.05)
# enemy.set_volume(0.05)
# shoot.set_volume(0.05)
# pygame.mixer.music.load('video/高梨康治 - FAIRY TAIL メインテーマ (1).wav')
# pygame.mixer.music.play(-1, 0.0)
# pygame.mixer.music.set_volume(0.25)
# print(player.get_rect().height)
long=1
while long:

    screen.fill(0)
    for i in range(width//grass.get_width()+1):
        for j in range(height//grass.get_height()+1):
            screen.blit(grass,(i*100,j*100))
    # screen.blit(player,playerpos)
    screen.blit(castle,(0,30))
    for xy in castle_list:
        screen.blit(castle, xy)
    # screen.blit(castle, (0, 135))
    # screen.blit(castle, (0, 240))
    # screen.blit(castle, (0, 345))
    position=pygame.mouse.get_pos()
    angle=math.atan2(position[1]-(playerpos[1]+player.get_rect().height//2),position[0]-(playerpos[0]+player.get_rect().width//2))
    player1=pygame.transform.rotate(player,360-angle*59.27)
    playerpos1=(playerpos[0]-player1.get_rect().width//2,playerpos[1]-player1.get_rect().height//2)
    # playerpos2 = (arrowss[0] - player1.get_rect().width // 2, arrowss[1] - player1.get_rect().height // 2)
    position = pygame.mouse.get_pos()
    screen.blit(player1,playerpos1)
    for arrow in arrows:
        # index=0
        velx=math.cos(arrow[0])*10
        vely=math.sin(arrow[0])*10
        arrow[1]+=velx
        arrow[2]+=vely
        if arrow[1]>640 or arrow[2]>640 or arrow[1]<-player.get_rect().width or arrow[2]<-player.get_rect().width:
            try:
                arrows.remove([arrow[0],arrow[1],arrow[2]])
            except Exception as e:
                continue
        # index+=1
        for i in arrows:
            arrow1=pygame.transform.rotate(aw,360-i[0]*59.27)
            screen.blit(arrow1,(i[1],i[2]-33))
    if start==0:
        badguys.append([597,random.choices((30,135,240,345))[0]])
        start=100
        end=0
    elif start:
        start-=2
        end+=2
        # time.sleep(0.5)
    for badguy in badguys:
        if badguy[0]<43:
            # hit.play()
            badguys.pop(0)
        badguy[0]-=2
        badrect=pygame.Rect(bg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<43:
            healthvalues-=random.randint(5,10)
            # print(healthvalues)
            if healthvalues<=0:
                long=0
                if long==0:
                    for i in range(width // grass.get_width() + 1):
                        for j in range(height // grass.get_height() + 1):
                            screen.blit(grass, (i * 100, j * 100))
                            input()


                # exit('gameover')
        for bullet in arrows:
            bulrect=pygame.Rect(player.get_rect())
            bulrect.left=bullet[1]
            bulrect.top=bullet[2]
            if badrect.colliderect(bulrect):
                # enemy.play()
                acc[1]+=1
                badguys.remove([badguy[0], badguy[1]])
                try:
                    arrows.remove([arrow[0],arrow[1],arrow[2]])
                except Exception as e:
                    continue


    for badguy in badguys:
        screen.blit(bg,tuple(badguy))
        # ///////////



    font = pygame.font.Font(None, 24)
    survivedtext = font.render(
        str((90000 - pygame.time.get_ticks()) / 60000) + ":" + str((90000 - pygame.time.get_ticks()) / 1000 % 60).zfill(
            2), True, (0, 0, 0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635, 5]
    screen.blit(survivedtext, textRect)
    screen.blit(healthbar, (5, 5))
    for health1 in range(healthvalues):
        screen.blit(health, (health1 + 8, 8))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            # pygame.quit()
            exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_s:
                keys[1]=True
            elif event.key==K_a:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0] =False
            elif event.key==pygame.K_s:
                keys[1] =False
            elif event.key == pygame.K_a:
                keys[2] =False
            elif event.key == pygame.K_d:
                keys[3] =False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # shoot.play()
            position=pygame.mouse.get_pos()
            acc[0]+=1
            arrows.append([math.atan2(position[1]-(playerpos[1]+player.get_rect().height//2),position[0]-(playerpos[0]+player.get_rect().width//2)),playerpos1[0]+32,playerpos1[1]+32])



    if keys[0] :
        playerpos[1]-=5
    elif keys[1] :
        playerpos[1]+=5
    elif keys[2] :
        playerpos[0]-=5
    elif keys[3] :
        playerpos[0]+=5

