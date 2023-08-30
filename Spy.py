#! /usr/bin/python -u
# -*- coding:utf-8 -*-

"""
Not only Obamas _is_ watching you...
Agora, estarei também espionando quem abre a tampa do meu notebook... Com a tela bloqueada, é claro.
Based in: http://stackoverflow.com/questions/15870619/python-webcam-http-streaming-and-image-capture
Based in http://helio.loureiro.eng.br/index.php/programacao/25-python/256-usando-python-pra-capturar-a-webcam
"""

SAVEDIR = "/home/eduardo/Imagens/Webcam"

import pygame, sys
import pygame.camera
import time
import os

pygame.init()
pygame.camera.init()
#cam = pygame.camera.Camera("/dev/video0", (640,480))
cam = pygame.camera.Camera("/dev/video0", (1366,720))

#Tempo necessário para bloquear a tela e fechar a tampa do notebook.


while True:
      
    cam.start()
    image = cam.get_image()
    cam.stop()
    timestamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    filename = "%s/%s.jpg" % (SAVEDIR, timestamp)
    pygame.image.save(image, filename)

#	time.sleep(1)
