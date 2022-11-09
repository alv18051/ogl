import pygame
from pygame.locals import *

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

face.position.z -= 10
face.scale.x = 5
face.scale.y = 5
face.scale.z = 5
limit = 100


rend.scene.append( face )


isRunning = True

while isRunning:

    

    keys = pygame.key.get_pressed()

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
    
    elif keys[K_1]:#normal shaders
        rend.setShaders(vertex_shader, fragment_shader)
    elif keys[K_2]:#toon shaders
        rend.setShaders(toon_vertex_shader, toon_fragment_shader)
    elif keys[K_3]:#color changing shaders
        rend.setShaders(vertex_shader,shader_colored_changing)
    elif keys[K_4]:#night vision shaders
        rend.setShaders(vertex_shader,night_vision)
        


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
    pygame.display.flip()

pygame.quit()
