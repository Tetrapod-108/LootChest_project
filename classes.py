import pygame

import global_variable as g
import sound as s

# クラス: 背景
class Background:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.pos = pos
        self.scale = 1.0
    
    # g.status = "drop"時に実行
    def drop(self):
        max_process = 31
        if 0 <= g.process % max_process < 10:
            self.image = pygame.image.load("image/background2.png")
        if 10 <= g.process % max_process < 20:
            self.image = pygame.image.load("image/background3.png")
        if 20 <= g.process % max_process < max_process:
            self.image = pygame.image.load("image/background4.png")

    # g.status = "standby"時に実行
    #def standby(self):
    #    print("a")

    # g.status = "zoom"時に実行
    def zoom(self):
        max_process = 90
        if 0 <= g.process % max_process < 2:
            offset = 0.3
        if 2 <= g.process % max_process < 3:
            offset = 0.2
        if 3 <= g.process % max_process < 5:
            offset = 0.1
        if 5 <= g.process % max_process < max_process:
            offset = 0
        self.scale = self.scale + offset
        if g.process % max_process == max_process - 1:
            g.status = "empty"
            g.next_status = "open"

    # 毎tick実行
    def tick(self):
        #if g.status == "standby":
            #self.standby()
        if g.status == "zoom":
            self.zoom()
        if g.status == "drop":
            self.drop()
    
    # 描画を更新
    def draw(self):
        self.new_image = pygame.transform.scale_by(self.image, self.scale)
        self.rect = self.new_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        g.SURFACE.blit(self.new_image, self.rect)


# クラス: チェスト
class Chest:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.new_image = pygame.image.load(path)
        self.pos = pos
        self.theta = 0
        self.scale = 1.0
        self.verocity = 0
    
    # g.status = "drop"時に実行
    def drop(self):
        max_process = 31
        if 0 <= g.process % max_process < max_process:
            self.verocity = 9.8 * g.process % max_process
            self.pos[1] += self.verocity
        if g.process % max_process == max_process - 1:
            s.play_sound("sound/drop.mp3", 0.5)
            g.status = "empty"
            g.next_status = "standby"

    # g.status = "superdrop"時に実行
    def superdrop(self):
        max_process = 32
        if 0 <= g.process % max_process < max_process:
            self.verocity = 9.8 * g.process % max_process
            self.pos[1] += self.verocity
        self.pos[1] = -100
        if g.process % max_process == max_process - 1:
            g.status = "empty"
            g.next_status = "standby"

    # g.status = "standby"時に実行
    def standby(self):
        max_process = 100
        if g.process % max_process == 0:
            s.play_sound("sound/standby.mp3", 0.5)
        if 0 <= g.process % max_process < 4:
            self.theta -= 3
        if 4 <= g.process % max_process < 12:
            self.theta += 3
        if 12 <= g.process % max_process < 20:
            self.theta -= 3
        if 20 <= g.process % max_process < 24:
            self.theta += 3
        if 24 <= g.process % max_process < max_process:
            if g.next_status != "standby":
                g.status = "empty"
        if g.process % max_process == max_process - 1:
            g.status = "empty"
        self.new_image = pygame.transform.rotate(self.image, self.theta)

    # g.status = "zoom"時に実行
    def zoom(self):
        max_process = 90
        if g.process % max_process == 10:
            s.play_sound("sound/lock_open.mp3", 0.5)
        if 0 <= g.process % max_process < 2:
            offset = 0.3
        if 2 <= g.process % max_process < 3:
            offset = 0.2
        if 3 <= g.process % max_process < 5:
            offset = 0.1
        if 5 <= g.process % max_process < max_process:
            offset = 0
        self.scale = self.scale + offset
        
    # g.status = "open"時に実行
    def open(self):
        max_process = 24
        if 0 <= g.process % max_process < 4:
            self.new_image = pygame.image.load("image/chest_frame2.png")
        if 4 <= g.process % max_process < 8:
            self.new_image = pygame.image.load("image/chest_frame3.png")
        if 12 <= g.process % max_process < 16:
            self.new_image = pygame.image.load("image/chest_frame4.png")
        if g.process % max_process == max_process - 1:
            g.status = "empty"
            g.next_status = "result"

    # 毎tick実行
    def tick(self):
        if g.status == "standby":
            self.standby()
        if g.status == "open":
            self.open()
        if g.status == "zoom":
            self.zoom()
        if g.status == "drop":
            self.drop()

    # 描画を更新
    def draw(self):
        after_zoom_image = pygame.transform.scale_by(self.new_image, self.scale)
        self.rect = after_zoom_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        g.SURFACE.blit(after_zoom_image, self.rect)



# クラス: フラッシュ
class Flash:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.new_image = pygame.image.load(path)
        self.pos = pos
        self.theta = 0
        self.scale = 2.0
    
    # g.status = "result"時に実行
    def result(self):
        self.theta += 1
        max_process = 100
        if 0 <= g.process % max_process < 50: 
            self.scale += 0.005
        if 50 <= g.process % max_process < 100: 
            self.scale -= 0.005
        self.new_image = pygame.transform.rotate(self.image, self.theta)

    # 毎tick実行
    def tick(self):
        if g.status == "result":
            self.result()

    # 描画を更新
    def draw(self):
        after_zoom_image = pygame.transform.scale_by(self.new_image, self.scale)
        self.rect = after_zoom_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        if g.status == "result":
            g.SURFACE.blit(after_zoom_image, self.rect)



# クラス: フリーズ
class Freeze:

    # コンストラクタ
    def __init__(self, pos, path):
        self.image = pygame.image.load(path)
        self.new_image = pygame.image.load(path)
        self.pos = pos
        self.theta = 0
        self.scale = 1.0
    
    # g.status = "freeze"時に実行
    def freeze(self):
        max_process = 90
        if 0 <= g.process % max_process < 4:
            self.new_image = pygame.image.load("image/freeze_frame3.png")
        if 4 <= g.process % max_process < 8:
            self.new_image = pygame.image.load("image/freeze_frame2.png")
        if 12 <= g.process % max_process < 16:
            self.new_image = pygame.image.load("image/freeze.png")
        if 16 <= g.process % max_process < max_process:
            self.new_image = pygame.image.load("image/freeze_frame3.png")
        if g.process % max_process == max_process - 1:
            g.status = "empty"

    # 毎tick実行
    def tick(self):
        if g.status == "freeze":
            self.freeze()

    # 描画を更新
    def draw(self):
        after_zoom_image = pygame.transform.scale_by(self.new_image, self.scale)
        self.rect = after_zoom_image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])
        if g.status == "freeze":
            g.SURFACE.blit(after_zoom_image, self.rect)
