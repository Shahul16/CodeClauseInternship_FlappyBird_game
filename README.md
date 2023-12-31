# CodeClauseInternship_FlappyBird_game
# code breakdown

# 1 – 23 

# In this part we set up the game window, initialize the game, and define some constants like frame rate, window dimensions, and font.  The code also imports necessary modules and constants from Pygame, and it sets the title of the game window.

# 25 – 52 

# In this part of the code, various game variables are defined, including those related to scrolling, game state, pipe generation, and the player's score.  Images for the game, including the background, ground, and restart buttons, are loaded from the provided files.  A function named draw_text is defined to display text on the game screen using the specified font and color at the given coordinates.  Another function called reset_game is defined, which resets the game state to its initial condition.  It clears the pipe_group, repositions the bird to the starting position, and resets the player's score to zero. The updated score is then returned from the function.

# 55 – 71 

# In the bird class we set up the bird's attributes and behavior, including animation, position, and jumping in response to mouse clicks.  The Bird class is used to manage the player's character throughout the game, in the class we see several of attributes such as: Clicked: A Boolean flag that indicates if the mouse button has been clicked.  Rect: The bounding rectangle of the bird sprite used for positioning and collision detection and many more.

# 74 – 110

# In this part of the code, the Bird class's update method manages the bird's behavior, which includes gravity and jumping, When flying is True, the bird's vertical velocity (vel) increases by 0.5 units per loop, simulating gravity. The velocity is capped at 9.81 to prevent rapid falling, and the bird's position (rect.y) is updated to make it descend on the screen. Additionally, the bird can jump if game_over is False and the left mouse button is clicked while the bird is not already jumping (self.clicked == False). Jumping sets the bird's velocity to -10, making it move upward, and the jump status is reset when the mouse button is released.  The bird's animation is controlled by self.counter, cycling through animation frames when it surpasses flap_cooldown (set to 5),If self.index exceeds the number of frames in self.images, it resets to 0, creating a loop, the bird's image is rotated by self.vel for flapping wings, when game_over is True, the bird's image rotates to -90 degrees, simulating falling after a collision or game over.

# 113 – 132 

# In this class we set up the pipes in the Flappy Bird game, positions them correctly, and makes them scroll to create the effect of the pipes moving toward the bird as the game progresses. When a new pipe object is created, it loads the pipe image and sets its position based on whether it's a top pipe or a bottom pipe.  The top pipe is flipped vertically so that it points upwards, and the bottom pipe is positioned below the top pipe with a gap in between.  The update method of the Pipe class makes the pipe move to the left, creating the illusion that the pipes are scrolling from right to left.  When a pipe moves entirely off the left side of the screen, it is removed from the game.

# 135 – 162

# In this part we create a restart bottom and we draw the button on the screen and sets its position to the center of the game screen.  In the code we checks if the mouse cursor is over the button by comparing its position with the button's boundaries.  If the mouse clicks while the cursor is over the button, the method returns True, indicating that the button has been clicked.  In addition to the button class, this code creates two sprite groups: bird_group and pipe_group, which are used to manage the bird and pipe objects in the game. 

# 166 – 244

# The main game loop is the heart of the Flappy Bird game, responsible for continuously updating and rendering the game elements.  It runs until the player decides to quit the game. Inside the loop, the background, bird sprites, and pipe sprites are drawn on the screen.  The animation and behavior of each bird are updated, allowing it to fly and respond to player input.  The ground is scrolled to create a moving effect, and the score is checked and updated as the bird passes through pipes.  The loop also detects collisions between the bird and pipes or if the bird hits the top boundary or the ground, resulting in a game over.  When the game is not over and the bird is flying, new pipes are periodically generated to keep the game challenging.  The player's input in the form of a mouse click is detected to control the bird's flying. The display is continuously updated to show all the changes in the game.  Once the player decides to quit, the game is closed gracefully.



