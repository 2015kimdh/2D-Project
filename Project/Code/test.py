from pico2d import *

sound = None
sound = load_music('50 Cal Machine Gun-SoundBible.com-305222493.mp3')


def sound_(self, n = 1):
    Mix_PlayMusic(self.sound, n)

sound_