import pygame
from pygame.locals import *
from pygame import *

from shaders import *



from gl import *

width = 1024
height = 768

deltaTime = 0.0

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()
pygame.display.set_caption('ver ReadMe para controles, si no se ve nada, mover la luz para apreciar el shader')

font = pygame.font.SysFont('Arial', 20)
textsurface = font.render('Hello World!', False, white)
screen.blit(textsurface, (250, 250))
    


rend = Renderer(screen)

#message_display('Controles: wasd para moverse, flechas para mover luz, jl para rotar y zx para rotar camara, 12 para cambiar entre modo relleno y modo wireframe')
#pygame.image.load('animegirl.png')

rend.setShaders(vertex_shader, fragment_shader)#vertex_shader, fragment_shader, shaderSi

face = Model("MouseS.obj", "Mouse_D.bmp")
face.position.z = -5
anime = Model("anime.obj", "animegirl.png")
anime.position.z = -5
sword = Model("sword.obj", "sword.png")
sword.position.z = -5
gun = Model("gun.obj", "gun.bmp")
gun.position.z = -5
puppy = Model("Puppy.obj","dog.bmp")
puppy.position.z = -5

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


rend.scene.append(face)

face.position.z -= 10
face.scale.x = 5
face.scale.y = 5
face.scale.z = 5

anime.position.y -= 1
anime.scale.x = 0.8
anime.scale.y = 0.8
anime.scale.z = 0.8

puppy.position.y -= 3
puppy.scale.x = 0.2
puppy.scale.y = 0.2
puppy.scale.z = 0.2

sword.position.y -= 1
sword.rotation.y = 90
sword.rotation.x = 90
sword.scale.x = 0.3
sword.scale.y = 0.3
sword.scale.z = 0.3

gun.scale.x = 1
gun.scale.y = 1
gun.scale.z = 1

backgroundP = pygame.image.load("background.jpg")

limit = 100

isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_g:
                rend.filledMode()
            elif event.key == pygame.K_h:
                rend.wireframeMode()



    if keys[K_d]:
        if limit > 0: 
            rend.camPosition.x -= 10 * deltaTime
            limit -= 5

    elif keys[K_a]:
        if limit <= 300:
            rend.camPosition.x += 10 * deltaTime
            limit += 5

    elif keys[K_s]:
        if limit <= 300:
            rend.camPosition.z += 10 * deltaTime
            limit += 5

    elif keys[K_w]:
        if limit > 0: 
            rend.camPosition.z -= 10 * deltaTime
            limit -= 5

    elif keys[K_q]:
        if limit <= 300:
            rend.camPosition.y += 10 * deltaTime
            limit += 5
    elif keys[K_e]:
        if limit > 0: 
            rend.camPosition.y -= 10 * deltaTime
            limit -= 5
    elif event.type == pygame.MOUSEWHEEL:
        if event.y > 0:
            if limit <= 300:
                rend.camPosition.z += 10 * deltaTime
                limit += 5
        elif event.y < 0:
            if limit > 0: 
                rend.camPosition.z -= 10 * deltaTime
                limit -= 5
        

    if pygame.mouse.get_rel()[0] > 0:
        rend.scene[0].rotation.y += 60 * deltaTime
    elif pygame.mouse.get_rel()[0] < 0:
        rend.scene[0].rotation.y -= 60 * deltaTime

    if pygame.mouse.get_rel()[1] > 0:
        if limit <= 300:
            rend.camPosition.y += 10 * deltaTime
            limit += 5
    elif pygame.mouse.get_rel()[1] < 0:
        if limit > 0: 
            rend.camPosition.y -= 10 * deltaTime
            limit -= 5
    
    
    elif keys[K_1]:#normal shaders
        rend.setShaders(vertex_shader, fragment_shader)
    elif keys[K_2]:#toon shaders
        rend.setShaders(toon_vertex_shader, toon_fragment_shader)
    elif keys[K_3]:#color changing shaders
        rend.setShaders(vertex_shader,shader_colored_changing)
    elif keys[K_4]:#night vision shaders
        rend.setShaders(vertex_shader,night_vision)

    #cambio modelos
    elif keys[K_KP1]:
        rend.scene[0] = face
        face.position.z = -5
    elif keys[K_KP2]:
        rend.scene[0] = anime
        anime.position.z = -1
    elif keys[K_KP3]:
        rend.scene[0] = puppy
        puppy.position.z = -20
    elif keys[K_KP4]:
        rend.scene[0] = sword
        sword.position.z = -15
    elif keys[K_KP5]:
        rend.scene[0] = gun
        gun.position.z = -5

    elif keys[K_KP9]:
        pygame.mixer.music.stop()

    elif keys[K_KP0]:
        pygame.mixer.music.play(-1)


        


    elif keys[K_LEFT]:
        rend.pointLight.x += 10 * deltaTime

    elif keys[K_RIGHT]:
        rend.pointLight.x -= 10 * deltaTime

    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime

    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    elif keys[K_j]:
        rend.scene[0].rotation.y += 60 * deltaTime
    elif keys[K_l]:
        rend.scene[0].rotation.y -= 60 * deltaTime
        

    elif keys[K_z]:
         rend.camRotation.y += 10 * deltaTime
         rend.LookAt(face.position)
    elif keys[K_x]:
         rend.camRotation.y -= 10 * deltaTime
         rend.LookAt(face.position)

    if keys[K_p]:
        if rend.value > 0:
            rend.value -= 0.1 * deltaTime

    if keys[K_o]:
        if rend.value < 0.2:
            rend.value += 0.1 * deltaTime

    #rend.scene[0].rotation.x += 10 * deltaTime
    #rend.scene[0].rotation.y += 10 * deltaTime
    #rend.scene[0].rotation.z += 10 * deltaTime


    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime
    #print(deltaTime)

    rend.update()
    rend.render()
    screen.blit(textsurface, (50, 50))
    rend.screen.blit(backgroundP, (0, 0))
    pygame.display.flip()

pygame.quit()
