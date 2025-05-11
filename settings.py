import pygame
import os
from Buttons import Button

class SettingsMenu:
    def __init__(self, screen_width, screen_height, game, current_settings):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.width = screen_width
        self.height = screen_height
        self.game = game
        self.path = os.path.join(os.getcwd(), './asset')
        
        # Khởi tạo settings từ current_settings được truyền vào
        self.settings = current_settings.copy()  # Sao chép để không thay đổi trực tiếp
        
        try:
            background_img = pygame.image.load(os.path.join(self.path, 'background1.jpg')).convert()
            self.background = pygame.transform.smoothscale(background_img, (screen_width, screen_height))
        except pygame.error:
            self.background = pygame.Surface((screen_width, screen_height))
            self.background.fill((0, 0, 0))
        
        self.create_buttons()
        self.running = True
    
    def create_buttons(self):
        try:
            ai_img = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'AI_IMAGE.png')).convert_alpha(), (105, 105))
            ai_img_gray = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'ai_gray.png')).convert_alpha(), (105, 105))
            person_img = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'HUMAN_IMAGE.png')).convert_alpha(), (105, 105))
            person_img_gray = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'human_gray.png')).convert_alpha(), (105, 105))
            h_img = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'h_btn.png')).convert_alpha(), (80, 80))
            h_img_gray = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'h_btn_gray.png')).convert_alpha(), (80, 80))
            m_img = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'm_btn.png')).convert_alpha(), (80, 80))
            m_img_gray = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'm_btn_gray.png')).convert_alpha(), (80, 80))
            e_img = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'e_btn.png')).convert_alpha(), (80, 80))
            e_img_gray = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'e_btn_gray.png')).convert_alpha(), (80, 80))
            exit_img = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'ExitBtn.png')).convert_alpha(), (240, 105))
            self.title_img = pygame.transform.smoothscale(pygame.image.load(
                os.path.join(self.path, 'setting1.png')).convert_alpha(), (300, 100))
        except pygame.error as e:
            print(f"Error loading images: {e}")
            raise
        
        self.ai_btn = Button(550, 220, ai_img, ai_img_gray, 0.8)
        self.person_btn = Button(650, 220, person_img, person_img_gray, 0.8)
        self.h_btn = Button(530, 370, h_img, h_img_gray, 0.8)
        self.m_btn = Button(620, 370, m_img, m_img_gray, 0.8)
        self.e_btn = Button(710, 370, e_img, e_img_gray, 0.8)
        self.exit_btn = Button(550, 590, exit_img, exit_img, 0.8)

        # Khởi tạo trạng thái nút dựa trên current_settings
        if self.settings['ai_first']:
            self.ai_btn.disable_button()
            self.person_btn.enable_button()
        else:
            self.person_btn.disable_button()
            self.ai_btn.enable_button()
        
        if self.settings['difficulty'] == 'hard':  # Replace "hard" with "SA"
            self.h_btn.disable_button()
            self.m_btn.enable_button()
            self.e_btn.enable_button()
        elif self.settings['difficulty'] == 'medium':
            self.m_btn.disable_button()
            self.h_btn.enable_button()
            self.e_btn.enable_button()
     
        else:  # easy
            self.e_btn.disable_button()
            self.h_btn.enable_button()
            self.m_btn.enable_button()
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        
        title_rect = self.title_img.get_rect(center=(self.width / 2, 100))
        self.screen.blit(self.title_img, title_rect)

        font = pygame.font.Font('freesansbold.ttf', 20)
        player_label = font.render('Who goes first?', True, (255, 255, 255))
        player_label_rect = player_label.get_rect(center=(650, 200))
        self.screen.blit(player_label, player_label_rect)

        mode_label = font.render('Select mode', True, (255, 255, 255))
        mode_label_rect = mode_label.get_rect(center=(650, 350))
        self.screen.blit(mode_label, mode_label_rect)

        self.ai_btn.draw(self.screen)
        self.person_btn.draw(self.screen)
        self.h_btn.draw(self.screen)
        self.m_btn.draw(self.screen)
        self.e_btn.draw(self.screen)
        self.exit_btn.draw(self.screen)

        pygame.display.flip()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return "exit", self.settings
                
                if self.ai_btn.draw(self.screen):
                    self.ai_btn.disable_button()
                    self.person_btn.enable_button()
                    self.settings['ai_first'] = True
                    self.game.set_ai_turn(1)
                
                if self.person_btn.draw(self.screen):
                    self.person_btn.disable_button()
                    self.ai_btn.enable_button()
                    self.settings['ai_first'] = False
                    self.game.set_ai_turn(2)
                
                if self.h_btn.draw(self.screen):  # Update button logic
                    self.h_btn.disable_button()
                    self.m_btn.enable_button()
                    self.e_btn.enable_button()
                    self.settings['difficulty'] = 'hard'  # Add Backtracking
                    self.game.change_hard_ai("hard")
                
                if self.m_btn.draw(self.screen):
                    self.m_btn.disable_button()
                    self.h_btn.enable_button()
                    self.e_btn.enable_button()
                    self.settings['difficulty'] = 'medium'
                    self.game.change_hard_ai("medium")
                
                if self.e_btn.draw(self.screen):
                    self.e_btn.disable_button()
                    self.h_btn.enable_button()
                    self.m_btn.enable_button()
                    self.settings['difficulty'] = 'easy'
                    self.game.change_hard_ai("easy")
                
                if self.exit_btn.draw(self.screen):
                    self.running = False
                    return "back", self.settings
            
            self.draw()
            pygame.time.Clock().tick(60)
        
        return "back", self.settings