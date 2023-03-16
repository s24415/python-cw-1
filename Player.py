import pygame

file = 'songs/Highway_to_Hell.mp3'
pygame.init()
pygame.mixer.init()

music = pygame.mixer.music
music.load(file)
music.play()

while music.get_busy():
    pygame.time.Clock().tick(100)