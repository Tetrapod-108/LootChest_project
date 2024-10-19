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




# クラス: 背景
class Background:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.pos = pos
        self.scale = 1.0
    
    # status = "standby"時に実行
    def standby(self):
        global process
        global status

    # status = "zoom"時に実行
    def zoom(self):
        global process
        global status
        global next_status
        max_process = 90
        if 0 <= process % max_process < 2:
            offset = 0.3
        if 2 <= process % max_process < 3:
            offset = 0.2
        if 3 <= process % max_process < 5:
            offset = 0.1
        if 5 <= process % max_process < max_process:
            offset = 0
        self.scale = self.scale + offset
        if process % max_process == max_process - 1:
            status = "empty"
            next_status = "open"

    # 毎tick実行
    def tick(self):
        global status
        if status == "standby":
            self.standby()
        if status == "zoom":
            self.zoom()
    
    # 描画を更新
    def draw(self):
        self.new_image = pygame.transform.scale_by(self.image, self.scale)
        self.rect = self.new_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        SURFACE.blit(self.new_image, self.rect)


# クラス: チェスト
class Chest:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.new_image = pygame.image.load(path)
        self.pos = pos
        self.theta = 0
        self.scale = 1.0
    
    # status = "standby"時に実行
    def standby(self):
        global process
        global status
        global next_status
        max_process = 100
        if 0 <= process % max_process < 4:
            self.theta -= 3
        if 4 <= process % max_process < 12:
            self.theta += 3
        if 12 <= process % max_process < 20:
            self.theta -= 3
        if 20 <= process % max_process < 24:
            self.theta += 3
        if 24 <= process % max_process < max_process:
            if next_status != "standby":
                status = "empty"
        if process % max_process == max_process - 1:
            status = "empty"
        self.new_image = pygame.transform.rotate(self.image, self.theta)

    # status = "zoom"時に実行
    def zoom(self):
        global process
        global status
        global next_status
        max_process = 90
        if 0 <= process % max_process < 2:
            offset = 0.3
        if 2 <= process % max_process < 3:
            offset = 0.2
        if 3 <= process % max_process < 5:
            offset = 0.1
        if 5 <= process % max_process < max_process:
            offset = 0
        self.scale = self.scale + offset
        
    # status = "open"時に実行
    def open(self):
        global process
        global status
        global next_status
        max_process = 24
        if 0 <= process % max_process < 4:
            self.new_image = pygame.image.load("image/chest_frame2.png")
        if 4 <= process % max_process < 8:
            self.new_image = pygame.image.load("image/chest_frame3.png")
        if 12 <= process % max_process < 16:
            self.new_image = pygame.image.load("image/chest_frame4.png")
        if process % max_process == max_process - 1:
            status = "empty"
            next_status = "result"

    # 毎tick実行
    def tick(self):
        global status
        if status == "standby":
            self.standby()
        if status == "open":
            self.open()
        if status == "zoom":
            self.zoom()

    # 描画を更新
    def draw(self):
        after_zoom_image = pygame.transform.scale_by(self.new_image, self.scale)
        self.rect = after_zoom_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        SURFACE.blit(after_zoom_image, self.rect)



# クラス: フラッシュ
class Flash:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.new_image = pygame.image.load(path)
        self.pos = pos
        self.theta = 0
        self.scale = 2.0
    
    # status = "result"時に実行
    def result(self):
        self.theta += 1
        self.new_image = pygame.transform.rotate(self.image, self.theta)

    # 毎tick実行
    def tick(self):
        global status
        if status == "result":
            self.result()

    # 描画を更新
    def draw(self):
        global status
        after_zoom_image = pygame.transform.scale_by(self.new_image, self.scale)
        self.rect = after_zoom_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        if status == "result":
            SURFACE.blit(after_zoom_image, self.rect)



# クラス: フリーズ
class Freeze:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.new_image = pygame.image.load(path)
        self.pos = pos
        self.theta = 0
        self.scale = 1.0
    
    # status = "freeze"時に実行
    def freeze(self):
        global process
        global status
        global next_status
        max_process = 90
        if 0 <= process % max_process < 4:
            self.new_image = pygame.image.load("image/freeze_frame3.png")
        if 4 <= process % max_process < 8:
            self.new_image = pygame.image.load("image/freeze_frame2.png")
        if 12 <= process % max_process < 16:
            self.new_image = pygame.image.load("image/freeze.png")
        if 16 <= process % max_process < max_process:
            self.new_image = pygame.image.load("image/freeze_frame3.png")
        if process % max_process == max_process - 1:
            status = "empty"

    # 毎tick実行
    def tick(self):
        global status
        if status == "freeze":
            self.freeze()

    # 描画を更新
    def draw(self):
        global status
        after_zoom_image = pygame.transform.scale_by(self.new_image, self.scale)
        self.rect = after_zoom_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        if status == "freeze":
            SURFACE.blit(after_zoom_image, self.rect)



status = "standby"
next_status = "standby"
process = 0
def main():

    global status
    global process
    global next_status
    background = Background((SURFACE_X_SIZE / 2, SURFACE_Y_SIZE / 2), "./image/background.png")
    chest = Chest((SURFACE_X_SIZE / 2, SURFACE_Y_SIZE / 2), "./image/chest.png")
    flash = Flash((SURFACE_X_SIZE / 2, SURFACE_Y_SIZE / 2), "image/flash.png")
    freeze = Freeze((SURFACE_X_SIZE / 2, SURFACE_Y_SIZE / 2), "image/freeze.png")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.dict["button"] == 3:
                    #pygame.quit()
                    #sys.exit()
                    next_status = "freeze"
                else:
                    next_status = "open"
        
        background.tick()
        chest.tick()
        flash.tick()
        freeze.tick()

        background.draw()
        chest.draw()
        flash.draw()
        freeze.draw()

        #print(f"status={status}, next_status={next_status}")
        if status == "empty":
            process = -1
            status = next_status
            if next_status == "standby":
                next_status = "standby"
            else:
                next_status = "empty"

        process += 1
        pygame.display.update()
        FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()