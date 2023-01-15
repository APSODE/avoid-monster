import pygame
from Class.FUNC.RW_JSON import READ_WRITE
from win32api import GetSystemMetrics
#CONFIG_DIR = "C:\\Users\\leegu\\Desktop\\게임제작\\Config\\Main_Config.json"
pygame.init()
CONFIG_DIR = ".\\Config\\Main_Config.json"

WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1) 

print(f"WIDTH = {WIDTH}")
print(f"HEIGHT = {HEIGHT}")

TEST_IMG_DIR = READ_WRITE.READ_JSON(CONFIG_DIR)["OBJECT"]["WEAPON_1"]["OBJECT_IMG_DIR"]


pygame.image.load(TEST_IMG_DIR)
