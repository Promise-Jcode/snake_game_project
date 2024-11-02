import unittest
from unittest.mock import patch
from snake_game import SnakeGame  # Assuming the game code is saved in snake_game.py


class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        """Set up the SnakeGame instance before each test."""
        self.game = SnakeGame()

    def test_initial_snake_position(self):
        """Test that the snake's initial position is set correctly."""
        self.assertEqual(self.game.snake_position, [100, 50])
        self.assertEqual(self.game.snake_body, [[100, 50], [90, 50], [80, 50], [70, 50]])
        print("test_initial_snake_position passed")

    def test_fruit_generation(self):
        """Test that fruit is generated within the window boundaries."""
        fruit_position = self.game.generate_fruit_position()
        self.assertTrue(0 <= fruit_position[0] < self.game.window_x)
        self.assertTrue(0 <= fruit_position[1] < self.game.window_y)
        print("test_fruit_generation passed")

    def test_snake_direction_change(self):
        """Test that the snake changes direction correctly."""
        # Change to UP
        self.game.change_to = "UP"
        self.game.update_snake_direction()
        self.assertEqual(self.game.direction, "UP")

        # Try changing to DOWN, which should not be allowed (opposite direction)
        self.game.change_to = "DOWN"
        self.game.update_snake_direction()
        self.assertNotEqual(self.game.direction, "DOWN")  # Should still be UP
        print("test_snake_direction_change passed")

    def test_snake_move(self):
        """Test the snake moves in the correct direction."""
        # Initially moving RIGHT
        initial_position = self.game.snake_position.copy()
        self.game.move_snake()
        self.assertEqual(self.game.snake_position[0], initial_position[0] + 10)
        self.assertEqual(self.game.snake_position[1], initial_position[1])

        # Change direction to UP and test movement
        self.game.direction = "UP"
        self.game.move_snake()
        self.assertEqual(self.game.snake_position[1], initial_position[1] - 10)
        print("test_snake_move passed")

    def test_snake_eats_fruit(self):
        """Test that the snake grows and score increases when eating fruit."""
        # Set fruit position directly in front of the snake
        self.game.fruit_position = [self.game.snake_position[0] + 10, self.game.snake_position[1]]
        initial_length = len(self.game.snake_body)

        # Move snake to eat the fruit
        self.game.move_snake()

        # Check that snake length increases and score updates
        self.assertEqual(len(self.game.snake_body), initial_length + 1)
        self.assertEqual(self.game.score, 10)
        print("test_snake_eats_fruit passed")

    def test_snake_hits_wall(self):
        """Test that game over is triggered when snake hits the wall."""
        self.game.snake_position = [0, 0]
        self.game.direction = "LEFT"  # Move the snake out of bounds

        with patch.object(self.game, 'game_over') as mock_game_over:
            self.game.move_snake()
            self.game.check_game_over()
            mock_game_over.assert_called_once()
        print("test_snake_hits_wall passed")

    def test_snake_hits_itself(self):
        """Test that game over is triggered when the snake hits itself."""
        # Create a scenario where the snake will collide with its body
        self.game.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [100, 50]]
        self.game.snake_position = [100, 50]

        with patch.object(self.game, 'game_over') as mock_game_over:
            self.game.check_game_over()
            mock_game_over.assert_called_once()
        print("test_snake_hits_itself passed")


if __name__ == "__main__":
    unittest.main()