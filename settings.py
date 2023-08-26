import pygame as pg
from support import loadSprite

tileSize = 16
WIDTH = 800
HEIGHT = 600
FPS = 60

spritePath = "Sprites/Sprout Lands - Sprites - Basic pack/Objects/"
uiPath = "Sprites/Sprout Lands - Sprites - Basic pack/Ui/Slots/"
testSpritePath = "Sprites/test/"

playerSpeed = 2.3
slotScale = (55, 55)
itemScale = (24,24)

itemData = {
    "Hoe":{
        "name": "Hoe",
        "uiSprite": loadSprite(f"{uiPath}Hoe.png", slotScale),
        "uiSpriteSelected": loadSprite(f"{uiPath}HoeSelected.png", slotScale),
         },
    "Axe": {
        "name": "Axe",
        "uiSprite": loadSprite(f"{uiPath}Axe.png", slotScale),
        "uiSpriteSelected": loadSprite(f"{uiPath}AxeSelected.png", slotScale),
         },
    "WateringCan": {
        "name": "WateringCan",
        "uiSprite": loadSprite(f"{uiPath}WateringCan.png", slotScale),
        "uiSpriteSelected":loadSprite(f"{uiPath}WateringCanSelected.png", slotScale),
        },
    "Apple": {
        "name": "Apple",
        "costs": 5,
        "CropSprite":  loadSprite(f"{spritePath}/Plants/Apple/2.png",(tileSize,tileSize)),
        "uiSprite": loadSprite(f"{uiPath}Apple.png", slotScale),
        "uiSpriteSelected": loadSprite(f"{uiPath}AppleSelected.png", slotScale),
        "PhaseOneSprite": loadSprite(f"{spritePath}/Plants/Apple/1.png",(tileSize,tileSize)),
        "PhaseTwoSprite": loadSprite(f"{spritePath}/Plants/Apple/2.png",(tileSize,tileSize)),
        "PhaseThreeSprite": loadSprite(f"{spritePath}/Plants/Apple/3.png",(tileSize,tileSize)),
        "CollisionSprite": loadSprite(f"{spritePath}/Plants/Apple/collision.png",(tileSize,tileSize)),
         },

    "Wheat":{
        "name": "Wheat",
        "costs": 10,
        "uiSprite": loadSprite(f"{uiPath}Wheat.png",slotScale),
        "uiSpriteSelected": loadSprite(f"{uiPath}WheatSelected.png", slotScale),
        "PhaseOneSprite": loadSprite(f"{spritePath}/Plants/Wheat/1.png",(tileSize,tileSize)),
        "PhaseTwoSprite": loadSprite(f"{spritePath}/Plants/Wheat/2.png",(tileSize,tileSize)),
        "PhaseThreeSprite": loadSprite(f"{spritePath}/Plants/Wheat/3.png",(tileSize,tileSize)),
        "PhaseFourSprite": loadSprite(f"{spritePath}/Plants/Wheat/4.png",(tileSize,tileSize)),
        "CropSprite": loadSprite(f"{spritePath}/Plants/Wheat/5.png",(tileSize,tileSize)),
        "CollisionSprite": loadSprite(f"{spritePath}/Plants/Wheat/collision.png",(tileSize,tileSize)),

        },
    "Tomato":{
        "name": "Tomato",
        "costs": 15,
        "uiSprite": loadSprite(f"{uiPath}Tomato.png", slotScale),
        "uiSpriteSelected": loadSprite(f"{uiPath}TomatoSelected.png", slotScale),
        "PhaseOneSprite": loadSprite(f"{spritePath}Plants/Tomato/1.png",(tileSize,tileSize)),
        "PhaseTwoSprite": loadSprite(f"{spritePath}Plants/Tomato/2.png",(tileSize,tileSize)),
        "PhaseThreeSprite": loadSprite(f"{spritePath}Plants/Tomato/3.png",(tileSize,tileSize)),
        "PhaseFourSprite": loadSprite(f"{spritePath}/Plants/Tomato/4.png",(tileSize,tileSize)),
        "CropSprite": loadSprite(f"{spritePath}/Plants/Tomato/5.png",(tileSize,tileSize)),
        "CollisionSprite": loadSprite(f"{spritePath}/Plants/Tomato/collision.png",(tileSize,tileSize)),
    },
    "Wood":{
        "name": "Wood",
        "CropSprite":  loadSprite(f"{spritePath}/Plants/Wood/Wood.png",(tileSize,tileSize)),
        "uiSprite": loadSprite(f"{uiPath}Wood.png", slotScale),
        "uiSpriteSelected": loadSprite(f"{uiPath}WoodSelected.png", slotScale),
        "CollisionSprite": loadSprite(f"{spritePath}/Plants/Wood/collision.png",(tileSize,tileSize)),

    }

}

chestSprites = {
    1: loadSprite(f"{spritePath}Chests/1.png",(tileSize,tileSize)),
    2: loadSprite(f"{spritePath}Chests/2.png",(tileSize,tileSize)),
    3: loadSprite(f"{spritePath}Chests/3.png",(tileSize,tileSize)),
    4: loadSprite(f"{spritePath}Chests/4.png",(tileSize,tileSize)),
    5: loadSprite(f"{spritePath}Chests/5.png",(tileSize,tileSize)),

}

plantTileSprites = {
    "Soil":{
        "untiledSprite": loadSprite(f"{spritePath}untiledDirt.png",(tileSize,tileSize)),
        "tiledSprite": loadSprite(f"{spritePath}tiledDirt.png",(tileSize,tileSize)),
        "WateredSprite": loadSprite(f"{spritePath}WateredTiledDirt.png",(tileSize,tileSize)),
    },
}

testSprites = {
               "Wall": loadSprite(f"{testSpritePath}wall.png",(tileSize,tileSize)),
               "Player": loadSprite(f"{testSpritePath}player.png",(tileSize,tileSize)),
               "Apple": "Sprites/Sprout Lands - Sprites - Basic pack/Objects/AppleFruit Final.png",
               "Chest": loadSprite(f"{spritePath}Chests/1.png",(tileSize,tileSize)),
               "AppleFruit": loadSprite(f"{testSpritePath}AppleFruit.png",(tileSize // 2,tileSize // 2)),
               }


uiSprites = {
             "InventoryHolder":"Sprites/Sprout Lands - Sprites - Basic pack/Ui/Inventory.png",
             "EmptySlot": loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/EmptySlot.png",slotScale),
             "EmptySlotSelected": loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/Slots/EmptySlotSelected.png",slotScale),
             "FaceContainer":loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/FaceContainer.png",(100,100)),
             "HeartCoinContainer":loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/CoinHeartContainer.png",(130,130)),
             "DefaultFace": loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/DefaultFace.png",(62,62)),
             "FullHeart": loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/Icons/Heart/Full.png",(40,38)),
             "HalfHeart": loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/Icons/Heart/Half.png",(40,38)),
             "EmptyHeart": loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/Icons/Heart/Empty.png",(40,38)),
             "DialogueBox": loadSprite("Sprites/Sprout Lands - Sprites - Basic pack/Ui/Dialouge UI/DialogueBox.png",(750,150)),

             }

equipmentItems = ["Hoe", "Axe", "WateringCan"]
seedItems = ["Wheat","Tomato"]
sellableItems = ["Wheat","Tomato","Apple"]
groundTiles = ["Soil","Plants"]




