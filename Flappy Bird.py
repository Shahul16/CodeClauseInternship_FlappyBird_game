# Import libraries
import pygame
import random

# Imports constants and classes from the pygame.locals module
from pygame.locals import *
pygame.init()

# Control the frame rate of the game loop
clock = pygame.time.Clock()
fps = 60

# Game window width and height
screen_width = 860
screen_height = 600

# Creates the game and title window 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Define font and colours for score
font = pygame.font.SysFont('Bauhaus 93', 60)
white = (255, 255, 255)

# Define font and colours for highest score
font_score = pygame.font.SysFont('Bauhaus 93', 35)
red_score = (255, 0, 0)

# Define font and colours for highest score text
font_score_text = pygame.font.SysFont('Arial Black', 25)
red_score_text = (255, 0, 0)

# Define game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 170
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
highest_score = 0
highest_score_text='Highest Score'
pass_pipe = False

# Load images
background = pygame.image.load('img/background.png')
ground_img = pygame.image.load('img/ground.png')
restart_img = pygame.image.load('img/restart.png')

# Displaying the text
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))
    
# Displaying the text
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))    
    
# Reset the game state to its initial state 
def reset_game():
	pipe_group.empty()
	flappy.rect.x = 100
	flappy.rect.y = int(screen_height / 2)
	score = 0    
	return score   


# Bird class
class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
                
		for num in range(1, 4):
			img = pygame.image.load(f'img/bird{num}.png')
			self.images.append(img)  
            
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False
        
# Gravity and jump function
# Gravity
	def update(self):
		if flying == True:
			self.vel += 0.5
            # Set a limit for the velocity
			if self.vel > 9.81:
				self.vel = 9.81
            # Set a limit for the falling bird
			if self.rect.bottom < 530:
				self.rect.y += int(self.vel)
   
        # Jump
		if game_over == False:           
            # Checks if the mouse has been clicked
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -10    
            # Checks if the mouse has been released    
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
                
			self.counter += 1
			flap_cooldown = 5
            
            # Checks if enough game loops have passed to update the animation frame.
			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
                
                # Checks if we have reached the end of the list
				if self.index >= len(self.images):
					self.index = 0
			self.image = self.images[self.index]
            # Rotate the bird
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			self.image = pygame.transform.rotate(self.images[self.index], -90)
            
            
# Pipe class           
class Pipe(pygame.sprite.Sprite):
	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/pipe.png')
		self.rect = self.image.get_rect()
        
        # Position 1 mean pipe is on top, -1 is mean pipe is on bottom
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap)/2]
		if position == -1:
			self.rect.topleft = [x, y + int(pipe_gap)/2]
            
	def update(self):
        # The pipe is moved horizontally towards the left side of the screen
		self.rect.x -= scroll_speed  
        # Delete all the pipes we passed
		if self.rect.right < 0:
			self.kill()
            
            
# Button class            
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self):
		action = False
		pos = pygame.mouse.get_pos()
        # Check if mouse is over the button
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True
		screen.blit(self.image, (self.rect.x, self.rect.y))
		return action
            
        
# Create and manage sprite groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

# Initial position of the bird sprite on the game screen.
flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)

# Create restart button instance
button = Button(screen_width // 2 - 50, screen_height // 2 - 100, restart_img)


# Main game loop
run = True
while run:
	clock.tick(fps)
    
    # Draw background
	screen.blit(background, (0,0))
    
    # Draws all the bird sprites on the game screen.
	bird_group.draw(screen)
    
    # Draws all the pip sprites on the game screen.
	pipe_group.draw(screen)
    
    # Updates the animation and behavior of each bird
	bird_group.update()

	# Draw the ground
	screen.blit(ground_img, (ground_scroll, 530))
    
    # Check the score
	if len(pipe_group) > 0:
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				if score >= highest_score:
					highest_score = score
				pass_pipe = False
                
	draw_text(str(score), font, white, int(screen_width / 2), 20)
	draw_text(str(highest_score), font_score, red_score, int(screen_width / 9), 40)
	draw_text(highest_score_text, font_score_text, red_score_text, int(screen_width / 80), 10)

    # Check for collision
	if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
		game_over = True

	# Check if bird has hit the ground
	if flappy.rect.bottom >= 530:
		game_over = True
		flying = False


	if game_over == False and flying == True:       
        # Generate new pipes
		time_now = pygame.time.get_ticks()
		if time_now - last_pipe > pipe_frequency:
			pipe_height = random.randint(-100, 100)
			btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now
        
        
        # Draw and scroll the ground
		ground_scroll -= scroll_speed
        # Create a continuous loop of the ground scrolling, making it appear seamless
		if abs(ground_scroll) > 35:
			ground_scroll = 0
		pipe_group.update()
       
    # Check for game over and reset
	if game_over == True:
		if button.draw() == True:
			game_over = False        
			score = reset_game()    

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
        # Start the game after the mouse is clicked
		if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
			flying = True
            
    # Update the display
	pygame.display.update()
    
# Quit the game
pygame.quit()

