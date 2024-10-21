# Pong Game 🎮

A simple, classic Pong game built using Python and the `turtle` module. This version includes scorekeeping, ball speed progression, and boundary limitations for paddle movement.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Controls](#game-controls)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

This is a modern take on the classic Pong game, developed using Python's `turtle` module. The game supports two players, keeps track of the score, and increases the ball's speed as the game progresses. The paddles are controlled via keyboard input, and the game gets progressively harder after each successful hit.

## Features

- **Two-player**: Supports two players with individual paddle controls.
- **Progressive Difficulty**: The ball speeds up after every paddle hit.
- **Scorekeeping**: The game tracks the score for both players and displays it on the screen.
- **Boundary Detection**: Paddles cannot move outside the screen boundaries.
- **Ball Reset**: The ball resets to the center after a player scores, and the speed resets.

## Installation

### Prerequisites

- Python 3.x installed on your machine.

### Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/NikolaosAI/Pong_Game.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Pong_Game
   ```

3. Run the game:

   ```bash
   python main.py
   ```

That’s it! You're ready to play.

## How to Play

1. Run the `main.py` script to start the game.
2. Player 1 controls the left paddle using the `W` and `S` keys.
3. Player 2 controls the right paddle using the `Up` and `Down` arrow keys.
4. The goal is to hit the ball with your paddle and prevent it from passing your side. When the ball passes a paddle, the other player scores a point.
5. The game gets progressively harder as the ball speeds up after each paddle hit.

## Game Controls

| Player         | Controls                |
|----------------|-------------------------|
| Left Paddle    | `W` (Up), `S` (Down)    |
| Right Paddle   | `Up Arrow` (Up), `Down Arrow` (Down) |

## Project Structure

```
pong-game/
│
├── paddle.py           # Paddle class handling the movement and positioning
├── ball.py             # Ball class handling ball movement, bouncing, and speed
├── scoreboard.py       # Scoreboard class for tracking and displaying the score
├── main.py             # Main game loop and logic
└── README.md           # Project documentation
```

### Explanation of Classes

- **Paddle Class (`paddle.py`)**:
    - Handles the paddle's movement and boundary detection.
    - Ensures the paddle cannot move out of the top or bottom edges of the screen.

- **Ball Class (`ball.py`)**:
    - Controls the ball's movement, including bouncing off walls and paddles.
    - Increases the ball's speed by 10% every time it bounces off a paddle.
    - Resets the ball to the center of the screen after a point is scored.

- **Scoreboard Class (`scoreboard.py`)**:
    - Tracks and displays the scores for both players.
    - Updates the scoreboard every time a player scores a point.

## Future Enhancements

Some features that could be added in future versions:

- **AI Paddle**: Implement a computer-controlled paddle for single-player mode.
- **Sound Effects**: Add sound effects for ball collisions and scoring.
- **Game Menu**: Create a main menu with options to restart the game or change settings.
- **Difficulty Levels**: Add selectable difficulty levels to change how fast the ball increases speed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
