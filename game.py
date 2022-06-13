import pygame

screen_width = 700
screen_height = 400
player_scale=1
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))

def create_screen():
    global screen
    return screen

def loadImages(images_path):
    image_list = []

    for path in images_path:
        loaded_image = pygame.image.load(path).convert_alpha()
        image_list.append(loaded_image)
    return image_list

def scaleImages(image_list, width, height):
    scaled_images = []
    if(len(image_list) == 1):
        return pygame.transform.scale(image_list[0], (width, height))

    for img in image_list:
        image = pygame.transform.scale(img, (width, height))
        scaled_images.append(image)

    return scaled_images

#Images
color_surf = loadImages(["assets/color_bg.jpg"])
background_surf = loadImages(["assets/environment.png"])
background_surf[0].set_alpha(100)

ground_surf = loadImages(["assets/ground.png"])
door_surf = loadImages(["assets/doorOpen.png"])
win_surf = loadImages(["assets/win.png"])

#player_surf = loadImages(["assets/joe1.png"])
cloud_surf = loadImages(["assets/cloud.png"])
cloud_surf[0].set_alpha(200)

doorHeight=100
doorWidth=100

#Image Scaling
background_surf = scaleImages(background_surf, screen_width, 300)
color_surf = scaleImages(color_surf, screen_width, 400)
door_surf= scaleImages(door_surf, 100,100)
cloud_surf = scaleImages(cloud_surf, 100, 50)
#player_surf = scaleImages(player_surf, 40, 63)
ground_surf = scaleImages(ground_surf, screen_width, 90)


# sprites
#player_rect = pygame.Rect(620,screen_height-145,40,63)
ground_rect = pygame.Rect(0,screen_height-100,screen_width,40)
door_rect = pygame.Rect(screen_width-150,screen_height-180, 100,100)


cloud1X = 50
cloud2X = 300
cloud3X = 550



def draw_arena():
    global color_surf, background_surf
    global ground_surf, door_surf, win_surf
    global cloud_surf, ground_rect, door_rect
    global cloud1X, cloud2X, cloud3X
    global screen

    screen.blit(color_surf, (0, 0))
    screen.blit(background_surf, (0, 100))
    screen.blit(ground_surf, (0, screen_height-90))
    screen.blit(door_surf,door_rect)

    screen.blit(cloud_surf, (cloud1X, 50))
    if cloud1X < -100:
        cloud1X = screen_width
    else:
        cloud1X -= 2

    screen.blit(cloud_surf, (cloud2X, 75))
    if cloud2X < -50:
        cloud2X = screen_width
    else:
        cloud2X -= 1

    screen.blit(cloud_surf, (cloud3X, 100))
    if cloud3X < 0:
        cloud3X = screen_width
    else:
        cloud3X -= 2


    clock.tick(30)



def gameplay(door_rect = door_rect, win_surf = win_surf):
    draw_arena()
    try:
        from main import player_rect, player_surf
        if(player_rect != None and player_surf != None):
            if(player_rect.colliderect(door_rect)):
                screen.blit(win_surf[0],(220,100))
                img_width = int(player_surf.get_width() * 0.99)
                img_height = int(player_surf.get_height() * 0.5)
                print("old"+str(player_surf.get_height()))
                #player_surf = scaleImages([player_surf], img_width,img_height)
                player_surf=pygame.transform.scale(player_surf, (img_width,img_height))
                print("new"+str(player_surf.get_height()))
    except:
        pass
