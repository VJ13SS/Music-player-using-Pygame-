		''''''HEY ALL..This is a simple music player created using Pygame module in python...
The project deals with the basic concepts in pygame like drawing rectangles ,rendering text labels,playing music etc and inculcating them to meet the logic...
Here the Border,boundaries are creted by drawing rectangles and music is handled  using mixer module functions...
The project only aims at understanding and implementing the logic to a real world item and here i had tried to make it in a way i could..try to include potential updates and enruch your creativity...


Prerequisite: Just have a directory of mp3 files

Note1: This project is made on mobile...and accordingly the dimensions and coordinates are taken ..Try to adjust for yours...

Note 2 : pygame cannot work in baground whioe you are running any other application


Feel free to raise your updates... 
Happy coding...

VJ 13 SS

'''

#Importing modules
import pygame
from pathlib import Path
import random
from datetime import datetime

#Initialization
pygame.init()
time = datetime.now().time()
formatted_time = time.strftime('%H: %M')
BOARD_WIDTH = 2000
BOARD_HEIGHT = 2500
BOARD_COLOR = 'white'

#user name
user = 'VJ 13 SS'

#initialization of font,color
SCREEN_COLOR = (8, 255, 247)
FONT = pygame.font.SysFont('comicsans',55)

#set board
BOARD = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))


def get_music():
	directory = Path('/storage/emulated/0/Audio songs') # Define path of your music directory
	
	#get names of  audio files
	music_names = [file.name for file in directory.iterdir() if file.is_file()]
	
	#get paths
	music_paths = [file for file in directory.iterdir() if file.is_file()]
	
	return music_names,music_paths

#to write text	
def write_text(text,pos,color):
	text_label = FONT.render(f'{text}',1,f'{color}')
	
	BOARD.blit(text_label,pos)

#to check if loop control variable extends the limits
def check_limits(i,limit):
			if i < 0 :
				i = limit - 1
				return i
			elif i > limit - 1 :
				i = 0
				return i
			return i

#load music
def load_music(path):
	#load the music file
	pygame.mixer.music.load(path)

#playing music
def play_music(path):
		#load the file
		load_music(path)
		#play the music
		pygame.mixer.music.play()

#main function	
def main():
	#to get the names and paths if the songs
	music_name,music_paths = get_music()
	
	limit = len(music_name)#total number of files
	i = 0 #loop control variable
	
	play_music(music_paths[i])#play the first song
	
	pause = False
	repeat = False
	state = 'Playing' # Current state(Playing os Paused)
	play = True
	
	
	while play:		
		
		#Drawing the screens and boundaries
		pygame.draw.rect(BOARD, 'orange', (0,0,BOARD_WIDTH, BOARD_HEIGHT))
		pygame.draw.rect(BOARD,BOARD_COLOR, (50,160,BOARD_WIDTH-1000, BOARD_HEIGHT-600))
		pygame.draw.rect(BOARD,SCREEN_COLOR,(90,300,BOARD_WIDTH - 1070, BOARD_HEIGHT - 1700))
		pygame.draw.circle(BOARD,'grey',(550,1580),450)
		pygame.draw.circle(BOARD,'white',(550,1580),270)
		
		#Display Text
		write_text(f'Time: {formatted_time}',(100,350),'red')	
		write_text('MUSIC PLAYER',(400,200),'red')
		write_text(f'Belongs to: {user}',(600,1050),'red')
		
		# writes text
		#for text 30 pixels horizontally and 50 pixels vertically were added
	
		pygame.draw.circle(BOARD,'grey',(550,1580),130)
		write_text('Play/Pause',(450,1570),'black')
			
		write_text('NEXT',(870,1570),'black')		
		
		write_text('PREV',(130,1570),'black')
				
		write_text('Repeat',(480,1200),'black')
				
		write_text('Random',(480,1940),'black')
		
		#events in pygame	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
				
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos()
				
				#100 --> button width
				#pause or resume the music
				if 430 <= mouse_x <= (430 + 150) and 1500 <= mouse_y <= (1500 + 300):
					
		
					#toggle the pause variable		
					pause = not(pause)
					if pause:
						pygame.mixer.music.pause()
						state = 'Paused'
					else:
						pygame.mixer.music.unpause()
						state = 'Playing'
							
				#play next music
				elif 840 <= mouse_x <= (840 + 100) and 1530 <= mouse_y <= (1530 + 100):
					#stop any previous playing music
					pygame.mixer.music.stop()
					
					pause = False
					state = 'Playing'	
					
					#move to next one
					i = check_limits(i+1,limit)
					
					#play music
					play_music(music_paths[i])
					
				#play previous music
				elif 100<= mouse_x <= (130+100) and 1500 <= mouse_y <= (1500 + 300):
					#stop any previous playing music
					pygame.mixer.music.stop()
					
					pause = False
					state = 'Playing'	
					
					#move to previous one
					i = check_limits(i-1,limit)
					#play music
					play_music(music_paths[i])
					
				#to repeat the music
				elif 450 <= mouse_x <= (480 + 100) and 1170 <= mouse_y <= (1200 + 300):
					
					pause = False
					state = 'Playing'	
					
					repeat = True
					state = 'Repeat'
					
				#to play random music from the list
				elif 450 <= mouse_x <= (480 + 100) and 1890 <= mouse_y <= (1940 + 300):
					
					pause = False
					state = 'Playing'	
					
					choice = random.randint(0,limit-1)
					
					i = choice #get random choice
					#play_music
					play_music(music_paths[i])
					
				
			#if a song has finished playing
		if not(pygame.mixer.music.get_busy()) and pause == False:
			if repeat:
				i = i #plays the same music
				repeat = False
			else:
				i = check_limits(i +1 , limit) # move to next song.
				state = 'Playing'
			play_music(music_paths[i]) # play the song
		
		#Displaying text on screen
						
		write_text(f'{state} : ',(100,550),'black')
		write_text(music_name[i],(100,650),'black')		
		write_text(f'Song {i + 1}/{limit}',(810,350),'black')
		write_text('NEXT : ',(100,850),'black')
		write_text(music_name[check_limits(i+1, limit)],(100,950),'black')
		
		
		
					
		pygame.display.update()
		
if __name__ == '__main__':
	main()
	
	
#task...
#try to include error handling
'''eg: try:
		   pygame.mixer.music.play()
		except pygame.error as e:
			print('Unsupported file type')
		'''
