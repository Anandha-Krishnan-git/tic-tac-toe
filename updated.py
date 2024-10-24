
#updted code with hardware setup script and minimax algorithm
#4 sep 19:00
import RPi.GPIO as GPIO
import time
from smbus2 import SMBus
from gpiozero import MCP23017

# Define the game board
board = [' '] * 9

# Define constants
HUMAN = 'X'
AI = 'O'

# GPIO Setup
GPIO.setmode(GPIO.BCM)

# Initialize MCP23017
mcp = MCP23017(address=0x20)

# Define MCP23017 GPIO pins
HUMAN_LED_PINS = [mcp.pin(i, "out") for i in range(8, 16)]  # Pins 8-15 for Yellow LEDs (Human)
TOUCH_SENSOR_PINS = [mcp.pin(i, "in") for i in range(0, 8)]  # Pins 0-7 for Touch Sensors

# Define Raspberry Pi GPIO pins
HUMAN_LED_PINS.append(17)  # Pin GPIO 17 for Square 9 Yellow LED
AI_LED_PINS = [27, 22, 5, 6, 13, 19, 26, 12, 23]  # GPIO pins for Red LEDs (AI)
TOUCH_SENSOR_PINS.append(4)  # GPIO 4 for Square 9 Touch Sensor

# Setup pins
for pin in AI_LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

# Game Logic
def check_winner(board, player):
    # Winning combinations
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def minimax(board, depth, is_ai):
    # Base cases: check if the game is over
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if ' ' not in board:
        return 0

    if is_ai:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = AI
    return move

def player_move(index):
    if board[index] == ' ':
        board[index] = HUMAN
        GPIO.output(HUMAN_LED_PINS[index], GPIO.HIGH)  # Turn on Human LED

def reset_leds():
    for pin in HUMAN_LED_PINS + AI_LED_PINS:
        if isinstance(pin, MCP23017.pin):
            pin.off()
        else:
            GPIO.output(pin, GPIO.LOW)

# Main loop
try:
    while True:
        reset_leds()
        for i, pin in enumerate(TOUCH_SENSOR_PINS):
            if isinstance(pin, MCP23017.pin):
                if pin.is_pressed:
                    player_move(i)
                    if check_winner(board, HUMAN):
                        # Blink winning combination
                        for _ in range(3):
                            reset_leds()
                            time.sleep(0.5)
                            for index in range(9):
                                if board[index] == HUMAN:
                                    GPIO.output(HUMAN_LED_PINS[index], GPIO.HIGH)
                            time.sleep(0.5)
                        break
                    else:
                        ai_index = ai_move()
                        GPIO.output(AI_LED_PINS[ai_index], GPIO.HIGH)  # Turn on AI LED
                        if check_winner(board, AI):
                            # Blink winning combination
                            for _ in range(3):
                                reset_leds()
                                time.sleep(0.5)
                                for index in range(9):
                                    if board[index] == AI:
                                        GPIO.output(AI_LED_PINS[index], GPIO.HIGH)
                                time.sleep(0.5)
                        break

except KeyboardInterrupt:
    GPIO.cleanup()

