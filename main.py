import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()
ORIGIN_X_SIZE = 128
ORIGIN_Y_SIZE = 128
SCALE = 6
SURFACE_X_SIZE = ORIGIN_X_SIZE * SCALE
SURFACE_Y_SIZE = ORIGIN_Y_SIZE * SCALE
SURFACE = pygame.display.set_mode((SURFACE_X_SIZE, SURFACE_Y_SIZE))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("PixelArt_LootChest")

# クラス: チェスト
class Chest:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.pos = pos
        self.theta = 0
    
    # status = "standby"時に実行
    def standby(self):
        global process
        global status
        max_process = 100
        if 0 <= process % max_process < 8:
            self.theta -= 5
        if 8 <= process % max_process < 24:
            self.theta += 5
        if 24 <= process % max_process < 40:
            self.theta -= 5
        if 40 <= process % max_process < 48:
            self.theta += 5
        if process % max_process == max_process - 1:
            status = "empty"

        self.new_image = pygame.transform.rotate(self.image, self.theta)
        #self.new_image = pygame.transform.scale_by(self.new_image, SCALE)
        self.rect = self.new_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])

    # 毎tick実行
    def tick(self):
        global status
        if status == "standby":
            self.standby()

    # 描画を更新
    def draw(self):
        SURFACE.blit(self.new_image, self.rect)


status = "standby"
process = 0
def main():

    global status
    global process
    next_status = " "
    chest = Chest((SURFACE_X_SIZE / 2, SURFACE_Y_SIZE / 2), "./image/chest.png")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.dict["button"] == 3:
                    #pygame.quit()
                    #sys.exit()
                    next_status = "standby"
                else:
                    next_status = "open"
        
        chest.tick()
        SURFACE.fill((255, 255, 255))
        chest.draw()
        #print(f"status={status}, next_status={next_status}")
        if next_status == " ":
            next_status = "standby"
        if status == "empty":
            process = -1
            status = next_status

        if process % 1000 == 0 and status == "open":
            status = "empty"

        process += 1
        pygame.display.update()
        FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()

"""
N = 0
N = N + 3286
N = N * 4736
N = N % 12312
print(N)
"""