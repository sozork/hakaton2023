#импортируем библиотеки
import pygame
from random import randint
from time import time as timer
pygame.init()
#создаём классы
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
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
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if titles[0].rect.x <=300:
                self.rect.x += self.speed
        if keys[pygame.K_d]:
            if titles[8].rect.x >=300:
                self.rect.x -= self.speed
        if keys[pygame.K_w]:
            if titles[0].rect.y <=180:
                self.rect.y += self.speed
        if keys[pygame.K_s]:
            if titles[len(titles)-5].rect.y >230:
                self.rect.y -= self.speed
    def move2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if titles[0].rect.x <=300:
                self.rect.x += self.speed
        if keys[pygame.K_d]:
            if titles[14].rect.x >=300:
                self.rect.x -= self.speed
        if keys[pygame.K_w]:
            if titles[14].rect.y <=180:
                self.rect.y += self.speed
        if keys[pygame.K_s]:
            if titles[len(titles)-1].rect.y >230:
                self.rect.y -= self.speed
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
# класс игрока
class Player(GameSprite):
    
    def animcr(self):
        
        self.spritesleft = []
        self.spritesright = []
        self.spritestop = []
        self.spritesdown = []
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown2.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown3.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]

    def animdown(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animtop(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animright(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animleft(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]

    def move(self):
        self.rect = pygame.rect.Rect(self.rect.x, self.rect.y, self.width,self.hight)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed 
        
    def jump(self):
        if self.die == False:
            global jumpspeed
            global is_jump
            global canfall
            if is_jump != False:
                if jumpspeed >= -startjumpspeed+1:
                    if jumpspeed > 0:
                        self.rect.y -= (jumpspeed ** 2) / 2
                    else:
                        if canfall == True:
                            self.rect.y += (jumpspeed ** 2) / 2-3
                    jumpspeed -= 1
                else:
                    canfall = True
                    jumpspeed = startjumpspeed    
                    is_jump = False 
            
    def isdead(self):
        self.speed = 0
        self.image = pygame.image.load("images/nothing.png")
        self.die = True
class Player2(GameSprite):
    
    def animcr(self):
        self.spritesleft = []
        self.spritesright = []
        self.spritestop = []
        self.spritesdown = []
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown2.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        image = pygame.transform.scale(pygame.image.load("images/player/playerdown3.png"), (self.width, self.hight))
        self.spritesdown.append(image)
        self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]

    def animdown(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animtop(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animright(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]
    def animleft(self):
        self.current_sprite += 0.1
        if self.current_sprite >=2:
            self.current_sprite = 0
        self.image = self.spritesdown[int(self.current_sprite)]

    def move(self):
        self.rect = pygame.rect.Rect(self.rect.x, self.rect.y, self.width,self.hight)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x += self.speed
        if keys[pygame.K_d]:
            self.rect.x -= self.speed 
    
    def jump(self):
        if self.die == False:
            global jumpspeed2
            global is_jump2
            global canfall2
            if is_jump2 != False:
                if jumpspeed2 >= -startjumpspeed2+1:
                    if jumpspeed2 > 0:
                        self.rect.y -= (jumpspeed2 ** 2) / 2
                    else:
                        if canfall2 == True:
                            self.rect.y += (jumpspeed ** 2) / 2-3
                    jumpspeed2 -= 1
                else:
                    canfall2 = True
                    jumpspeed2 = startjumpspeed2    
                    is_jump2 = False 
            
    def isdead(self):
        self.speed = 0
        self.image = pygame.image.load("images/nothing.png")
        self.die = True
# класс мусора
class Trash(GameSprite):
    def tel(self):
        self.rect.x = randint(10, 700-self.width) 
        self.rect.y = 10
        self.speed = randint(1,6)
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
    def apear(self):
        self.word = self.font.render(str(self.text), True, self.color)
        win.blit(self.word, (self.x, self.y))
# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# назначаю шрифты
pygame.font.init()
font1 = pygame.font.Font(None, 70)
font2 = pygame.font.Font(None, 200)
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
currentlvl = 0
currentmap = 0
canplay1 = True
canplay2 = True
game2 = False
losegame2 = False
fallgame2stop = False
canbigfall = True
cansetcurecttime = True
# разные карты
map1 ="aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa/"
map2 = "aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa//aaaaaaaaaaaaaaa/"
map3 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnndnnnnn/nnnnnnsnnnnnnnn/ppnnppppnpnnnnnnn/"
map4 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/dnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/pppnnnnnnnnnnnn/nnnnnnnnnsnnnnn/nnnnppppnpnnnnnnn/"
map5 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnndnnnnnnnnn/nnnnnnnnnnnnnnn/pppnpppnnpnnnnnnn/"
map6 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/pppppppnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnndnnnnn/nnnnnnnnnnnnnnn/ppnnpppnnpnnnnnnn/"
map7 = "nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/nnnnnnnnnnnnnnnn/pnnnndnnnnnnnnn/nnnnnnnnnnnnnn/nppnppnnppnnnnn/"
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

# создаю 1 уровень
cave_1 = GameSprite("images/cave_1.png", 500, 130, 5, 70, 70)        
# создаю карту
map ="fffffffff//fffffffff//fffffffff//fffffffff//fffffffff//fffffffff//fffffffff"
TitleX = 0
line = 0
titles.clear()
#  фон
sky = GameSprite("images/sky.jpg", 0, 0, 0, 700, 500)
# идёт загрузка подождите
print("!!!Идёт загрузка подождите!!!")
# Функция для создания карты
def Createmap(map):
    global TitleX
    global line
    for word in map:
        if word == "w":
            wall = GameSprite("images/wall.png", TitleX, line, 5, 70, 70)
            titles.append(wall)
            TitleX += 70
        if word == "/":
            line += 32
            TitleX = 0
        if word == "a":
            i = randint(1, 5)
            floor = GameSprite("images/floor_"+str(i) + ".png", TitleX, line, 5, 70, 70)
            titles.append(floor)
            TitleX += 70
        if word == "p":
            plate = GameSprite("images/plate_1.png", TitleX, line, 10, 64, 26)
            titles.append(plate)
            TitleX += 70
        if word == "n":
            TitleX += 70
        if word == "s":
            spike = GameSprite("images/spikes.png", TitleX, line, 0, 50, 32)
            titles.append(spike)
            dietitles.append(spike)
            TitleX += 70
        if word == "d":
            door= GameSprite("images/spikes.png", TitleX, line, 0, 70, 70)
            titles.append(door)
            doors.append(door)
            TitleX += 70
        if word == "f":
            i = randint(1, 5)
            floor = GameSprite("images/planks_"+str(i) + ".png", TitleX, line, 5, 70, 70)
            titles.append(floor)
            TitleX += 70
Createmap(map)
# объекты для 1 уровня
bed = GameSprite("images/bed.png", 80, 0, 5, 64, 100)
titles.append(bed)
stend = GameSprite("images/stend.png", 250, 0, 5, 100, 100)
titles.append(stend)
table = GameSprite("images/table.png", 50, 300, 5, 120, 80)
titles.append(table)
cover = GameSprite("images/cover.png", 320, 300, 5, 238, 138)
titles.append(cover)
# количество нажатий на мусор
najat = 0
# Фунуция рестарта
def rest(x, y, x2, y2):
    global player2
    global player3
    player2.die = False
    player3.die = False
    player2 = Player("images/player/playerdown1.png", x, y, 10, 70, 70)
    player2.animcr()
    player3 = Player2("images/player/playerdown1.png", x2, y2, 10, 70, 70)
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
player = Player("images/player/playerdown1.png", 300, 200, 5, 70, 70)
player.animcr()
# создаю игрока для платформ
player2 = Player("images/player/playerdown1.png", 15, 300, 10, 70, 70)    

player3 = Player2("images/player/playerdown1.png", 310, 300, 10, 70, 70)   
# "мусор"
trash1 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash2 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash3 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash4 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash5 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash6 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash7 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash8 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash9 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash10 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
trash11 = Trash("images/player/playerdown1.png", randint(10, 700-60), 10, randint(1, 5), 60, 60)
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
trashBIG = Trash("images/player/playerdown1.png", 200, 10, 2, 200, 200)
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
            losetext = Text(130, 200, "U lose", font2, black)
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
                if pygame.sprite.collide_rect(player, cave_1):
                    if i.key == pygame.K_SPACE:
                        currentmap +=1
    if pause == False:
        if currentlvl == 0:
            # Смена карты
            if currentmap == 1:
                screendark()
                #создание карты
                map = map1
                TitleX = 0
                line = 50
                titles.clear()
                Createmap(map)
                cave_1.rect.x = 900
                currentlvl +=1
            # отрисовка тайтлов
            do_function3(titles)
            # уровни
            cave_1.move()
            cave_1.reset()
            # игрок
            player.reset()
            keys = pygame.key.get_pressed()
            # анимации
            if keys[pygame.K_s]:
                player.animdown()
            else:
                image = pygame.transform.scale(pygame.image.load("images/player/playerdown1.png"), (player.width, player.hight))
                player.image = image
            # действия
            if keys[pygame.K_p]:
                pause = True
        if currentlvl == 1:
            # Смена карты
            if currentmap == 2:
                screendark()
                #создание карты
                player.rect.x = 0
                currentlvl +=1
            # отрисовка тайтлов
            do_function(titles)
            # уровни
            cave_1.move2()
            cave_1.reset()
            # игрок
            player.reset()
            keys = pygame.key.get_pressed()
            # анимации
            if keys[pygame.K_a]:
                player.animleft()
            if keys[pygame.K_d]:
                player.animright()
            if keys[pygame.K_w]:
                player.animtop()
            if keys[pygame.K_s]:
                player.animdown()
            # действия
            if keys[pygame.K_p]:
                pause = True
            # все остальные объекты классов
        if currentlvl == 2:   
            # создаю иконки игр
            plate = GameSprite("images/plate_1.png", 100, 100, 10, 150, 150)
            plate2 = GameSprite("images/plate_1.png", 450, 100, 10, 150, 150)
            # Смена карты
            if currentmap == 3:
                screendark()
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
            # отрисовка окон
            plate.reset()
            plate2.reset()
            # нажатие мыши
            pressed = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            # НАЖАЛИ ЛИ НА КНОПКУ УРОВНЯ?
            if plate.rect.collidepoint(pos):
                print(pos, plate.rect.x, plate.rect.y)
                if pressed[0] == True:
                    if canplay1 == True:
                        currentmap = 3
            if plate2.rect.collidepoint(pos):
                print(pos, plate2.rect.x, plate2.rect.y)
                if pressed[0] == True:
                    if canplay2 == True:
                        canplay1 = False
                        game2 = True
            
        if currentlvl == 3:    
            # Смена карты
            if currentmap == 4:
                screendark()
                #создание карты
                map = map4
                TitleX = 0
                line = 50
                titles.clear()
                dietitles.clear()
                doors.clear()
                Createmap(map)
                rest(310, 300, 500, 300)
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
            # анимации
            if keys[pygame.K_a]:
                player2.animleft()
            if keys[pygame.K_d]:
                player2.animright()
            if keys[pygame.K_s]:
                player2.animdown()
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
            # анимации
            if keys[pygame.K_a]:
                player2.animleft()
            if keys[pygame.K_d]:
                player2.animright()
            if keys[pygame.K_s]:
                player2.animdown()
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
            # анимации
            if keys[pygame.K_a]:
                player2.animleft()
            if keys[pygame.K_d]:
                player2.animright()
            if keys[pygame.K_s]:
                player2.animdown()
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
            # анимации
            if keys[pygame.K_a]:
                player2.animleft()
            if keys[pygame.K_d]:
                player2.animright()
            if keys[pygame.K_s]:
                player2.animdown()
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
            # анимации
            if keys[pygame.K_a]:
                player2.animleft()
            if keys[pygame.K_d]:
                player2.animright()
            if keys[pygame.K_s]:
                player2.animdown()
            # действия
            if keys[pygame.K_p]:
                pause = True
            if keys[pygame.K_r]:
                rest(15, 200, 629, 300)

        if game2 == True:
            if najat < 10:
                # вывод количества подобраного мусора
                trashtext = Text(20, 20, najat, font1, black)
                # фон
                bg = GameSprite("images/bg2.png", 0, 0, 0, 700, 500)
                bg.reset()
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
            # бос на 100 пойманых
            if najat >= 10:
                # фон
                bg = GameSprite("images/bg2.png", 0, 0, 0, 700, 500)
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
                
            if najat >= 100:
                canbigfall = False
                if cansetcurecttime == True:
                    pasttime = timer()
                    cansetcurecttime = False
                currecttime = timer()
                if currecttime-pasttime <= 5:
                    wintext = Text(130, 200, "U win", font2, black)
                    wintext.apear()
                else:
                    canplay2 = False
                    game2 = False
                    screendark()
                    currentlvl = 2
                    

    # Обновление дисплея и фпс
    pygame.display.update()
    clock.tick(fps)
    # пауза
    keys = pygame.key.get_pressed()
    if keys[pygame.K_u]:
        pause = False
