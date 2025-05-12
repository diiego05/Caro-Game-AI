import pygame
import sys
import os
from Buttons import Button

class GameMenu:
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.width = screen_width
        self.height = screen_height
        
        # Load assets
        self.load_assets()
        
        # Tạo các nút
        self.create_buttons()
        
        # Biến kiểm soát trạng thái
        self.running = True
        self.game_state = "menu"
        
    def load_assets(self):
        path = os.path.join(os.getcwd(), 'asset')
        
        try:
            self.background = pygame.image.load(os.path.join(path, "background1.jpg")).convert()
            self.background = pygame.transform.scale(self.background, (self.width, self.height))
            self.title_img = pygame.image.load(os.path.join(path, 'text2.png')).convert_alpha()
            self.title_img = pygame.transform.scale(self.title_img, (400, 100))
        except:
            self.background = pygame.Surface((self.width, self.height))
            self.background.fill((0, 0, 0))

        try:
            play_img = pygame.image.load(os.path.join(path, 'PlayBtn.png')).convert_alpha()
            exit_img = pygame.image.load(os.path.join(path, 'ExitBtn.png')).convert_alpha()
            settings_img = pygame.image.load(os.path.join(path, 'OptBtn.png')).convert_alpha()
            
            btn_width, btn_height = 200, 80
            self.play_img = pygame.transform.scale(play_img, (btn_width, btn_height))
            self.exit_img = pygame.transform.scale(exit_img, (btn_width, btn_height))
            self.settings_img = pygame.transform.scale(settings_img, (btn_width, btn_height))
            
            self.play_img_gray = self.play_img
            self.exit_img_gray = self.exit_img
            self.settings_img_gray = self.settings_img
        except Exception as e:
            print(f"Error loading images: {e}")
            btn_width, btn_height = 200, 80
            self.play_img = pygame.Surface((btn_width, btn_height))
            self.play_img.fill((0, 255, 0))
            self.settings_img = pygame.Surface((btn_width, btn_height))
            self.settings_img.fill((255, 255, 0))
            self.exit_img = pygame.Surface((btn_width, btn_height))
            self.exit_img.fill((255, 0, 0))
            
            self.play_img_gray = pygame.Surface((btn_width, btn_height))
            self.play_img_gray.fill((100, 100, 100))
            self.settings_img_gray = pygame.Surface((btn_width, btn_height))
            self.settings_img_gray.fill((100, 100, 100))
            self.exit_img_gray = pygame.Surface((btn_width, btn_height))
            self.exit_img_gray.fill((100, 100, 100))
    
    def create_buttons(self):
        btn_width, btn_height = 200, 80
        spacing = 30
        
        total_height = 3 * btn_height + 2 * spacing
        start_y = (self.height - total_height) // 1.5
        
        self.play_btn = Button(
            (self.width - btn_width) // 2, 
            start_y, 
            self.play_img, 
            self.play_img_gray, 
            1.0
        )
        
        self.settings_btn = Button(
            (self.width - btn_width) // 2, 
            start_y + btn_height + spacing, 
            self.settings_img, 
            self.settings_img_gray, 
            1.0
        )
        
        self.exit_btn = Button(
            (self.width - btn_width) // 2, 
            start_y + 2 * (btn_height + spacing), 
            self.exit_img, 
            self.exit_img_gray, 
            1.0
        )
        
        self.about_font = pygame.font.Font(None, 36)
        self.about_text = self.about_font.render("About Us", True, (255, 255, 255))
        self.about_text_underline = pygame.Surface((self.about_text.get_width(), 2))
        self.about_text_underline.fill((255, 255, 255))
        
        self.about_text_pos = (self.width - self.about_text.get_width() - 20, 
                              self.height - self.about_text.get_height() - 20)
        self.about_underline_pos = (self.about_text_pos[0], 
                                   self.about_text_pos[1] + self.about_text.get_height() + 2)
    
    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))
        
        title_rect = self.title_img.get_rect(center=(self.width//2, self.height//4))
        self.screen.blit(self.title_img, title_rect)
        
        # Vẽ các nút tại vị trí gốc
        self.play_btn.draw(self.screen)
        self.settings_btn.draw(self.screen)
        self.exit_btn.draw(self.screen)
        
        self.screen.blit(self.about_text, self.about_text_pos)
        self.screen.blit(self.about_text_underline, self.about_underline_pos)
        
        pygame.display.flip()
    
    def check_about_click(self, pos):
        about_rect = pygame.Rect(
            self.about_text_pos[0],
            self.about_text_pos[1],
            self.about_text.get_width(),
            self.about_text.get_height() + 2
        )
        return about_rect.collidepoint(pos)
    
    def show_about_screen(self):
        about_running = True
        about_font = pygame.font.Font(None, 32)
        about_lines = [
            "Caro Game - AI Project",
            "Developed by Group 15",
            "Artificial Intelligence Course",
            "Members:",
            "1. Nguyen Duy Cuong - 23110189",
            "2. Nguyen Thanh Tin - 23110340",
            "3. Lam Van Di - 23110191",
            "Click anywhere to return"
        ]
        
        while about_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    about_running = False
                    self.running = False
                    self.game_state = "exit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    about_running = False
            
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0, 0))
            
            about_rect = pygame.Rect(
                self.width // 4,
                self.height // 4,
                self.width // 2,
                self.height // 2
            )
            pygame.draw.rect(self.screen, (50, 50, 50), about_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), about_rect, 2)
            
            line_height = about_font.get_linesize()
            start_y = about_rect.y + 30
            
            for i, line in enumerate(about_lines):
                text = about_font.render(line, True, (255, 255, 255))
                text_rect = text.get_rect(center=(about_rect.centerx, start_y + i * line_height))
                self.screen.blit(text, text_rect)
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return "exit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.check_about_click(event.pos):
                        self.show_about_screen()
            
            if self.play_btn.draw(self.screen):
                self.game_state = "playing"
                self.running = False
            
            if self.settings_btn.draw(self.screen):
                self.game_state = "settings"
                self.running = False
            
            if self.exit_btn.draw(self.screen):
                self.game_state = "exit"
                self.running = False
            
            self.draw_menu()
            
            pygame.time.Clock().tick(60)
        
        return self.game_state