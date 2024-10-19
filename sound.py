import pygame.mixer

pygame.mixer.init()

def play_sound(path, vol = 1.0):
    sound = pygame.mixer.Sound(path)
    sound.set_volume(vol)
    sound.play()