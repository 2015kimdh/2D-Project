import game_framework
import main_state
from pico2d import *
from bullet import P_Bullet
from missile import P_missile
from sky import Sky

import random
import game_world


# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.6) # 10 pix 60cm
FLY_SPEED_KMPH = 120.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)
FLY_UP_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, PULLUP_DOWN, PULLUP_UP, PUSHDOWN_DOWN, PUSHDOWN_UP, SLEEP_TIMER, BULLET_UP, BULLET_DOWN, MISSILE_DOWN, MAP_CHANGE, RECT_ON = range(14)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_z): BULLET_UP,
    (SDL_KEYDOWN, SDLK_z): BULLET_DOWN,
    (SDL_KEYDOWN, SDLK_UP): PULLUP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): PUSHDOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): PULLUP_UP,
    (SDL_KEYUP, SDLK_DOWN): PUSHDOWN_UP,
    (SDL_KEYDOWN, SDLK_x): MISSILE_DOWN,
    (SDL_KEYDOWN, SDLK_q): MAP_CHANGE,
    (SDL_KEYDOWN, SDLK_t): RECT_ON
}


# Boy States


class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += FLY_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= FLY_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= FLY_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += FLY_SPEED_PPS

        if event == PULLUP_DOWN:
            player.altitude += FLY_UP_SPEED_PPS
        elif event == PUSHDOWN_DOWN:
            player.altitude -= FLY_UP_SPEED_PPS
        elif event == PULLUP_UP:
            player.altitude -= FLY_UP_SPEED_PPS
        elif event == PUSHDOWN_UP:
            player.altitude += FLY_UP_SPEED_PPS

        if event == BULLET_DOWN:
            player.armed = 1
        elif event == BULLET_UP:
            player.armed = 0
        if event == MISSILE_DOWN:
            player.player_fire_missile()
        if event == RECT_ON:
            if player.rect == 0:
                player.rect = 1
            else :
                player.rect = 0
        if event == MAP_CHANGE:
            player.map_change()

        player.dir = 1


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if player.velocity > 0:
            if player.x < 1550 - player.velocity * game_framework.frame_time:
                player.x += player.velocity * game_framework.frame_time
        if player.velocity < 0:
            if player.x > 50 + player.velocity * game_framework.frame_time:
                player.x += player.velocity * game_framework.frame_time

        if player.altitude > 0:
            if player.y < 780 - player.velocity * game_framework.frame_time:
                player.y += player.altitude * game_framework.frame_time
        if player.altitude < 0:
            if player.y > 30 + player.altitude * game_framework.frame_time:
                player.y += player.altitude * game_framework.frame_time

        player.shottime += (FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) * 3
        if player.armed == 1 and int(player.shottime % 4) == 0:
            player.player_fire_bullet()

    @staticmethod
    def draw(player):
            player.image.clip_draw(0, int(player.frame) * 85, 370, 85, player.x, player.y, 185, 42.5)
            if player.rect == 0:
                draw_rectangle(*player.get_bb())


next_state_table = {
    RunState: {PUSHDOWN_DOWN : RunState, PUSHDOWN_UP : RunState, PULLUP_DOWN : RunState, PULLUP_UP : RunState, RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState,
               RIGHT_DOWN: RunState, BULLET_DOWN: RunState, BULLET_UP: RunState, MISSILE_DOWN: RunState,
               MAP_CHANGE : RunState, RECT_ON : RunState}}

class Player:

    def __init__(self):
        self.x, self.y = 0+150, 800 / 2
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('jet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.altitude = 0
        self.armed = 0
        self.frame = 0
        self.shottime = 0
        self.sound = load_wav('50CalMachineGun.wav')
        self.missile_sound = load_wav('Grenade.wav')
        self.bullet_load = 0.015
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.angle = 0
        self.sound.set_volume(10)
        self.missile_sound.set_volume(30)
        self.state = 0
        self.rect = 0

    def map_change(self):
        for sky in game_world.get_sky():
            if sky.night == 0:
                sky.night = 1
            elif sky.night == 1:
                sky.night = 0


    def player_fire_bullet(self):
        bullet = P_Bullet(self.x, self.y, self.dir*15)
        #main_state.pbullet = P_Bullet(self.x, self.y, self.dir*15)
        game_world.add_object(bullet, 1)
        self.sound.play()


    def player_fire_missile(self):
        pmissile = P_missile(self.x, self.y)
        game_world.add_object(pmissile, 1)
        self.missile_sound.play()

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - PIXEL_PER_METER*1, self.y - PIXEL_PER_METER*1.0, self.x + PIXEL_PER_METER*2, self.y + PIXEL_PER_METER*0.5