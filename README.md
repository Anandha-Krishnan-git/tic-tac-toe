
# AI Tic Tac Toe - Hardware Implementation

This project involves the development of an AI-driven **Tic Tac Toe** game using physical hardware, combining capacitive touch sensors and RGB LED strips to create an interactive game experience. Players can interact with the game using touch-sensitive squares on a physical board, while the AI opponent responds by lighting up different LEDs.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [How It Works](#how-it-works)
- [Installation and Setup](#installation-and-setup)
- [Future Improvements](#future-improvements)
- [Acknowledgements](#acknowledgements)

## Project Overview

This AI Tic Tac Toe project integrates **machine intelligence** into a physical gaming experience. It uses capacitive touch sensors to detect player input and RGB LED strips to visually represent the game state. The game supports a human vs AI mode, where the AI uses advanced algorithms to determine optimal moves.

The board consists of 9 squares, each representing a cell in the Tic Tac Toe grid. Capacitive touch sensors detect when a player makes a move, and the AI responds accordingly. The AI uses the Minimax algorithm to strategize its moves.

## Features

- **Human vs AI gameplay**: Players compete against the AI.
- **Capacitive touch interaction**: Touch-sensitive squares to register human input.
- **Dynamic LED feedback**: RGB LEDs light up to display moves (green for human, red for AI).
- **Winning indication**: The winning line blinks three times, with all other LEDs turned off.
- **Real-time AI decisions**: The AI selects optimal moves using Minimax strategy.
- **Compact hardware design**: No need for an IO expander.

## Hardware Components

1. **Capacitive Touch Sensors (x9)** – Detect player touches on the board.
2. **RGB LED Strips (x9)** – Represent the game board and signal moves.
3. **Microcontroller (e.g., Arduino/Raspberry Pi)** – Controls the sensors and LEDs.
4. **Translucent Sheet** – Forms the top layer of the board to allow visibility of the LED lights while detecting touches.
5. **Resistors, Wires, and Power Supply** – Basic electronics for wiring the system.

## Software Components

- **Python (with GPIO Libraries)** – For handling input from touch sensors and controlling the LEDs.
- **AI Logic**: Implemented using the Minimax algorithm for strategic decision-making.
- **Pygame (optional)** – Used during the development phase to simulate AI moves before deploying on the hardware.

## How It Works

1. **Human Turn**: 
   - The player touches one of the nine squares. 
   - The corresponding touch sensor detects the input, and the system lights up the square’s LED in green.

2. **AI Turn**: 
   - After the human move, the AI processes the game state and makes its move using the Minimax algorithm.
   - The AI’s selected square lights up in red.

3. **Win Detection**:
   - The game checks for a win after each move.
   - If a player wins, the winning line's LEDs blink three times while the other LEDs are turned off.

## Installation and Setup

1. **Hardware Setup**:
   - Connect capacitive touch sensors to the input pins of your microcontroller.
   - Wire the RGB LEDs to the output pins.
   - Ensure that the power supply and ground are correctly connected.

2. **Software Setup**:
   - Install necessary libraries (e.g., GPIO for Raspberry Pi).
   - Clone the project repository:  
     ```
     git clone https://github.com/anandha-krishnan/ai-tic-tac-toe-hardware.git
     ```
   - Run the game using the Python script:  
     ```
     python3 ai_tictactoe.py
     ```

## Future Improvements

- Implement a more sophisticated algorithm like Expectimax for a stronger AI.
- Add a scoring system and multiplayer modes.
- Upgrade the board design for a more polished look and feel.

## Acknowledgements

Special thanks to the open-source community for resources on GPIO handling and to [Your Team/University] for support in building the hardware components.
