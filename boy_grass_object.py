from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자를 이용해서 객체의 초기 상태를 정의상태 정의
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(10, 200), 90
        self.frame= 0
        self.image = load_image('run_animation.png')

    def update(self):
        #self.frame = (self.frame + 1 ) % 8
        self.frame = random.randint(0,7)
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    pass

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0,700), 599
        self.speed = random.randint(5, 15)
        self.image = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')
        self.i = random.randint(0, 1)

    def update(self):
        if self.y >=71 and self.i == 1:
            self.y -= self.speed
        elif self.y >=61 and self.i == 0:
            self.y -= self.speed
    def draw(self):
        if self.i == 0:
            self.image.draw(self.x,self.y)
        else:
            self.image2.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def reset_world():
    global running
    global grass
    global boy
    global team
    global ball
    global world


    running = True
    world = []
    grass = Grass() # Grass 클래스를 이용해서 grass 객체를 생성
    world.append(grass)
    ball = [Ball() for i in range(20)]
    team = [Boy() for i in range(10)]
    world += team
    world += ball

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
