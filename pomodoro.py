import pygame
import sys
from button import Button

pygame.init()

# Set the screen size
WIDTH, HEIGHT = 1100, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")

CLOCK = pygame.time.Clock()

# Load music file
pygame.mixer.music.load("assets/thejazzpiano.mp3")
# Load the font
FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 120)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))

# Buttons
START_STOP_BUTTON = Button(pos=(WIDTH/2, HEIGHT/2+100), width=170, height=60, text_input="START", 
                    font=pygame.font.Font("assets/ArialRoundedMTBold.ttf", 22), base_color=(0, 33, 71), 
                    hovering_color=(65, 105, 225), white_background=True)
POMODORO_BUTTON = Button(pos=(WIDTH/2-150, HEIGHT/2-140), width=120, height=30, text_input="Pomodoro", 
                         font=pygame.font.Font("assets/ArialRoundedMTBold.ttf", 22), base_color="#FFFFFF", 
                         hovering_color=(65, 105, 225))
SHORT_BREAK_BUTTON = Button(pos=(WIDTH/2, HEIGHT/2-140), width=120, height=30, text_input="Short Break", 
                            font=pygame.font.Font("assets/ArialRoundedMTBold.ttf", 22), base_color="#FFFFFF", 
                            hovering_color=(65, 105, 225))
LONG_BREAK_BUTTON = Button(pos=(WIDTH/2+150, HEIGHT/2-140), width=120, height=30, text_input="Long Break", 
                           font=pygame.font.Font("assets/ArialRoundedMTBold.ttf", 22), base_color="#FFFFFF", 
                           hovering_color=(65, 105, 225))

# Pomodoro Timer
POMODORO_LENGTH = 1500 
SHORT_BREAK_LENGTH = 300 
LONG_BREAK_LENGTH = 600 

current_seconds = POMODORO_LENGTH
pygame.time.set_timer(pygame.USEREVENT, 1000)
# Variables
started = False
music_paused = False
pomodoro_finished = False 

congratulation_text = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                    # Pause music when stopping
                    pygame.mixer.music.pause()  # Pause music when stopping
                    music_paused = True
                else:
                    started = True
                    if music_paused:
                        # Resume music 
                        pygame.mixer.music.unpause()  
                        music_paused = False
                    else:
                        # Start music from the beginning
                        pygame.mixer.music.play(-1)
            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = POMODORO_LENGTH
                started = False
                # Stop music
                pygame.mixer.music.stop()  # Stop music when clicking Pomodoro
                music_paused = False
                # Remove congratulation message
                congratulation_text = None  
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = SHORT_BREAK_LENGTH
                started = False
                # Stop music when Short Break button is clicked
                pygame.mixer.music.stop()  
                music_paused = False
                # Remove congratulation message
                congratulation_text = None 
            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_BREAK_LENGTH
                started = False
                # Stop music when Long Break button is clicked
                pygame.mixer.music.stop()  
                music_paused = False
                # Remove congratulation message
                congratulation_text = None
            if started:
                START_STOP_BUTTON.text_input = "STOP"
                START_STOP_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            else:
                START_STOP_BUTTON.text_input = "START"
                START_STOP_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1
            if current_seconds <= 0:
                started = False
                # Stop music when timer ends
                pygame.mixer.music.stop()  
                music_paused = False
                # Set the flag to True when a pomodoro session finishes
                pomodoro_finished = True 

    # Color of the screen
    SCREEN.fill((0, 33, 71)) 

    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())

    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    SCREEN.blit(timer_text, timer_text_rect)
    
    # Congratulation message
    if pomodoro_finished:
        congratulation_text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 22).render(
            "Congratulations! You finished a pomodoro!", True, "white")
         # Reset pomodoro_finished flag
        pomodoro_finished = False 

    if congratulation_text:
        congratulation_text_rect = congratulation_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 150))  
        SCREEN.blit(congratulation_text, congratulation_text_rect)

    pygame.display.update()
