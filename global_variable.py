import pygame

# 定数のような何か
ORIGIN_X_SIZE = 128
ORIGIN_Y_SIZE = 128
SCALE = 6
SURFACE_X_SIZE = ORIGIN_X_SIZE * SCALE
SURFACE_Y_SIZE = ORIGIN_Y_SIZE * SCALE
SURFACE = pygame.display.set_mode((SURFACE_X_SIZE, SURFACE_Y_SIZE))
FPSCLOCK = pygame.time.Clock()

# シーンのステータスを管理するグローバル変数
status = "empty"
next_status = "empty"
process = 0