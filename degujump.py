import os, pygame, random, time
from pygame.locals import *
from pygame.compat import geterror

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')
screen_width = 800
screen_height = 400
spawn_time = 1
Clock = pygame.time.Clock()
def image(name, colorkey = None):
    #image load stuff here
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ("cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def sound(name):
    #sound load stuff here
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ("Cannot load sound: %s" % fullname)
        raise SystemExit(str(geterror()))
    return sound

class Degu(pygame.sprite.Sprite):
    #degu stuff here, jump, collission, animation
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = image('degurest.png', -1)
        screen = pygame.display.get_surface()
        #self.area = screen.get_rect()
        self.rect.topleft = 10, 400
        self.change_x = 0
        self.change_y = 0
        self.power_y = 0
    def update(self):
        self.gravity()
        #self.power()
        #self.rect.x += self.change_x
        self.rect.y += self.change_y
        #self.rect.y += self.power_y


    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1
        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_height - self.rect.height

        #if self.rect.y < 350:
        #    self.change_y = -9
        #elif self.rect.y == 350:
    #        self.change_y = 0



    def power(self):
        if self.rect.y <= 150:
            self.power_y = 0
        else:
            pass

    def jump(self):
        #self.rect.y += 2
        #self.rect.y -= 2
        if self.rect.bottom >= 390:
            
            self.change_y = -24


        else:
            pass
        #if self.rect.y >= 350:
        #    self.power_y = -18
    def dead(self):
        self.image = pygame.transform.rotate(self.image, 180)
        pygame.time.wait(500)








class Pipe(pygame.sprite.Sprite):
    def __init__(self, screen, height):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load('Pipe.png')
        #self.image = pygame.transform.scale(image, (100, 100))
        #self.rect = image.get_rect()
        self.image, self.rect = image('pipe.png', -1)
        self.image = pygame.transform.scale(self.image, (50, 210))
        screen = pygame.display.get_surface()
        #self.area = screen.get_rect()
        self.rect.topleft = 770, height
        self.change_x = 0
    def update(self):
        self.rect.x -= 6.5



def score():
    #score stuff here
    pass

def menu():
    # start menu here
    pass

def tube():
    #tubes and random sizing here
    pass

def main():
    #main game loop here
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Degu Jump")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))


    screen.blit(background, (0, 0))
    pygame.display.flip()

    degu = Degu()
    #pipe = Pipe()
    pipelist = pygame.sprite.Group()
    #now = pygame.time.get_ticks()
    #time_difference = pygame.time.get_ticks() - now
    clock = pygame.time.Clock()

    timer = 0
    #x = 0

    ##pipes = [ {'x': pipe, 'y': pipe2} ]
    #pipe3 = Pipe()
    #pipe4 = Pipe()
    degusprites = pygame.sprite.RenderPlain((degu))
    #pipesprites = pygame.sprite.RenderPlain((pipe))
    running = True
    #starttime = time.time()
    while running:
        Clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    degu.jump()

                    #if x < 1:
                    #    pipelist.add(Pipe(screen, random.randint(200, 290)))
                    #    x += 1



        #for pipe in pipes:
        #    pipe['x'].move()
    #    if 0 < pipes[0]['x'] < 5:
    #        newPipe = Pipe()
    #        pipes.append(newPipe[0])
        # attempt to remove pipes from list
        #if pipes[0]['x'] <

        #pipe.move()
# Here is the good stuff
        timer += 1
        if timer >= random.randint(45, 65):
            pipelist.add(Pipe(screen, random.randint(270, 380)))
            timer = 0


        pipelist.update()
        degusprites.update()
        #pipesprites.update()

        screen.blit(background, (0, 0))
        degusprites.draw(screen)
        pipelist.draw(screen)
        hit = pygame.sprite.spritecollide(degu, pipelist, False)
        if hit:

            degu.dead()
            # needs work to update to flipped and land at game over menu







        #pipesprites.draw(screen)

        pygame.display.flip()
        # Testing Branch














    pygame.quit()

if __name__ == '__main__':
    main()
