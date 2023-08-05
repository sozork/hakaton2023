#импортируем библиотеки
import pygame
from random import randint
from time import time as timer

pygame.init()
# классы
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h, naprav):
        global titles
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_w
        self.hight = player_h
        self.die = False
        self.startx = player_x
        self.starty = player_y
        self.naprav = naprav
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if titles[0].rect.x <=300:
                player.naprav = "left"
                self.rect.x += self.speed
        if keys[pygame.K_d]:
            if titles[8].rect.x >=300:
                player.naprav = "right"
                self.rect.x -= self.speed
        if keys[pygame.K_w]:
            if titles[0].rect.y <=180:
                player.naprav = "top"
                self.rect.y += self.speed
        if keys[pygame.K_s]:
            if titles[len(titles)-5].rect.y >230:
                player.naprav = "down"
                self.rect.y -= self.speed
    def move2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if titles[0].rect.x <=300:
                player.naprav = "left"
                self.rect.x += self.speed
        if keys[pygame.K_d]:
            if titles[14].rect.x >=300:
                player.naprav = "right"
                self.rect.x -= self.speed
        if keys[pygame.K_w]:
            if titles[14].rect.y <=180:
                player.naprav = "top"
                self.rect.y += self.speed
        if keys[pygame.K_s]:
            if titles[len(titles)-1].rect.y >230:
                player.naprav = "down"
                self.rect.y -= self.speed
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
# класс игрока
class Player(GameSprite):
    
    def animcr(self):
        self.naprav = "down"
        self.spritesleft = []
        self.spritesright = []
        self.spritestop = []
        self.spritesdown = []
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown1.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown2.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
        image = pygame.transform.scale(pygame.image.load("images/player/playertop1.png"), (self.width, self.hight))
        self.spritestop.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playertop2.png"), (self.width, self.hight))
        self.spritestop.append(image)
        self.current_sprite = 0
        self.image = self.spritestop[int(self.current_sprite)]
        image = pygame.transform.scale(pygame.image.load("images/player/playerleft1.png"), (self.width, self.hight))
        self.spritesleft.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playerleft2.png"), (self.width, self.hight))
        self.spritesleft.append(image)
        self.current_sprite = 0
        self.image = self.spritesleft[int(self.current_sprite)]
        image = pygame.transform.scale(pygame.image.load("images/player/playerright1.png"), (self.width, self.hight))
        self.spritesright.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playerright2.png"), (self.width, self.hight))
        self.spritesright.append(image)
        self.current_sprite = 0
        self.image = self.spritesright[int(self.current_sprite)]
    def animdown(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animtop(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritestop[int(self.current_sprite)]
    def animright(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesright[int(self.current_sprite)]
    def animleft(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesleft[int(self.current_sprite)]

    def move(self):
        self.rect = pygame.rect.Rect(self.rect.x, self.rect.y, self.width,self.hight)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.naprav = "left"
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.naprav = "right"
            self.rect.x += self.speed 
        
    def jump(self):
        if self.die == False:
            
            global jumpspeed
            global is_jump
            global canfall
            if is_jump != False:
                if self.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerleftjump.png"), (player.width, player.hight))
                    self.image = image
                if self.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerrightjump.png"), (player.width, player.hight))
                    self.image = image
                if jumpspeed >= -startjumpspeed+1:
                    if jumpspeed > 0:
                        self.rect.y -= (jumpspeed ** 2) / 2
                    else:
                        if canfall == True:
                            self.rect.y += (jumpspeed ** 2) / 2-3
                    jumpspeed -= 1
                else:
                    if self.naprav == "left":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                        self.image = image
                    if self.naprav == "right":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                        self.image = image
                    canfall = True
                    jumpspeed = startjumpspeed    
                    is_jump = False 
            
    def isdead(self):
        self.speed = 0
        self.image = pygame.image.load("images/nothing.png")
        self.die = True
    def fire(self):
        bullet = Bullet("images/bulletleft.png", player.rect.x, player.rect.y+10, 10, 10, 10, player.naprav)
        if player.naprav == "right":
            bullet.image = pygame.transform.scale(pygame.image.load("images/bulletright.png"), (10, 10))
        if player.naprav == "top":
            bullet.image = pygame.transform.scale(pygame.image.load("images/bullettop.png"), (10, 10))
        if player.naprav == "down":
            bullet.image = pygame.transform.scale(pygame.image.load("images/bulletdown.png"), (10, 10))
        bullets.append(bullet)
class Player2(GameSprite):
    
    def animcr(self):
        self.naprav = "down"
        self.spritesleft = []
        self.spritesright = []
        self.spritestop = []
        self.spritesdown = []
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown1.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown2.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
        image = pygame.transform.scale(pygame.image.load("images/player/playertop1.png"), (self.width, self.hight))
        self.spritestop.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playertop2.png"), (self.width, self.hight))
        self.spritestop.append(image)
        self.current_sprite = 0
        self.image = self.spritestop[int(self.current_sprite)]
        image = pygame.transform.scale(pygame.image.load("images/player2/player2left1.png"), (self.width, self.hight))
        self.spritesleft.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player2/player2left2.png"), (self.width, self.hight))
        self.spritesleft.append(image)
        self.current_sprite = 0
        self.image = self.spritesleft[int(self.current_sprite)]
        image = pygame.transform.scale(pygame.image.load("images/player2/player2right1.png"), (self.width, self.hight))
        self.spritesright.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player2/player2right2.png"), (self.width, self.hight))
        self.spritesright.append(image)
        self.current_sprite = 0
        self.image = self.spritesright[int(self.current_sprite)]
    def animdown(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animtop(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritestop[int(self.current_sprite)]
    def animright(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesright[int(self.current_sprite)]
    def animleft(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesleft[int(self.current_sprite)]

    def move(self):
        self.rect = pygame.rect.Rect(self.rect.x, self.rect.y, self.width,self.hight)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.naprav = "right"
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.naprav = "left"
            self.rect.x += self.speed 
    
    def jump(self):
        if self.die == False:
            global jumpspeed2
            global is_jump2
            global canfall2
            if is_jump2 != False:
                if self.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2leftjump.png"), (player.width, player.hight))
                    self.image = image
                if self.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2rightjump.png"), (player.width, player.hight))
                    self.image = image
                if jumpspeed2 >= -startjumpspeed2+1:
                    if jumpspeed2 > 0:
                        self.rect.y -= (jumpspeed2 ** 2) / 2
                    else:
                        if canfall2 == True:
                            self.rect.y += (jumpspeed ** 2) / 2-3
                    jumpspeed2 -= 1
                else:
                    if self.naprav == "left":
                        image = pygame.transform.scale(pygame.image.load("images/player2/player2left.png"), (player.width, player.hight))
                        self.image = image
                    if self.naprav == "right":
                        image = pygame.transform.scale(pygame.image.load("images/player2/player2right.png"), (player.width, player.hight))
                        self.image = image
                    canfall2 = True
                    jumpspeed2 = startjumpspeed2    
                    is_jump2 = False 
            
    def isdead(self):
        self.speed = 0
        self.image = pygame.image.load("images/nothing.png")
        self.die = True
# класс противников
class Enemy(GameSprite):
    def tel(self):
        self.rect.x = randint(10, 700) 
        self.rect.y = randint(10, 500) 
        i = randint(1, 2)
        if self.rect.y <=430 and self.rect.y >= 20:
            if i == 1:
                self.rect.x = 0
            if i == 2:
                self.rect.x = 700
        self.speed = randint(1,2)
    def run(self):
        if self.rect.x <player.rect.x:
            self.rect.x+= self.speed
        if self.rect.x >player.rect.x:
            self.rect.x-= self.speed  
        if self.rect.y <player.rect.y:
            self.rect.y+= self.speed
        if self.rect.y >player.rect.y:
            self.rect.y-= self.speed
    def animcr(self):
        self.naprav = "down"
        self.spritesleft = []
        self.spritesright = []
        self.spritestop = []
        self.spritesdown = []
        image = pygame.transform.scale(pygame.image.load("images/crab1.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        image = pygame.transform.scale(pygame.image.load("images/crab2.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def anim(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]

# класс пуль
class Bullet(GameSprite):
    def fly(self):
        if self.naprav == "left":
            self.rect.x-=self.speed
        if self.naprav == "right":
            self.rect.x+=self.speed
        if self.naprav == "top":
            self.rect.y-=self.speed
        if self.naprav == "down":
            self.rect.y+=self.speed
# класс мусора
class Trash(GameSprite):
    def tel(self):
        i = randint(1, 2)
        if i == 1:
            self.image = pygame.transform.scale(pygame.image.load("images/shark.png"), (self.width, self.hight+30))
            self.rect.x = randint(10, 700-self.width) 
            self.rect.y = 10
            self.speed = randint(1,3)
        if i == 2:
            self.image = pygame.transform.scale(pygame.image.load("images/pirnia.png"), (self.width, self.hight))
            self.rect.x = randint(10, 700-self.width) 
            self.rect.y = 10
            self.speed = randint(3,6)
    def fall(self):
        self.rect.y += self.speed
# класс текста
class Text():
    def __init__(self, text_x, text_y, text, font, color):
        self.x = text_x
        self.y = text_y
        self.text = text
        self.font = font
        self.color = color
        self.size = self.font.size(str(self.text))
        self.surface = pygame.Surface([self.size[0]+10, self.size[1]+10], pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
        self.surface.fill((0, 0, 0, 180))
    def apear(self):
        self.word = self.font.render(str(self.text), True, self.color)
        win.blit(self.surface, (self.x-5, self.y-5))
        win.blit(self.word, (self.x, self.y))
        
# разные тексты
texts = []
text0 = "phone: Привет, не мог ли ты мне достать "
text1 = "phone: потеряную риликвию со дна моря?"
text2 = "phone: Ты же не далеко живёшь, помоги. "
text3 = "phone: Она очень важна для меня. "
text4 = "вы: Ладно, ты сможешь помочь мне  "
text5 = "вы: с её поиском? "
text6 = "phone: Конечно, одевайся и выходи. "
text7 = "phone: Потом раскажу подробности."
text8 = "звонок обрывается"
text9 = "вы: Ладно я иду."
text10 = "Встроеный наушник: Спуститесь в море 'space'"
text11 = "cave, коснитесь чтобы"
text12 = "перейти на след. уровень"
text13 = "Enemy, если она дойдёт"
text14 = "до пещеры, то вы проиг-"
text15 = "раете, так же она пов-"
text16 = "торяет, все ващи дейст-"
text17 = "вия, только наоборот."
text18 = "Шипы, если вы или enemy"
text19 = "наступит на них, то ум-"
text20 = "рёте, вам стоит быть ос-"
text21 = "торожнее"
text22 = "D, идти в лево"
text23 = "W, прыжок"
text24 = "A, идти в право"
text25 = "Вы нашли спп, этот пистолет"
text26 = "может стрелять под водой'f'"
text27 = "Встроеный наушник: Тебе не стоит пока тратить "
text28 = "патроны "
texts.append(text0)
texts.append(text1)
texts.append(text2)
texts.append(text3)
texts.append(text4)
texts.append(text5)
texts.append(text6)
texts.append(text7)
texts.append(text8)
texts.append(text9)
texts.append(text10)
texts.append(text11)
texts.append(text12)
texts.append(text13)
texts.append(text14)
texts.append(text15)
texts.append(text16)
texts.append(text17)
texts.append(text18)
texts.append(text19)
texts.append(text20)
texts.append(text21)
texts.append(text22)
texts.append(text23)
texts.append(text24)
texts.append(text25)
texts.append(text26)
texts.append(text27)
texts.append(text28)
# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# назначаю шрифты
pygame.font.init()
font1 = pygame.font.Font("better-vcr_0.ttf", 20)
font2 = pygame.font.Font("better-vcr_0.ttf", 8)
font3 = pygame.font.Font("better-vcr_0.ttf",100)
# переменная для списка тайтлов
titles = []        
dietitles = []
doors = []
buttons = []
# переменые
startjumpspeed = 9
jumpspeed = startjumpspeed
startjumpspeed2 = startjumpspeed
jumpspeed2 = startjumpspeed2
is_jump = False
is_jump2 = False
isdark = True
pause = False
canfall = True
canfall2 = True
currentlvl = -1
currentmap = 0
canplay1 = True
canplay2 = False
game2 = False
losegame2 = False
fallgame2stop = False
canbigfall = True
cansetcurecttime = True
game3 = False
naprav = "down"
bullets = list()
menu = True
canplay3 = True
game3 = False
enemys = list()
hp = 3
stopgame = False
canspawn = True
killcount = 0
cancarrysomething = False
gameend = False
iscutscene = False
currenttext = 0
spp = GameSprite("images/spp.png", 170, 380, 0, 30, 30, "none")
bulletscount = 10
canpickupclip = True
dificulty = 0
canshowdif = False
canshowopt = False
canplaywalksound = True
# звуки
sounds = []
musicvolume = 1
soundvolume = 1
shag = pygame.mixer.Sound("sounds/shag.mp3")
shag.set_volume(soundvolume)
sounds.append(shag)
jumpsound = pygame.mixer.Sound("sounds/jumpsound.mp3")
jumpsound.set_volume(soundvolume)
sounds.append(jumpsound)
clicksound = pygame.mixer.Sound("sounds/click.mp3")
clicksound.set_volume(soundvolume)
sounds.append(clicksound)
doorsound = pygame.mixer.Sound("sounds/doorsound.mp3")
doorsound.set_volume(soundvolume)
sounds.append(doorsound)
watersound = pygame.mixer.Sound("sounds/water.mp3")
watersound.set_volume(soundvolume)
sounds.append(watersound)
callendsound = pygame.mixer.Sound("sounds/endcall.mp3")
callendsound.set_volume(soundvolume)
sounds.append(callendsound)
phonesound = pygame.mixer.Sound("sounds/phonecall.ogg")
phonesound.set_volume(soundvolume)
sounds.append(phonesound)
shotsound = pygame.mixer.Sound("sounds/shot.mp3")
shotsound.set_volume(soundvolume)
sounds.append(shotsound)
# музыка
pygame.mixer.music.load("sounds/menumusic.mp3")
pygame.mixer.music.set_volume(musicvolume)
pygame.mixer.music.play(-1)


# затемнение экрана
def screendark():
    image = pygame.Surface([700,500], pygame.SRCALPHA, 32)
    image.fill((0,0,0))
    for alpha in range (0, 50):
        image.set_alpha(alpha)
        win.blit(image, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)   
# создание функции для применения колизии и прыжка
def do_collide(titles):
    global is_jump
    global is_jump2
    global canfall2
    global canfall
    # косание иголок == рестарт!
    for object in dietitles:
        if pygame.sprite.collide_rect(player2, object) :
            player2.isdead()
        if pygame.sprite.collide_rect(player3, object):
            player3.isdead()
    # колизия с разными сторонами объектов
    for object in titles:
        if player2.rect.collidepoint(object.rect.midtop) or player2.rect.collidepoint(object.rect.topleft) or player2.rect.collidepoint(object.rect.topright):
            player2.rect.y = object.rect.y-player2.hight
            print(object.rect.midtop, player2)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                is_jump = True 
                jumpsound.play()
                canfall = True  
        
        if player3.rect.collidepoint(object.rect.midtop) or player3.rect.collidepoint(object.rect.topleft) or player3.rect.collidepoint(object.rect.topright):
            player3.rect.y = object.rect.y-player3.hight
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                is_jump2 = True 
                canfall2 = True 
       
        if pygame.sprite.collide_rect(player3, object):
            canfall = False
        else:
            canfall = True
        if pygame.sprite.collide_rect(player3, object):
            canfall2 = False
        else:
            canfall2 = True
        # падение
        player2.rect.y +=1 
        player3.rect.y +=1 
    # ИСПОЛЬЗОВАНИЕ ДВЕРЕЙ
    for object in doors:
        global currentlvl
        global currentmap
        global currentlvl
        if pygame.sprite.collide_rect(player2, object):
            currentmap +=1
        if pygame.sprite.collide_rect(player3, object):
            if currentlvl == 2:
                rest(15, 300, 310, 300)
            if currentlvl == 3:
                rest(15, 300, 500, 300)
            if currentlvl == 4:
                rest(15, 300, 629, 300)
            if currentlvl == 5:
                rest(15, 300, 629, 310)
            if currentlvl == 6:
                rest(15, 300, 15, 140)
            if currentlvl == 7:
                rest(15, 200, 629, 300)
# функция создания карты
def Createmap(map):
    global TitleX
    global line
    for word in map:
        if word == "w":
            wall = GameSprite("images/wall.png", TitleX, line, 5, 70, 70, "net")
            titles.append(wall)
            TitleX += 70
        if word == "/":
            line += 32
            TitleX = 0
        if word == "a":
            i = randint(1, 5)
            floor = GameSprite("images/floor_"+str(i) + ".png", TitleX, line, 5, 70, 70, "net")
            titles.append(floor)
            TitleX += 70
        if word == "p":
            plate = GameSprite("images/plate_1.png", TitleX, line, 10, 70, 26, "net")
            titles.append(plate)
            TitleX += 70
        if word == "v":
            plate = GameSprite("images/plate_2.png", TitleX, line, 10, 70, 26, "net")
            titles.append(plate)
            TitleX += 70
        if word == "r":
            plate = GameSprite("images/plate_3.png", TitleX, line, 10, 70, 26, "net")
            titles.append(plate)
            TitleX += 70
        if word == "l":
            plate = GameSprite("images/plate_4.png", TitleX, line, 10, 70, 26, "net")
            titles.append(plate)
            TitleX += 70
        if word == "n":
            TitleX += 70
        if word == "s":
            spike = GameSprite("images/spikes.png", TitleX, line, 0, 50, 32, "net")
            titles.append(spike)
            dietitles.append(spike)
            TitleX += 70
        if word == "d":
            door= GameSprite("images/underwatercave.png", TitleX, line, 0, 70, 70, "net")
            titles.append(door)
            doors.append(door)
            TitleX += 70
        if word == "f":
            i = randint(1, 5)
            floor = GameSprite("images/planks_"+str(i) + ".png", TitleX, line, 5, 70, 70, "net")
            titles.append(floor)
            TitleX += 70
# создаю 1 уровень
cave_1 = GameSprite("images/cave_1.png", 760, 50, 5, 140, 450, "net")        
door = GameSprite("images/door.png", 500, 130, 5, 80, 90, "net")        
# создаю карту
map ="fffffffff//fffffffff//fffffffff//fffffffff//fffffffff//fffffffff//fffffffff"
TitleX = 0
line = 0
titles.clear()
#  фон
sky = GameSprite("images/sky.png", 0, 0, 0, 700, 500, "net")
# идёт загрузка подождите
print("!!!Идёт загрузка подождите!!!")
# Функция для создания карты
Createmap(map)
# количество нажатий на мусор
najat = 0
# Фунуция рестарта
def rest(x, y, x2, y2):
    global player2
    global player3
    player2.die = False
    player3.die = False
    player2 = Player("images/player/playerdown1.png", x, y, 10, 70, 70, "net")
    player2.animcr()
    player3 = Player2("images/player/playerdown1.png", x2, y2, -10, 70, 70, "net")
    player3.animcr()
    player2.die = False
    player3.die = False
    
# создаём окно игры и настраеваем его
win = pygame.display.set_mode((700, 500))
pygame.display.set_caption(":)(●'◡'●):-):-)^_^ಥ_ಥ(┬┬﹏┬┬)☆*: .｡. o(≧▽≦)o .｡.:*☆")
# создаём объект clock
clock = pygame.time.Clock()
# fps и исловие для основного цикла.
run = True
fps = 30
# CОЗДАНИЕ ОБЪЕКТОВ КЛАССов
player = Player("images/player/playerdown1.png", 300, 200, 5, 70, 70, "net")
player.animcr()
# создаю игрока для платформ
player2 = Player("images/player/playerdown1.png", 15, 300, 10, 70, 70, "net")    

player3 = Player2("images/player/playerdown1.png", 310, 300, 10, 70, 70, "net")   
# "мусор"
trash1 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash2 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash3 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash4 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash5 =Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash6 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash7 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash8 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash9 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash10 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trash11 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60, "net")
trashs = list()
trashs.append(trash1)
trashs.append(trash2)
trashs.append(trash3) 
trashs.append(trash4)
trashs.append(trash5)
trashs.append(trash6)
trashs.append(trash7)
trashs.append(trash8)
trashs.append(trash9)
trashs.append(trash10)
trashs.append(trash11)
trash1.tel()
trash2.tel()
trash3.tel()
trash4.tel()
trash5.tel()
trash6.tel()
trash7.tel()
trash8.tel()
trash9.tel()
trash10.tel()
trash11.tel()
trashBIG = Trash("images/bigshark.png", 200, 10, 2, 200, 200, "net")
# разные карты
map1 ="aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa/"
map2 = "aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa/"
map3 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnndnnnnn/nnnnnnsnnnnnnnn/lrnnlpprnvnnnnnnn/"
map4 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/dnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/lprnnnnnnnnnnnn/nnnnnnnnnsnnnnn/nnnnlpprnvnnnnnnn/"
map5 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnndnnnnnnnnn/nnnnnnnnnnnnnnn/lprnlprnnvnnnnnnn/"
map6 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/lppppprnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnndnnnnn/nnnnnnnnnnnnnnn/lrnnlprnnvnnnnnnn/"
map7 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/vnnnndnnnnnnnnn/nnnnnnnnnnnnnn/nlrnlrnnlrnnnnn/"
# противники
enemy1 = Enemy("images/crab.png", randint(10, 700-60), 10, randint(1, 5), 70, 70, "net")
enemy1.tel()
enemy1.animcr()
enemys.append(enemy1)
enemy2 = Enemy("images/crab.png", randint(10, 700-60), 10, randint(1, 5), 70, 70, "net")
enemy2.tel()
enemy2.animcr()
enemys.append(enemy2)
enemy3 = Enemy("images/crab.png", randint(10, 700-60), 10, randint(1, 5), 70, 70, "net")
enemy3.tel()
enemy3.animcr()
enemys.append(enemy3)
enemy4 = Enemy("images/crab.png", randint(10, 700-60), 10, randint(1, 5), 70, 70, "net")
enemy4.tel()
enemy4.animcr()
enemys.append(enemy4)
enemy5 = Enemy("images/crab.png", randint(10, 700-60), 10, randint(1, 5), 70, 70, "net")
enemy5.tel()
enemy5.animcr()
enemys.append(enemy5)
enemy6 = Enemy("images/crab.png", randint(10, 700-60), 10, randint(1, 5), 70, 70, "net")
enemy6.tel()
enemy6.animcr()
enemys.append(enemy6)
enemy7 = Enemy("images/crab.png", randint(10, 700-60), 10, randint(1, 5), 70, 70, "net")
enemy7.tel()
enemy7.animcr()
enemys.append(enemy7)

# переменная для таймера
cancurecttime = True
done = False
starttime = timer()
# функция таймера
def timeset(time):
    global cancurecttime
    global done
    global starttime
    global losegame2
    global fallgame2stop
    global najat
    if cancurecttime == True:
        starttime = timer()
        cancurecttime = False
    curecttime = timer()
    if losegame2 == False:
        if curecttime - starttime >= time:
            done = True
            cancurecttime = True
    else:
        if curecttime - starttime <= time:
            fallgame2stop = True
            losetext = Text(130, 200, "U lose", font3, black)
            losetext.apear()
        else:
            done = True
            cancurecttime = True
            
# создание функции для применения методов класса ко всем его объектам
def do_function(titles):
    for object in titles:
        object.move2()
        object.reset()
def do_function3(titles):
    for object in titles:
        object.move()
        object.reset()
def do_function2(titles):
    for object in titles:
        object.reset()
def do_function4(trashs):
    for object in trashs:
        global najat
        # выход за экран == рест
        if object.rect.y >= 500-object.hight:
            najat -= 2
            object.tel()
        # нажатие мыши
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        # коснулась ли мышка мусора?
        if object.rect.collidepoint(pos):
            if pressed[0] == True:
                najat += 1
                shotsound.play()
                object.tel()
def do_function5():
    global najat
    global trashBIG
    # нажатие мыши
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    # коснулась ли мышка мусора?
    if trashBIG.rect.collidepoint(pos):
        if pressed[0] == True:
            shotsound.play()
            najat += 1
#  КОТОРЫЙ ЧАС
timme = timer()
# основной цикл
while run:
    for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                # заходим в уровень
                if pygame.sprite.collide_rect(player, door):
                    if i.key == pygame.K_SPACE:
                        currentmap +=1
                if game3 == True:
                    if bulletscount >0:
                        if i.key == pygame.K_f:
                            # стрелять
                            player.fire()
                            shotsound.play()
                            bulletscount -=1
                    else:
                        if cansetcurecttime == True:
                            pasttime = timer()
                            cansetcurecttime = False
                        currecttime = timer()
                        if currecttime-pasttime >=5:
                            bulletscount = 10
                            cansetcurecttime == True
                if iscutscene == True:
                    if currentlvl == 3:
                        if i.key == pygame.K_SPACE:
                            currenttext = 25
                            iscutscene = False
                            screendark()
                    if najat<100:
                        if canplay1 == False:
                            if game3 == False:
                                if i.key == pygame.K_SPACE:
                                    iscutscene = False
                                    screendark()
                                else:
                                    if i.key == pygame.K_SPACE:
                                        currenttext+=1
                    if game3 == True:
                        if i.key == pygame.K_SPACE:
                            iscutscene = False
                            screendark()
                    else:
                        if i.key == pygame.K_SPACE:
                            currenttext+=1
                    if currentlvl == 7:
                        if i.key == pygame.K_SPACE:
                            currenttext = 27
                            iscutscene = False
                            screendark()
                    else:
                        if i.key == pygame.K_SPACE:
                            currenttext+=1
                            clicksound.play()
    if pause == False:
        if menu == True:
            # текст для настроек
            text = Text(260, 50, round(musicvolume, 2), font1, white)
            text2 = Text(260, 180, round(soundvolume, 2), font1, white)
            # фон
            bg = GameSprite("images/bgformenu.png", 0, 0, 0, 700, 500, "net")
            # создаю иконки игр
            plate = GameSprite("images/startplay.png", 280, 190, 10, 130, 100, "net")
            options = GameSprite("images/options.png", 250, 300, 10, 180, 100, "net")
            low = GameSprite("images/low.png", 20, 30, 10, 180, 100, "net")
            normal = GameSprite("images/normal.png", 20, 250, 10, 180, 100, "net")
            hard = GameSprite("images/hard.png", 510, 30, 10, 180, 100, "net")
            hardcore = GameSprite("images/hardcore.png", 510, 250, 10, 180, 100, "net")
            volume = GameSprite("images/volume.png", 30, 30, 10, 220, 100, "net")
            sound = GameSprite("images/sound.png", 30, 150, 10, 220, 100, "net")
            back = GameSprite("images/back.png", 550, 380, 10, 120, 100, "net")
            # отрисовка окон
            bg.reset()
            if canshowdif == True:
                low.reset()
                normal.reset()
                hard.reset()
                hardcore.reset()
            else:
                plate.reset()
                options.reset()
            # нажатие мыши
            pressed = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            # НАЖАЛИ ЛИ НА КНОПКУ УРОВНЯ?
            if canshowdif == False and canshowopt == False:
                if plate.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        canshowdif = True
                        clicksound.play()
                if options.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        canshowopt = True
                        clicksound.play()
            if canshowopt == True:
                bg.reset()
                volume.reset()
                text.apear()
                back.reset()
                sound.reset()
                text2.apear()
                if volume.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        musicvolume += 0.01
                        if musicvolume >= 1:
                            musicvolume = 0
                if sound.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        soundvolume += 0.01
                        if soundvolume >= 1:
                            soundvolume = 0
                if back.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        canshowdif = False
                        canshowopt = False
                for sound in sounds:
                    sound.set_volume(soundvolume)
                pygame.mixer.music.set_volume(musicvolume)
                    
                    
            if canshowdif == True:
                back.reset()
                if low.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        dificulty = 0.9
                        currentlvl = 0
                        menu = False
                        clicksound.play()
                        pygame.mixer.music.stop()
                        iscutscene = True
                        screendark()

                if normal.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        dificulty = 1
                        currentlvl = 0
                        menu = False
                        clicksound.play()
                        pygame.mixer.music.stop()
                        iscutscene = True
                        screendark()
                if hard.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        dificulty = 1.3
                        currentlvl = 0
                        menu = False
                        clicksound.play()
                        pygame.mixer.music.stop()
                        iscutscene = True
                        screendark()
                if hardcore.rect.collidepoint(pos):
                    print(pos, plate.rect.x, plate.rect.y)
                    if pressed[0] == True:
                        dificulty = 1.7
                        currentlvl = 0
                        menu = False
                        iscutscene = True
                        clicksound.play()
                        pygame.mixer.music.stop()
                        screendark()
                if back.rect.collidepoint(pos):
                        print(pos, plate.rect.x, plate.rect.y)
                        if pressed[0] == True:
                            canshowdif = False
                            canshowopt = False
                
        if currentlvl == 0:
            
            # текст
            text = Text(30,450,texts[currenttext], font1, white) 
            # кат сцена
            cutscene = GameSprite("images/cutscene1.png", 0, 0, 0, 700, 500, "net")
            if iscutscene == True:
                # звук звонка
                if currenttext == 8:
                    if canplaywalksound == True: 
                        callendsound.play()
                        canplaywalksound = False
                if currenttext == 9:
                    canplaywalksound = True
                    callendsound.stop()
                if currenttext >= 9:
                    callendsound.stop()
                cutscene.reset()
                text.apear()
                if currenttext >= 9:
                    screendark()
                    iscutscene = False
            else:
                phonesound.stop()
                # фон 
                bg = GameSprite("images/fon1.png", 0, 0, 0, 700, 500, "net")
                # Смена карты
                if currentmap == 1:
                    doorsound.play()
                    screendark()
                    #создание карты
                    map = map1
                    TitleX = 0
                    line = 50
                    titles.clear()
                    Createmap(map)
                    cave_1.rect.x = 900
                    currentlvl +=1
                    currenttext= 10
                # отрисофка фона
                bg.reset()
                # отрисовка тайтлов
                do_function3(titles)
                # уровни
                door.move()
                door.reset()
                # игрок
                player.reset()
                keys = pygame.key.get_pressed()
                # анимации
                if keys[pygame.K_s]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player.animdown()
                if keys[pygame.K_w]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player.animtop()
                if keys[pygame.K_a]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player.animleft()
                if keys[pygame.K_d]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player.animright()
                if keys[pygame.K_d] != True and keys[pygame.K_w] != True and keys[pygame.K_a] != True and keys[pygame.K_s] != True:
                    shag.stop()
                    canplaywalksound = True
                    if player.naprav == "down":
                        image = pygame.transform.scale(pygame.image.load("images/player/player1.png"), (player.width, player.hight))
                        player.image = image
                    if player.naprav == "top":
                        image = pygame.transform.scale(pygame.image.load("images/player/playertop.png"), (player.width, player.hight))
                        player.image = image
                    if player.naprav == "left":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                        player.image = image
                    if player.naprav == "right":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                        player.image = image
                # действия
                if keys[pygame.K_p]:
                    pause = True
        if currentlvl == 1:
            # текст
            text = Text(30,450,texts[currenttext], font1, white) 
            # подсказка
            space = GameSprite("images/space.png", 0, 0, 0, 80, 50, "net")
            # фон 
            bg = GameSprite("images/floor_2.png", 0, 0, 0, 700, 500, "net")
            # Смена карты
            if currentmap == 2:
                watersound.play()
                shag.stop()
                canplaywalksound = True
                screendark()
                #создание карты
                player.rect.x = 0
                currentlvl +=1
                pygame.mixer.music.load("sounds/elevatormusic.mp3")
                pygame.mixer.music.set_volume(musicvolume)
                pygame.mixer.music.play(-1)
                
            # отрисофка фона
            bg.reset()
            
            # отрисовка тайтлов
            do_function(titles)
            # уровни
            
            cave_1.move2()
            cave_1.reset()
            # игрок
            player.reset()
            keys = pygame.key.get_pressed()
            # отрисовка текста
            text.apear()
            # отрисовка подсказки
            if cave_1.rect.x <=300:
                space.rect.x = player.rect.x-10
                space.rect.y = player.rect.y-60
                space.reset()
            # анимации
            if keys[pygame.K_s]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player.animdown()
            if keys[pygame.K_w]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player.animtop()
            if keys[pygame.K_a]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player.animleft()
            if keys[pygame.K_d]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player.animright()
            if keys[pygame.K_d] != True and keys[pygame.K_w] != True and keys[pygame.K_a] != True and keys[pygame.K_s] != True:
                shag.stop()
                canplaywalksound = True
                if player.naprav == "down":
                    image = pygame.transform.scale(pygame.image.load("images/player/player1.png"), (player.width, player.hight))
                    player.image = image
                if player.naprav == "top":
                    image = pygame.transform.scale(pygame.image.load("images/player/playertop.png"), (player.width, player.hight))
                    player.image = image
                if player.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                    player.image = image
                if player.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                    player.image = image
            # действия
            if keys[pygame.K_p]:
                pause = True
        if currentlvl == 2: 
            # остановка звука входа в воду и ходьбы 
            watersound.stop()
            shag.stop()
            bg = GameSprite("images/bg3.png", 0, 0, 0, 700, 500, "net")
            # создаю иконки игр
            plate = GameSprite("images/game_1.png", 100, 100, 10, 150, 150, "net")
            plate2 = GameSprite("images/shark.png", 450, 100, 10, 150, 150, "net")
            plate3 = GameSprite("images/crab.png", 250, 300, 10, 150, 150, "net")
            # Смена карты
            if currentmap == 3:
                screendark()
                shag.stop()
                canplaywalksound = True
                #создание карты
                map = map3
                TitleX = 0
                line = 50
                titles.clear()
                dietitles.clear()
                doors.clear()
                Createmap(map)
                rest(15, 300, 500, 300)
                currentlvl+=1
            # отрисофка фона
            bg.reset()
            # отрисовка окон
            plate.reset()
            plate2.reset()
            plate3.reset()
            # нажатие мыши
            pressed = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            # НАЖАЛИ ЛИ НА КНОПКУ УРОВНЯ?
            if plate.rect.collidepoint(pos):
                print(pos, plate.rect.x, plate.rect.y)
                if pressed[0] == True:
                    if canplay1 == True:
                        iscutscene = True
                        currentmap = 3
                        clicksound.play()
                    else:
                        text = Text(30, 30, "ты уже там был", font1, white)
                        text.apear()
            if plate2.rect.collidepoint(pos):
                print(pos, plate2.rect.x, plate2.rect.y)
                if pressed[0] == True:  
                    if canplay2 == True:
                        canplay1 = False
                        canplay3 = False
                        canplay2 = False
                        game2 = True
                        iscutscene = True
                        clicksound.play()
                    else:
                        text = Text(30, 30, "Ты ещё туда не дошёл", font1, white)
                        text.apear()
            if plate3.rect.collidepoint(pos):
                print(pos, plate3.rect.x, plate3.rect.y)
                if pressed[0] == True:
                    if canplay3 == True:
                        canplay1 = False
                        game3 = True
                        clicksound.play()
                        iscutscene = True
                        cansetcurecttime == True
                    else:
                        text = Text(30, 30, "пока не туда", font3, white)
                        text.apear()
            
        if currentlvl == 3:   
            if iscutscene == True:
                # остановка музыки
                pygame.mixer.music.stop()
                # ФОН
                bg = GameSprite("images/cutscene2.png", 0, 0, 0, 700, 500, "net")
                bg.reset()
                # текст
                text = Text(180,30,texts[11], font2, white) 
                text2 = Text(180,60,texts[12], font2, white) 
                text.apear()
                text2.apear()
                text3 = Text(360,30,texts[13], font2, white) 
                text4 = Text(360,60,texts[14], font2, white) 
                text3.apear()
                text4.apear()
                text5 = Text(360,90,texts[15], font2, white) 
                text6 =Text(360,120,texts[16], font2, white) 
                text5.apear()
                text6.apear()
                text7 = Text(360,160,texts[17], font2, white) 
                text7.apear()
                text8 = Text(180,260,texts[18], font2, white) 
                text8.apear()
                text9 = Text(180,390,texts[19], font2, white) 
                text9.apear()
                text10 = Text(180,420,texts[20], font2, white) 
                text10.apear()
                text11 = Text(180,450,texts[21], font2, white) 
                text11.apear()
                text12 = Text(430,290,texts[22], font2, white) 
                text12.apear()
                text13 = Text(540,290,texts[23], font2, white) 
                text13.apear()
                text14 = Text(430,450,texts[24], font2, white) 
                text14.apear()
            else:    
                # Смена карты
                if currentmap == 4:
                    screendark()
                    #создание карты
                    map =map4
                    TitleX = 0
                    line = 50
                    titles.clear()
                    dietitles.clear()
                    doors.clear()
                    Createmap(map)
                    rest(310, 300, 500, 300)
                    currentlvl+=1
                # новая музыка
                pygame.mixer.music.load("sounds/musicforgame1.mp3")
                pygame.mixer.music.set_volume(musicvolume)
                pygame.mixer.music.play(-1)
                # прыжок и движение
                player2.jump()
                player2.move()
                player3.jump()
                player3.move()          
                # колизия
                do_collide(titles)     
                # отрисовка заднего фона
                sky.reset()
                # отрисовка тайтлов 
                do_function2(titles)
                # игрок
                
                player2.reset()
                player3.reset()
                if player2.rect.y >= 430:
                    player2.isdead()
                if player3.rect.y >= 430:
                    player3.isdead()
                keys = pygame.key.get_pressed()
                # запрещаю выходить за края!
                if player2.rect.x <= 0:
                    player2.rect.x = 0
                if player3.rect.x <= 0:
                    player3.rect.x = 0
                if player2.rect.x >= 630:
                    player2.rect.x = 630
                if player3.rect.x >= 630:
                    player3.rect.x = 630
                # игрок
                player2.reset()
                keys = pygame.key.get_pressed()
                # анимации
                if keys[pygame.K_a]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player2.animleft()
                if keys[pygame.K_d]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player2.animright()
                if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                    canplaywalksound = True
                    shag.stop()
                    if player2.naprav == "left":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                        player2.image = image
                    if player2.naprav == "right":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                        player2.image = image
                # ещё анимации
                if keys[pygame.K_a]:
                    player3.animright()
                if keys[pygame.K_d]:
                    player3.animleft()
                if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                    if player3.naprav == "left":
                        image = pygame.transform.scale(pygame.image.load("images/player2/player2left.png"), (player.width, player.hight))
                        player3.image = image
                    if player3.naprav == "right":
                        image = pygame.transform.scale(pygame.image.load("images/player2/player2right.png"), (player.width, player.hight))
                        player3.image = image
                # действия
                if keys[pygame.K_p]:
                    pause = True
                if keys[pygame.K_r]:
                    rest(15, 300, 310, 300)
        if currentlvl == 4:    
            # Смена карты
            if currentmap == 5:
                screendark()
                #создание карты
                map = map5
                TitleX = 0
                line = 50
                dietitles.clear()
                doors.clear()
                titles.clear()
                Createmap(map)
                rest(15, 300, 629, 300)
                currentlvl+=1
            # прыжок и движение
            player2.jump()
            player2.move()
            player3.jump()
            player3.move()          
            # колизия
            do_collide(titles)     
            # отрисовка заднего фона
            sky.reset()
            # отрисовка тайтлов 
            do_function2(titles)
            # игрок
            player2.reset()
            player3.reset()
            if player2.rect.y >= 430:
                player2.isdead()
            if player3.rect.y >= 430:
                player3.isdead()
            keys = pygame.key.get_pressed()
            # запрещаю выходить за края!
            if player2.rect.x <= 0:
                player2.rect.x = 1
            if player3.rect.x <= 0:
                player3.rect.x = 1
            if player2.rect.x >= 630:
                player2.rect.x = 629
            if player3.rect.x >= 630:
                player3.rect.x = 629
            # игрок
            player2.reset()
            keys = pygame.key.get_pressed()
            # анимации
            if keys[pygame.K_a]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player2.animleft()
            if keys[pygame.K_d]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player2.animright()
            if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                canplaywalksound= True
                shag.stop()
                if player2.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                    player2.image = image
                if player2.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                    player2.image = image
            # ещё анимации
            # ещё анимации
            if keys[pygame.K_a]:
                player3.animright()
            if keys[pygame.K_d]:
                player3.animleft()
            if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                if player3.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2left.png"), (player.width, player.hight))
                    player3.image = image
                if player3.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2right.png"), (player.width, player.hight))
                    player3.image = image
            # действия
            if keys[pygame.K_p]:
                pause = True
            if keys[pygame.K_r]:
                rest(310, 300, 500, 300)
        print(currentlvl)
        if currentlvl == 5:    
            # Смена карты
            if currentmap == 6:
                screendark()
                #создание карты
                map = map6
                TitleX = 0
                line = 50
                dietitles.clear()
                doors.clear()
                titles.clear()
                Createmap(map)
                rest(15, 300, 15, 140)
                currentlvl+=1
            # прыжок и движение
            player2.jump()
            player2.move()
            player3.jump()
            player3.move()          
            # колизия
            do_collide(titles)     
            # отрисовка заднего фона
            sky.reset()
            # отрисовка тайтлов 
            do_function2(titles)
            # игрок
            player2.reset()
            player3.reset()
            if player2.rect.y >= 430:
                player2.isdead()
            if player3.rect.y >= 430:
                player3.isdead()
            keys = pygame.key.get_pressed()
            # запрещаю выходить за края!
            if player2.rect.x <= 0:
                player2.rect.x = 1
            if player3.rect.x <= 0:
                player3.rect.x = 1
            if player2.rect.x >= 630:
                player2.rect.x = 629
            if player3.rect.x >= 630:
                player3.rect.x = 629
            # игрок
            player2.reset()
            keys = pygame.key.get_pressed()
            # анимации
            if keys[pygame.K_a]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player2.animleft()
            if keys[pygame.K_d]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player2.animright()
            if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                canplaywalksound = True
                shag.stop()
                if player2.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                    player2.image = image
                if player2.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                    player2.image = image
            # ещё анимации
            # ещё анимации
            if keys[pygame.K_a]:
                player3.animright()
            if keys[pygame.K_d]:
                player3.animleft()
            if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                if player3.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2left.png"), (player.width, player.hight))
                    player3.image = image
                if player3.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2right.png"), (player.width, player.hight))
                    player3.image = image
            # действия
            if keys[pygame.K_p]:
                pause = True
            if keys[pygame.K_r]:
                rest(15, 300, 629, 300)
        if currentlvl == 6:    
            # Смена карты
            if currentmap ==7:
                screendark()
                #создание карты
                map = map7
                TitleX = 0
                line = 50
                dietitles.clear()
                doors.clear()
                titles.clear()
                Createmap(map)
                rest(15, 200, 629, 300)
                currentlvl+=1
                pygame.mixer.music.stop()
            # прыжок и движение
            player2.jump()
            player2.move()
            player3.jump()
            player3.move()          
            # колизия
            do_collide(titles)     
            # отрисовка заднего фона
            sky.reset()
            # отрисовка тайтлов 
            do_function2(titles)
            # игрок
            player2.reset()
            player3.reset()
            if player2.rect.y >= 430:
                player2.isdead()
            if player3.rect.y >= 430:
                player3.isdead()
            keys = pygame.key.get_pressed()
            # запрещаю выходить за края!
            if player2.rect.x <= 0:
                player2.rect.x = 1
            if player3.rect.x <= 0:
                player3.rect.x = 1
            if player2.rect.x >= 630:
                player2.rect.x = 629
            if player3.rect.x >= 630:
                player3.rect.x = 629
            # игрок
            player2.reset()
            keys = pygame.key.get_pressed()
            # анимации
            if keys[pygame.K_a]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player2.animleft()
            if keys[pygame.K_d]:
                if canplaywalksound == True:
                    shag.play(-1)
                    canplaywalksound = False
                player2.animright()
            if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                shag.stop()
                canplaywalksound = True
                if player2.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                    player2.image = image
                if player2.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                    player2.image = image
            # ещё анимации
            if keys[pygame.K_a]:
                player3.animright()
            if keys[pygame.K_d]:
                player3.animleft()
            if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                if player3.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2left.png"), (player.width, player.hight))
                    player3.image = image
                if player3.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2right.png"), (player.width, player.hight))
                    player3.image = image
            # действия
            if keys[pygame.K_p]:
                pause = True
            if keys[pygame.K_r]:
                rest(15, 300, 15, 140)
        if currentlvl == 7:    
            # Смена карты
            if currentmap == 8:
                screendark()
                #создание карты
                dietitles.clear()
                doors.clear()
                titles.clear()
                currentlvl = 2
                canplay1 = False
                canplay2 = True
                
            if iscutscene:
                bg = GameSprite("images/cutscene3.png", 0,0,0,700,500, "net")
                bg.reset()
                text = Text(190,30,texts[25], font1, white) 
                text2 = Text(190,90,texts[26], font1, white) 
                text.apear()
                text2.apear()
            else:   
                # колизия с спп
                if pygame.sprite.collide_rect(player2, spp):
                    print(1)
                    iscutscene = True
                    spp.rect.x = -100
                # прыжок и движение
                player2.jump()
                player2.move()
                player3.jump()
                player3.move()          
                # колизия
                do_collide(titles)     
                # отрисовка заднего фона
                sky.reset()
                # отрисовка тайтлов 
                do_function2(titles)
                # игрок
                player2.reset()
                player3.reset()
                if player2.rect.y >= 430:
                    player2.isdead()
                if player3.rect.y >= 430:
                    player3.isdead()
                keys = pygame.key.get_pressed()
                # запрещаю выходить за края!
                if player2.rect.x <= 0:
                    player2.rect.x = 1
                if player3.rect.x <= 0:
                    player3.rect.x = 1
                if player2.rect.x >= 630:
                    player2.rect.x = 629
                if player3.rect.x >= 630:
                    player3.rect.x = 629
                # игрок
                player2.reset()
                keys = pygame.key.get_pressed()
                # псс
                spp.reset()
                # помошь
                if keys[pygame.K_f]:
                    if spp.rect.x == -100:
                        text = Text(20,20,texts[27], font1, white) 
                        text.apear()
                        text2 = Text(20,50,texts[28], font1, white) 
                        text2.apear()
                        
                # анимации
                if keys[pygame.K_a]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player2.animleft()
                if keys[pygame.K_d]:
                    if canplaywalksound == True:
                        shag.play(-1)
                        canplaywalksound = False
                    player2.animright()
                if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                    shag.stop()
                    canplaywalksound = True
                    if player2.naprav == "left":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                        player2.image = image
                    if player2.naprav == "right":
                        image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                        player2.image = image
            # ещё анимации
            # ещё анимации
            if keys[pygame.K_a]:
                player3.animright()
            if keys[pygame.K_d]:
                player3.animleft()
            if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
                if player3.naprav == "left":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2left.png"), (player.width, player.hight))
                    player3.image = image
                if player3.naprav == "right":
                    image = pygame.transform.scale(pygame.image.load("images/player2/player2right.png"), (player.width, player.hight))
                    player3.image = image
            # действия
            if keys[pygame.K_p]:
                pause = True
            if keys[pygame.K_r]:
                rest(15, 200, 629, 300)

        if game2 == True:
            if iscutscene == True:
                bg = GameSprite("images/cutscene4.png", 0, 0, 0, 700, 500, "net")
                bg.reset()
                text = Text(190, 50, "Акула, оно медленая", font2, white)
                text2 = Text(350, 50, "пиранья, быстрая", font2, white)
                text3 = Text(190, 350, "Это бос", font1, white)
                text4 = Text(250, 450, "LKM, Что бы стрелять по рыбам", font1, white)
                text.apear()
                text2.apear()
                text3.apear()
                text4.apear()

            else:
                if najat < 100*dificulty:
                    # текст
                    text = Text(170, 30, "phone, стреляй по ним!", font1, white)
                    
                    # вывод количества подобраного мусора
                    trashtext = Text(20, 20, najat, font1, white)
                    # фон
                    bg = GameSprite("images/bg2.png", 0, 0, 0, 700, 500, "net")
                    bg.reset()
                    # обновление текста
                    text.apear()
                    # мусор
                    if fallgame2stop == False:
                        trash1.fall()
                        trash2.fall()
                        trash3.fall()
                        trash4.fall()
                        trash5.fall()
                        trash6.fall()
                        trash7.fall()
                        trash8.fall()
                        trash9.fall()
                        trash10.fall()
                        trash11.fall()
                    # нажатие на мусор
                    do_function4(trashs)
                    # мусор на экране
                    trash1.reset()
                    trash2.reset()
                    trash3.reset()
                    trash4.reset()
                    trash5.reset()
                    trash6.reset()
                    trash7.reset()
                    trash8.reset()
                    trash9.reset()
                    trash10.reset()
                    trash11.reset()
                    # проигрываешь нсли пропустил много рыб
                    if najat <= -10:
                        losegame2 = True
                    # таймер
                    if losegame2 != True:
                        if done == False:
                            timeset(50)              # изменить если вы не успеваете, оно изменяет время отведёное на уровень.
                        else:
                            done = False
                            losegame2 = True
                    if losegame2 == True:
                        if done == False:
                            timeset(5)
                        else:
                            done = False
                            najat = 0
                            trash1.tel()
                            trash2.tel()
                            trash3.tel()
                            trash4.tel()
                            trash5.tel()
                            trash6.tel()
                            trash7.tel()
                            trash8.tel()
                            trash9.tel()
                            trash10.tel()
                            trash11.tel()
                            trashBIG.rect.y = 0
                            fallgame2stop = False
                            losegame2 = False
                    # прорисовка текста
                    trashtext.apear()
                    # действия
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_p]:
                        pause = True
                    if keys[pygame.K_r]:
                        najat = 0
                        trash1.tel()
                        trash2.tel()
                        trash3.tel()
                        trash4.tel()
                        trash5.tel()
                        trash6.tel()
                        trash7.tel()
                        trash8.tel()
                        trash9.tel()
                        trash10.tel()
                        trash11.tel()
            # бос на 100*dificulty пойманых
            if najat >= 100*dificulty:
                # фон
                bg = GameSprite("images/bg2.png", 0, 0, 0, 700, 500, "net")
                bg.reset()
                # Босс
                if canbigfall == True:
                    trashBIG.fall()
                trashBIG.reset()
                # колизия
                do_function5()
                # действия
                keys = pygame.key.get_pressed()

                if keys[pygame.K_p]:
                    pause = True
                if keys[pygame.K_r]:
                    najat = 0
                    trash1.tel()
                    trash2.tel()
                    trash3.tel()
                    trash4.tel()
                    trash5.tel()
                    trash6.tel()
                    trash7.tel()
                    trash8.tel()
                    trash9.tel()
                    trash10.tel()
                    trash11.tel()
                # таймер
                if losegame2 == True:
                    if done == False:
                        timeset(5)
                    else:
                        done = False
                        najat = 0
                        trash1.tel()
                        trash2.tel()
                        trash3.tel()
                        trash4.tel()
                        trash5.tel()
                        trash6.tel()
                        trash7.tel()
                        trash8.tel()
                        trash9.tel()
                        trash10.tel()
                        trash11.tel()
                        fallgame2stop = False
                        losegame2 = False
                if trashBIG.rect.y >= 700-trashBIG.hight:
                    losegame2 = True
                
            if najat >= 200*dificulty:
                canbigfall = False
                if cansetcurecttime == True:
                    pasttime = timer()
                    cansetcurecttime = False
                currecttime = timer()
                if currecttime-pasttime <= 5:
                    wintext = Text(130, 200, "U win", font3, white)
                    wintext.apear()
                else:
                    canplay2 = False
                    game2 = False
                    screendark()
                    game3 = True
                    currentlvl = 2
                    player.rect.x = 250
                    player.rect.y = 250 
        if game3 == True:
            print(iscutscene)
            if iscutscene:
                bg = GameSprite("images/cutscene5.png", 0, 0, 0, 700, 500, "net")
                bg.reset()
                text0 = Text(200, 30, "Crab, при косании отнимает hp", font2, white)
                text0.apear()
                text1 = Text(400, 200, "Магазин, при косании пополняет поезапас", font2, white)
                text1.apear()
                text2 = Text(430, 400, "F, что бы стрелять", font2, white)
                text2.apear()
            else:
                
                print(iscutscene)
                bulletcount = GameSprite("images/bullettop.png", 500, 410, 0, 20, 20, "net")
                crableft = GameSprite("images/leftcrab.png", 300, 410, 0, 40, 40, "net")
                manuhp = GameSprite("images/hearth.png", 100, 410, 0, 40, 40, "net")
                surface = pygame.Surface([700, 200], pygame.SRCALPHA, 32)
                surface = surface.convert_alpha()
                surface.fill((0, 0, 0, 180))
                # вешь
                thing= GameSprite("images/something.png", 300, 370, 0, 70, 70, "net")
                # текст
                ulose = Text(180, 230, "U lose, r to restart", font1, white)
                howmanybullets = Text(450, 410, bulletscount, font1, white)
                howmanyhp = Text(50, 410, hp, font1, white)
                howmanycrab = Text(250, 410, killcount, font1, white)
                # фон 
                bg = GameSprite("images/floor_2.png", 0, 0, 0, 700, 500, "net")
                # отрисофка фона
                bg.reset()
                # подсказка
                text = Text(30, 30, "phone: ВОН МОё сокровище, убей всех крабов и забери его 'space'", font2, white)
                text.apear()
                # пули - летать
                if stopgame != True:
                    for bulet in bullets:
                        bulet.fly()
                        bulet.reset()
                # отрисовка вещи
                thing.reset()
                # бонус
                if killcount > 14:
                    if canpickupclip == True:
                        clip = GameSprite("images/clip.png", randint(1, 700), randint(1, 500), 0, 20, 20, "net")
                        canpickupclip = False
                    clip.reset()
                    if pygame.sprite.collide_rect(player, clip):
                        bulletscount = 10
                        clip.rect.x = -100

                # игрок
                player.reset()
                keys = pygame.key.get_pressed()
                if stopgame != True:
                    # передвижение
                    if keys[pygame.K_s]and player.rect.y<=500-player.hight:
                        player.naprav = "down"
                        player.rect.y+=player.speed
                    if keys[pygame.K_w]and player.rect.y>=0:
                        player.naprav = "top"
                        player.rect.y-=player.speed
                    if keys[pygame.K_a]and player.rect.x>=0:
                        player.naprav = "left"
                        player.rect.x-=player.speed
                    if keys[pygame.K_d]and player.rect.x <= 700-player.width:
                        player.naprav = "right"
                        player.rect.x+=player.speed
                    # отрисовка и методы enemy
                    for enemy in enemys:
                        if pygame.sprite.collide_rect(player, enemy):
                            hp -= 1
                            if canspawn == True:
                                enemy.tel()
                            else:
                                enemys.remove(enemy)
                        enemy.run()
                        enemy.anim()
                        enemy.reset()
                    for enemy in enemys:
                        for bullet in bullets:
                            if pygame.sprite.collide_rect(bullet, enemy):
                                if canspawn == True:
                                    enemy.tel()
                                    killcount +=1
                                else:
                                    enemys.remove(enemy)
                    # отрисовка меню
                    win.blit(surface, (0, 400))
                    bulletcount.reset()
                    manuhp.reset()
                    crableft.reset()
                    howmanybullets.apear()
                    howmanyhp.apear()
                    howmanycrab.apear()
                    # возможность поднять объект
                    if pygame.sprite.collide_rect(player, thing):
                        if keys[pygame.K_SPACE]:
                            if cancarrysomething == True:
                                gameend = True
                            else:
                                pass

                    # анимации
                    if keys[pygame.K_s]:
                        player.animdown()
                    if keys[pygame.K_w]:
                        player.animtop()
                    if keys[pygame.K_a]:
                        player.animleft()
                    if keys[pygame.K_d]:
                        player.animright()
                    if keys[pygame.K_d] != True and keys[pygame.K_w] != True and keys[pygame.K_a] != True and keys[pygame.K_s] != True:
                        if player.naprav == "down":
                            image = pygame.transform.scale(pygame.image.load("images/player/player1.png"), (player.width, player.hight))
                            player.image = image
                        if player.naprav == "top":
                            image = pygame.transform.scale(pygame.image.load("images/player/playertop.png"), (player.width, player.hight))
                            player.image = image
                        if player.naprav == "left":
                            image = pygame.transform.scale(pygame.image.load("images/player/playerleft.png"), (player.width, player.hight))
                            player.image = image
                        if player.naprav == "right":
                            image = pygame.transform.scale(pygame.image.load("images/player/playerright.png"), (player.width, player.hight))
                            player.image = image
                    print(iscutscene)

                # проигрышь
                if hp <=0:
                    stopgame = True
                    # отрисовка текста
                    ulose.apear()
                    # рест
                    if keys[pygame.K_r]:
                        player.rect.x = 250
                        player.rect.y = 250
                        for enemy in enemys:
                            enemy.tel()
                        stopgame = False
                        hp = 3
                        bullets.clear()
                        killcount = 0
                        cansetcurecttime = True
                if killcount >= 35*dificulty:
                    cancarrysomething = True
                    canspawn = False
                # действия
                if keys[pygame.K_p]:
                    pause = True
            if gameend == True:
                bg = GameSprite("images/plate_3", 0, 0, 0, 700, 500, "net")
                bg.reset()
                currentlvl = -2
                game2=False
                game3=False
    # Обновление дисплея и фпс
    pygame.display.update()
    clock.tick(fps)

    # пауза
    keys = pygame.key.get_pressed()
    if keys[pygame.K_u]:
        pause = False
