import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        # Inisialisasi atribut dari button
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set properties of the button
        self.width, self.height = 500, 60
        self.button_color = "red"
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("arcadenormal", 48)

        # Membangun button dan memposisikan button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (480, 820)

        # Message di button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Memunculkan teks dari Message
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (480, 820)

    def draw_button(self):
        # draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)