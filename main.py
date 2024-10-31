import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, K_SPACE, K_r

import global_variable as g
import classes
import lottery
import sound as s

pygame.init()
pygame.display.set_caption("PixelArt_LootChest")

def main():

    background = classes.Background((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2), "./image/background.png")
    chest = classes.Chest([g.SURFACE_X_SIZE / 2, -100], "./image/chest.png")
    flash = classes.Flash((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2), "image/flash.png")
    freeze = classes.Freeze((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2), "image/freeze.png")
    display = classes.Display((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2))
    title = classes.Title((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2), "image/title.png")

    lottery_result = " "

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.dict["button"] == 3:
                    g.next_status = "freeze"
                else:
                    if g.status == "standby":
                        g.next_status = "zoom"
                    if g.status == "gold_standby":
                        g.next_status = "zoom"
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if g.status == "opening":
                        s.play_sound("sound/select.mp3", 1.0)
                        g.status = "empty"
                        lottery_result = lottery.lottery()
                        g.next_status = "drop"
                if event.key == K_r:
                    if g.status == "result":
                        g.status = "empty"
                        g.next_status = "opening"

        background.tick()
        chest.tick()
        flash.tick()
        freeze.tick()
        title.tick()
        display.tick(lottery_result)

        background.draw()
        chest.draw()
        flash.draw()
        freeze.draw()
        title.draw()
        display.draw()

        #print(f"g.status={g.status}, g.next_status={g.next_status}")
        if g.status == "empty":
            g.process = -1
            g.status = g.next_status
            if g.next_status == "standby":
                g.next_status = "standby"
            elif g.next_status == "gold_standby":
                g.next_status = "gold_standby"
            else:
                g.next_status = "empty"

        g.process += 1
        pygame.display.update()
        g.FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()