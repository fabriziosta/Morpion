import pygame, sys, random
from pygame.locals import *
from sys import exit

def controllovittoria (analisi, lista):
	analisi.sort()
	if 1 in analisi and 2 in analisi and 3 in analisi:
		analisi = True
		return analisi
	elif 4 in analisi and 5 in analisi and 6 in analisi:
		analisi = True
		return analisi
	elif 7 in analisi and 8 in analisi and 9 in analisi:
		analisi = True
		return analisi
	elif 1 in analisi and 4 in analisi and 7 in analisi:
		analisi = True
		return analisi
	elif 2 in analisi and 5 in analisi and 8 in analisi:
		analisi = True
		return analisi
	elif 3 in analisi and 6 in analisi and 9 in analisi:
		analisi = True
		return analisi
	elif  1 in analisi and 5 in analisi and 9 in analisi:
		analisi = True
		return analisi
	elif 3 in analisi and 5 in analisi and 7 in analisi:
		analisi = True
		return analisi
	cont = len(lista)
	if cont == 0:
		return False

def inserimento (LISTA, giocatore, variabile):
	giocatore.append(variabile)
	LISTA.remove(variabile)
	return True
	
turno = False #INIZIA UTENTE se e' FALSE
scelta = input("Chi vuoi fare giocare per prima? \nDigita qualsiasi tasto per iniziare tu oppure \nDigita 2 per far iniziare il computer: ")
if scelta == "2":
	turno = True

RED = (255,0,0)
BLACK = (0,0,0)
VERDE = (10,255,10)

pygame.init()
sfondo = pygame.display.set_mode((600,600))
pygame.display.set_caption('Il gioco del Morpion')
LISTA = [1,2,3,4,5,6,7,8,9]
giocatore = []
computer = []
sfondo.fill(RED)
click = True #DISABILITA CLICK UTENTE SE DIVENTA FALSE

while True:
	for event in pygame.event.get():
		pygame.draw.line(sfondo,BLACK,(200,0),(200,600),4)
		pygame.draw.line(sfondo,BLACK,(400,0),(400,600),4)
		pygame.draw.line(sfondo,BLACK,(0,200),(600,200),4)
		pygame.draw.line(sfondo,BLACK,(0,400),(600,400),4)
		
#EVENTO CLICK UTENTE
		if click == True:
			if turno == False:
				if event.type == MOUSEBUTTONUP:
					x,y = event.pos
					for lunghezza in range (0,200):
						for altezza in range (0,200):
							if 1 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(40,40),(160,160),4)
									pygame.draw.line(sfondo,BLACK,(160,40),(40,160),4) 
									variabile = 1
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (205,400):
						for altezza in range (0,200):
							if 2 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(240,40),(360,160),4)
									pygame.draw.line(sfondo,BLACK,(240,160),(360,40),4)
									variabile = 2
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (405,600):
						for altezza in range (0,200):
							if 3 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(440,40),(560,160),4)
									pygame.draw.line(sfondo,BLACK,(440,160),(560,40),4)
									variabile = 3
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (0,200):
						for altezza in range (205,400):
							if 4 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(40,240),(160,360),4)
									pygame.draw.line(sfondo,BLACK,(160,240),(40,360),4)
									variabile = 4
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (205,400):
						for altezza in range (205,400):
							if 5 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(240,240),(360,360),4)
									pygame.draw.line(sfondo,BLACK,(360,240),(240,360),4)
									variabile = 5
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (405,600):
						for altezza in range (205,400):
							if 6 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(440,240),(560,360),4)
									pygame.draw.line(sfondo,BLACK,(560,240),(440,360),4) 
									variabile = 6
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (0,200):
						for altezza in range (405,600):
							if 7 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(40,440),(160,560),4)
									pygame.draw.line(sfondo,BLACK,(160,440),(40,560),4)
									variabile = 7
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (205,400):
						for altezza in range (405,600):
							if 8 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(240,440),(360,560),4)
									pygame.draw.line(sfondo,BLACK,(360,440),(240,560),4) 
									variabile = 8
									turno = inserimento(LISTA, giocatore, variabile)
					for lunghezza in range (405,600):
						for altezza in range (405,600):
							if 9 in LISTA:
								if x == lunghezza and y == altezza:
									pygame.draw.line(sfondo,BLACK,(440,440),(560,560),4)
									pygame.draw.line(sfondo,BLACK,(560,440),(440,560),4)
									variabile = 9
									turno = inserimento(LISTA, giocatore, variabile)				
					
					#CONTROLLO VITTORIA
					risultato = controllovittoria(giocatore, LISTA)
					if risultato == True:
						turno = False
						myfont = pygame.font.Font('freesansbold.ttf',115)
						texteSurface = myfont.render("VITTORIA!", 100,BLACK,VERDE)
						texteRect = texteSurface.get_rect()
						texteRect.topleft = (0,250)
						sfondo.blit(texteSurface,texteRect)
						click = False
					elif risultato == False:  #CONTROLLO PAREGGIO
						turno = False
						myfont = pygame.font.Font('freesansbold.ttf',100)
						texteSurface = myfont.render("PAREGGIO", 100,BLACK,VERDE)
						texteRect = texteSurface.get_rect()
						texteRect.topleft = (30,250)
						sfondo.blit(texteSurface,texteRect)
								
#TURNO COMPUTER!!
		if turno == True: 
			variabile = int(random.choice(LISTA)) #selezione un numero random da 1 a 9
			if variabile == 1:
				pygame.draw.circle(sfondo,BLACK,(100,100),70,4)
			elif variabile == 2:
				pygame.draw.circle(sfondo,BLACK,(300,100),70,4)
			elif variabile == 3:
				pygame.draw.circle(sfondo,BLACK,(500,100),70,4)
			elif variabile == 4:
				pygame.draw.circle(sfondo,BLACK,(100,300),70,4)
			elif variabile == 5:
				pygame.draw.circle(sfondo,BLACK,(300,300),70,4)
			elif variabile == 6:
				pygame.draw.circle(sfondo,BLACK,(500,300),70,4)
			elif variabile == 7:
				pygame.draw.circle(sfondo,BLACK,(100,500),70,4)
			elif variabile == 8:
				pygame.draw.circle(sfondo,BLACK,(300,500),70,4)
			elif variabile == 9:
				pygame.draw.circle(sfondo,BLACK,(500,500),70,4)
				
				
			computer.append(variabile)
			LISTA.remove(variabile) #RIMUOVE QUEL NUMERO DALLA LISTA
			risultato = controllovittoria (computer, LISTA) 
			if risultato == True: #COMUNICA ALL'UTENTE ATTRAVERSO UNA FINESTRA CHE HA PERSO
				click = False
				myfont = pygame.font.Font('freesansbold.ttf',100)
				texteSurface = myfont.render("SCONFITTA.", 100,VERDE,BLACK)
				texteRect = texteSurface.get_rect()
				texteRect.topleft = (0,250)
				sfondo.blit(texteSurface,texteRect)
			elif risultato == False: #PAREGGIO!!
				myfont = pygame.font.Font('freesansbold.ttf',100)
				texteSurface = myfont.render("PAREGGIO", 100,BLACK,VERDE)
				texteRect = texteSurface.get_rect()
				texteRect.topleft = (30,250)
				sfondo.blit(texteSurface,texteRect)
			turno = False		
							 
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
