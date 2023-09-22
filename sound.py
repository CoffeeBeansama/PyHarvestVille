
import pygame as pg
from pygame import mixer


pg.init()

sfx = {
    "coin": mixer.Sound("SFX/Gold.wav"),
    "hoe": mixer.Sound("SFX/hoe.wav"),
    "axe": mixer.Sound("SFX/axe.wav"),
    "purchase": mixer.Sound("SFX/purchase.wav"),
    "noCash": mixer.Sound("SFX/noCash.wav"),
    "chest": mixer.Sound("SFX/chest.wav"),
}

for sounds in sfx.values():
    sounds.set_volume(0.3)

sfx["chest"].set_volume(0.1)

inventorySfx = {
    "selection" : mixer.Sound("SFX/Menu/Selection.wav"),
    "itemSwap": mixer.Sound("SFX/Menu/ItemSwap.mp3"),
    "openInventory": mixer.Sound("SFX/Menu/OpenInventory.mp3"),
    "closeInventory": mixer.Sound("SFX/Menu/CloseInventory.mp3"),

}

for sounds in inventorySfx.values():
    sounds.set_volume(0.2)


def playBGM(bgm):
    if bgm == "level":
        mixer.music.load("SFX/BGM/daybgm.ogg")
    elif bgm == "Menu":
        pass

    mixer.music.play(-1)
    mixer.music.set_volume(0.2)

def playSound(sound):
    player = pg.mixer.Sound

    match sound:
        case "Hoe":
            player.play(sfx["hoe"])
        case "Axe":
            player.play(sfx["axe"])
        case "Coin":
            player.play(sfx["coin"])
        case "Purchase":
            player.play(sfx["purchase"])
        case "No Cash":
            player.play(sfx["noCash"])
        case "Chest":
            player.play(sfx["chest"])
        case "Selection":
            player.play(inventorySfx["selection"])
        case "ItemSwap":
            player.play(inventorySfx["itemSwap"])
        case "OpenInventory":
            player.play(inventorySfx["openInventory"])
        case "CloseInventory":
            player.play(inventorySfx["closeInventory"])


