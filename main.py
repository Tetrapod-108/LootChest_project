import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, K_SPACE

import global_variable as g
import classes

pygame.init()
pygame.display.set_caption("PixelArt_LootChest")

def main():

    background = classes.Background((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2), "./image/background.png")
    chest = classes.Chest([g.SURFACE_X_SIZE / 2, -100], "./image/chest.png")
    flash = classes.Flash((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2), "image/flash.png")
    freeze = classes.Freeze((g.SURFACE_X_SIZE / 2, g.SURFACE_Y_SIZE / 2), "image/freeze.png")

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
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if g.status == "empty":
                        g.next_status = "drop"

        background.tick()
        chest.tick()
        flash.tick()
        freeze.tick()

        background.draw()
        chest.draw()
        flash.draw()
        freeze.draw()

        #print(f"g.status={g.status}, g.next_status={g.next_status}")
        if g.status == "empty":
            g.process = -1
            g.status = g.next_status
            if g.next_status == "standby":
                g.next_status = "standby"
            else:
                g.next_status = "empty"

        g.process += 1
        pygame.display.update()
        g.FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()