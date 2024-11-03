import pygame
import time
import random

# Define the SnakeGame class which contains all the game logic
class SnakeGame:
    def __init__(self):
        # Game parameters
        self.snake_speed = 15  # Speed of the snake (frames per second)
        self.window_x = 720  # Width of the game window
        self.window_y = 480  # Height of the game window

        # Defining colors using RGB values
        self.black = pygame.Color(0, 0, 0)  # Background color
        self.white = pygame.Color(255, 255, 255)  # Fruit color
        self.red = pygame.Color(255, 0, 0)  # Game over text color
        self.green = pygame.Color(0, 255, 0)  # Snake color

        # Initializing pygame and setting up the window
        pygame.init()
        pygame.display.set_caption("Snake Game")  # Title of the game window
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))  # Set window size

        # FPS controller to control the speed of the game
        self.fps = pygame.time.Clock()

        # Initial snake position (starting point)
        self.snake_position = [100, 50]  # Head of the snake

        # Initial snake body (the first four blocks of the snake)
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

        # Generate the initial position for the fruit
        self.fruit_position = self.generate_fruit_position()
        self.fruit_spawn = True  # To check if a new fruit needs to spawn

        # Direction control - snake starts by moving to the right
        self.direction = "RIGHT"  # Initial direction
        self.change_to = self.direction  # Stores the direction to change to

        # Initial score
        self.score = 0

    # This method generates a random position for the fruit on the grid
    def generate_fruit_position(self):
        return [
            random.randrange(1, (self.window_x // 10)) * 10,
            random.randrange(1, (self.window_y // 10)) * 10,
        ]

    # This method displays the score on the screen during the game
    def show_score(self, color, font, size):
        # Create font object using system font
        score_font = pygame.font.SysFont(font, size)

        # Render the score text
        score_surface = score_font.render("Score : " + str(self.score), True, color)

        # Get the rectangular area for the text
        score_rect = score_surface.get_rect()

        # Display the score on the screen
        self.game_window.blit(score_surface, score_rect)

    # This method handles the game over logic when the player loses
    def game_over(self):
        # Create a font object for the "Game Over" message
        my_font = pygame.font.SysFont("times new roman", 50)

        # Create the "Game Over" text surface
        game_over_surface = my_font.render("Game Over. Your Score is : " + str(self.score), True, self.red)

        # Get the rectangular area for the game over text
        game_over_rect = game_over_surface.get_rect()

        # Position the game over text at the top center of the window
        game_over_rect.midtop = (self.window_x / 2, self.window_y / 4)

        # Display the game over text on the screen
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()  # Update the display

        # Pause for 2 seconds before quitting
        time.sleep(2)

        # Quit the game
        pygame.quit()
        quit()

    # This method handles direction changes based on user input
    def update_snake_direction(self):
        # Check for key presses (events) in the game window
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_UP:  # If UP arrow key is pressed
                    self.change_to = "UP"
                elif event.key == pygame.K_DOWN:  # If DOWN arrow key is pressed
                    self.change_to = "DOWN"
                elif event.key == pygame.K_LEFT:  # If LEFT arrow key is pressed
                    self.change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:  # If RIGHT arrow key is pressed
                    self.change_to = "RIGHT"

        # Prevent snake from moving in the opposite direction instantly
        if self.change_to == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif self.change_to == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    # This method updates the snake's position and checks for collisions with the fruit
    def move_snake(self):
        # Move the snake in the current direction
        if self.direction == "UP":
            self.snake_position[1] -= 10
        elif self.direction == "DOWN":
            self.snake_position[1] += 10
        elif self.direction == "LEFT":
            self.snake_position[0] -= 10
        elif self.direction == "RIGHT":
            self.snake_position[0] += 10

        # Insert the new head position of the snake at the start of the body list
        self.snake_body.insert(0, list(self.snake_position))

        # Check if the snake has eaten the fruit
        if self.snake_position == self.fruit_position:
            self.score += 10  # Increase the score
            self.fruit_spawn = False  # Fruit has been eaten, so stop displaying it
        else:
            # Remove the last part of the snake if no fruit is eaten (normal movement)
            self.snake_body.pop()

        # Spawn a new fruit if the previous one was eaten
        if not self.fruit_spawn:
            self.fruit_position = self.generate_fruit_position()
        self.fruit_spawn = True  # Always keep a fruit on the screen

    # This method draws the snake and the fruit on the screen
    def draw_elements(self):
        self.game_window.fill(self.black)  # Fill the screen with black (background)

        # Draw each block of the snake
        for pos in self.snake_body:
            pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw the fruit
        pygame.draw.rect(
            self.game_window, self.white, pygame.Rect(self.fruit_position[0], self.fruit_position[1], 10, 10)
        )

    # This method checks if the game should end (snake hits wall or itself)
    def check_game_over(self):
        # Check if the snake hits the boundaries (walls)
        if (
            self.snake_position[0] < 0 or self.snake_position[0] > self.window_x - 10
            or self.snake_position[1] < 0 or self.snake_position[1] > self.window_y - 10
        ):
            self.game_over()  # Trigger game over if snake hits the wall

        # Check if the snake collides with its own body
        for block in self.snake_body[1:]:
            if self.snake_position == block:
                self.game_over()  # Trigger game over if snake hits itself

    # This is the main loop that runs the game
    def run(self):
        while True:  # Infinite loop to keep the game running
            self.update_snake_direction()  # Check and update the snake's direction
            self.move_snake()  # Move the snake and check for fruit collisions
            self.check_game_over()  # Check if the game should end
            self.draw_elements()  # Draw the snake and fruit on the screen
            self.show_score(self.white, "times new roman", 20)  # Display the score
            pygame.display.update()  # Refresh the game screen
            self.fps.tick(self.snake_speed)  # Control the game's frame rate

# Start the game by creating an instance of the SnakeGame class and running it
if __name__ == "__main__":
    game = SnakeGame()  # Create the SnakeGame object
    game.run()  # Run the game loop
