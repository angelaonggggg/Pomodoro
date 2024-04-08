import pygame

class Button():
    def __init__(self, pos=None, width=None, height=None, text_input=None, font=None, base_color=None, hovering_color=None, white_background=False):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = width
        self.height = height
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = pygame.Rect(self.x_pos - self.width/2, self.y_pos - self.height/2, self.width, self.height)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.white_background = white_background

    def update(self, screen):
        if self.white_background:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)  # Draw white background
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)

    def change_color(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
