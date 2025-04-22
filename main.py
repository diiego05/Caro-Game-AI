from turtle import Screen
import Buttons as button
import pygame
import sys
import caro
import os
from agent import Agent
from menu import GameMenu
from settings import SettingsMenu

# -------------------------Setup----------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (77, 199, 61)
RED = (199, 36, 55)
BLUE = (68, 132, 222)

XO = 'X'
FPS = 120
ROWNUM = 18
COLNUM = 20
winning_condition = 5

is_developer_mode = False
# is_developer_mode = True

dev_mode_setup = {
    'ai_1': 'X',
    'ai_2': 'O',
    'ai_1_depth': 1,
    'ai_2_depth': 3,
    'start': False,
}

# Biến toàn cục để lưu cài đặt
game_settings = {
    'ai_first': False,
    'difficulty': 'medium'
}

def main():
    pygame.init()
    Window_size = [1280, 720]
    
    while True:
        menu = GameMenu(Window_size[0], Window_size[1])
        menu_result = menu.run()
        
        if menu_result == "exit":
            pygame.quit()
            sys.exit()
        elif menu_result == "playing":
            my_game = caro.Caro(ROWNUM, COLNUM, winning_condition, XO)
            my_game.use_ai(True)
            # Áp dụng cài đặt đã lưu
            my_game.change_hard_ai(game_settings['difficulty'])
            my_game.set_ai_turn(1 if game_settings['ai_first'] else 2)
            run_main_game(my_game)
        elif menu_result == "settings":
            my_game = caro.Caro(ROWNUM, COLNUM, winning_condition, XO)
            settings = SettingsMenu(Window_size[0], Window_size[1], my_game, game_settings)
            settings_result, new_settings = settings.run()
            
            if settings_result == "back":
                # Cập nhật cài đặt toàn cục
                game_settings.update(new_settings)
                continue
            elif settings_result == "exit":
                pygame.quit()
                sys.exit()
            else:
                # Cập nhật cài đặt và chạy game
                game_settings.update(new_settings)
                my_game.use_ai(True)
                my_game.change_hard_ai(game_settings['difficulty'])
                my_game.set_ai_turn(1 if game_settings['ai_first'] else 2)
                run_main_game(my_game)

def run_main_game(my_game):
    difficulty = my_game.hard_ai
    if difficulty == 1:
        algorithm = "greedy"
    elif difficulty == 2:
        algorithm = "genetic"
    elif difficulty == 3:
        algorithm = "minimax"
    agent = Agent(max_depth=my_game.hard_ai, XO=my_game.get_current_XO_for_AI(),algorithm=algorithm)
    agent1 = Agent(max_depth=dev_mode_setup['ai_1_depth'], XO=dev_mode_setup['ai_1'],algorithm=algorithm)  
    agent2 = Agent(max_depth=dev_mode_setup['ai_2_depth'], XO=dev_mode_setup['ai_2'],algorithm= algorithm)

    Window_size = [1280, 720]
    my_len_min = min(900/COLNUM, (720) / ROWNUM)
    MARGIN = my_len_min/15
    my_len_min = min((900 - MARGIN)/COLNUM, (720 - MARGIN) / ROWNUM)
    my_len_min = my_len_min - MARGIN
    WIDTH = my_len_min
    HEIGHT = my_len_min

    Screen = pygame.display.set_mode(Window_size)
    path = os.path.join(os.getcwd(), './asset')

    # ------------------------------Load asset----------------------------------------
    x_img = pygame.transform.smoothscale(pygame.image.load(
        path + "/X_caro.png").convert_alpha(), (my_len_min, my_len_min))
    o_img = pygame.transform.smoothscale(pygame.image.load(
        path + "/O_caro.png").convert_alpha(), (my_len_min, my_len_min))
    start_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/start_btn.png').convert_alpha(), (240, 105))
    exit_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/exit_btn.png').convert_alpha(), (240, 105))
    replay_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/replay_btn.png').convert_alpha(), (240, 105))
    undo_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/undo_btn.png').convert_alpha(), (240, 105))
    pvp_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/player_vs_player.jpg').convert_alpha(), (105, 105))
    pvp_img_gray = pygame.transform.smoothscale(pygame.image.load(
        path + '/player_vs_player_gray.jpg').convert_alpha(), (105, 105))
    aivp_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/ai_vs_player.jpg').convert_alpha(), (105, 105))
    aivai_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/ai_vs_ai.png').convert_alpha(), (105, 105))
    aivp_img_gray = pygame.transform.smoothscale(pygame.image.load(
        path + '/ai_vs_player_gray.jpg').convert_alpha(), (105, 105))
    ai_thinking_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/ai_thinking.png').convert_alpha(), (105, 105))
    ai_thinking_img_gray = pygame.transform.smoothscale(pygame.image.load(
        path + '/ai_thinking_gray.png').convert_alpha(), (105, 105))
    icon_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/old/icon.jpg').convert_alpha(), (20, 20))
    logo_img = pygame.transform.smoothscale(pygame.image.load(
        path + '/logo.jpg').convert_alpha(), (240, 105))

    start_button = button.Button(970, 200, start_img, start_img, 0.8)
    replay_button = button.Button(970, 575, replay_img, replay_img, 0.8)
    exit_button = button.Button(970, 485, exit_img, exit_img, 0.8)
    undo_button = button.Button(970, 395, undo_img, undo_img, 0.8)
    ai_thinking_btn = button.Button(
        1020, 30, ai_thinking_img, ai_thinking_img_gray, 0.8)
    pvp_btn = button.Button(1075, 145, pvp_img, pvp_img_gray, 0.8)
    aivp_btn = button.Button(970, 145, aivp_img, aivp_img_gray, 0.8)
    aivai_btn = button.Button(1020, 250, aivai_img, aivp_img_gray, 0.8)
    """ 
    logo_btn = button.Button(990, 660, logo_img, logo_img, 0.6)
    """

    if my_game.is_use_ai:
        aivp_btn.disable_button()
        pvp_btn.enable_button()
    else:
        pvp_btn.disable_button()
        aivp_btn.enable_button()
    ai_thinking_btn.disable_button()

    if is_developer_mode:
        aivp_btn.disable_button()
        pvp_btn.disable_button()
        start_button.enable_button()

    pygame.display.set_caption('Caro game by nhóm 12 Trí tuệ nhân tạo')
    pygame.display.set_icon(icon_img)

    done = False
    status = None
    clock = pygame.time.Clock()

    def logo():
        font = pygame.font.Font('freesansbold.ttf', 36)
        text = font.render('By AI - nhóm 12', True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (1050, 700)
        Screen.blit(text, textRect)
        if is_developer_mode:
            font = pygame.font.Font('freesansbold.ttf', 36)
            text = font.render('Developer_Mode', True, WHITE, BLACK)
            textRect = text.get_rect()
            textRect.center = (1080, 160)
            Screen.blit(text, textRect)

    def draw(this_game: caro.Caro, this_screen):
        logo()
        board_background = (245, 222, 179)
        board_width = (MARGIN + WIDTH) * COLNUM + MARGIN
        board_height = (MARGIN + HEIGHT) * ROWNUM + MARGIN
        pygame.draw.rect(this_screen, board_background, [MARGIN, MARGIN, board_width - MARGIN * 2, board_height - MARGIN * 2])
        line_color = (50, 50, 50)
        line_thickness = 1
        
        for column in range(COLNUM + 1):
            start_pos = (MARGIN + (MARGIN + WIDTH) * column, MARGIN)
            end_pos = (MARGIN + (MARGIN + WIDTH) * column, MARGIN + (MARGIN + HEIGHT) * ROWNUM)
            pygame.draw.line(this_screen, line_color, start_pos, end_pos, line_thickness)
        
        for row in range(ROWNUM + 1):
            start_pos = (MARGIN, MARGIN + (MARGIN + HEIGHT) * row)
            end_pos = (MARGIN + (MARGIN + WIDTH) * COLNUM, MARGIN + (MARGIN + HEIGHT) * row)
            pygame.draw.line(this_screen, line_color, start_pos, end_pos, line_thickness)
        
        star_point_color = (50, 50, 50)
        star_point_radius = 3
        star_points = [
            (ROWNUM // 4, COLNUM // 4),
            (ROWNUM // 4, COLNUM * 3 // 4),
            (ROWNUM * 3 // 4, COLNUM // 4),
            (ROWNUM * 3 // 4, COLNUM * 3 // 4),
            (ROWNUM // 2, COLNUM // 2)
        ]
        
        for point in star_points:
            center = (
                int(MARGIN + (MARGIN + WIDTH) * point[1] + WIDTH / 2),
                int(MARGIN + (MARGIN + HEIGHT) * point[0] + HEIGHT / 2)
            )
            pygame.draw.circle(this_screen, star_point_color, center, star_point_radius)
        
        for row in range(ROWNUM):
            for column in range(COLNUM):
                img_pos = (
                    int(MARGIN + (MARGIN + WIDTH) * column),
                    int(MARGIN + (MARGIN + HEIGHT) * row)
                )
                
                if this_game.grid[row][column] == 'X':
                    this_screen.blit(x_img, img_pos)
                elif this_game.grid[row][column] == 'O':
                    this_screen.blit(o_img, img_pos)
        
        if len(this_game.last_move) > 0:
            last_move_row, last_move_col = this_game.last_move[-1][0], this_game.last_move[-1][1]
            center = (
                int(MARGIN + (MARGIN + WIDTH) * last_move_col + WIDTH / 2),
                int(MARGIN + (MARGIN + HEIGHT) * last_move_row + HEIGHT / 2)
            )
            pygame.draw.circle(this_screen, (255, 0, 0), center, 5)
            
    def re_draw():
        logo()
        Screen.fill(BLACK)
        for row in range(ROWNUM):
            for column in range(COLNUM):
                color = WHITE
                pygame.draw.rect(Screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])

    def Undo(self: caro.Caro):
        re_draw()
        if self.is_use_ai:
            if len(self.last_move) > 2:
                last_move = self.last_move[-1]
                last_move_2 = self.last_move[-2]
                self.last_move.pop()
                self.last_move.pop()
                row = int(last_move[0])
                col = int(last_move[1])
                row2 = int(last_move_2[0])
                col2 = int(last_move_2[1])
                self.grid[row][col] = '.'
                self.grid[row2][col2] = '.'
                draw(my_game, Screen)
        else:
            if len(self.last_move) > 0:
                last_move = self.last_move[-1]
                self.last_move.pop()
                row = int(last_move[0])
                col = int(last_move[1])
                self.grid[row][col] = '.'
                if self.XO == 'X':
                    self.XO = 'O'
                else:
                    self.XO = 'X'
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                draw(my_game, Screen)

    def checking_winning(status):
        if status == 2:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('Draw', True, GREEN, BLUE)
            textRect = text.get_rect()
            textRect.center = (int(Window_size[0]/2), int(Window_size[1]/2))
            Screen.blit(text, textRect)
        if status == 0:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('X wins', True, RED, GREEN)
            textRect = text.get_rect()
            textRect.center = (int(Window_size[0]/2), int(Window_size[1]/2))
            Screen.blit(text, textRect)
        if status == 1:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('O wins', True, BLUE, GREEN)
            textRect = text.get_rect()
            textRect.center = (int(Window_size[0]/2), int(Window_size[1]/2))
            Screen.blit(text, textRect)

    def draw_labels(ai_1_algorithm, ai_2_algorithm):
        font = pygame.font.Font('freesansbold.ttf', 20)
        # Label for AI 1 (X)
        ai_1_label = font.render(f"X: {ai_1_algorithm}", True, WHITE)  # Xóa tham số nền
        ai_1_label_rect = ai_1_label.get_rect()
        ai_1_label_rect.center = (aivai_btn.rect.left - 100, aivai_btn.rect.centery)
        Screen.blit(ai_1_label, ai_1_label_rect)

        # Label for AI 2 (O)
        ai_2_label = font.render(f"O: {ai_2_algorithm}", True, WHITE)  # Xóa tham số nền
        ai_2_label_rect = ai_2_label.get_rect()
        ai_2_label_rect.center = (aivai_btn.rect.right + 100, ai_2_label_rect.centery + 280)
        Screen.blit(ai_2_label, ai_2_label_rect)

    # Thực hiện nước đi đầu tiên của AI nếu được chọn
    if my_game.is_use_ai and my_game.ai_turn == 1 and len(my_game.last_move) == 0:
        best_move = agent.get_move(my_game)
        my_game.make_move(best_move[0], best_move[1])

    while not done:
        for event in pygame.event.get():
            if undo_button.draw(Screen):
                Undo(my_game)
            if exit_button.draw(Screen):
                done = True
            if replay_button.draw(Screen):
                my_game.reset()
                re_draw()

                # Reinitialize buttons
                start_button = button.Button(970, 200, start_img, start_img, 0.8)
                replay_button = button.Button(970, 575, replay_img, replay_img, 0.8)
                exit_button = button.Button(970, 485, exit_img, exit_img, 0.8)
                undo_button = button.Button(970, 395, undo_img, undo_img, 0.8)
                ai_thinking_btn = button.Button(1020, 30, ai_thinking_img, ai_thinking_img_gray, 0.8)
                pvp_btn = button.Button(1075, 145, pvp_img, pvp_img_gray, 0.8)
                aivp_btn = button.Button(970, 145, aivp_img, aivp_img_gray, 0.8)
                aivai_btn = button.Button(1020, 250, aivai_img, aivp_img_gray, 0.8)

                # Reinitialize agents for AI vs AI mode
                if aivai_btn.is_disable:
                    agent1 = Agent(max_depth=dev_mode_setup['ai_1_depth'], XO=dev_mode_setup['ai_1'], algorithm=ai_1_algorithm)
                    agent2 = Agent(max_depth=dev_mode_setup['ai_2_depth'], XO=dev_mode_setup['ai_2'], algorithm=ai_2_algorithm)
                    # Automatically let AI play against each other
                    while my_game.get_winner() == -1:
                        if my_game.turn == 1:
                            best_move = agent1.get_move(my_game)
                        else:
                            best_move = agent2.get_move(my_game)
                        my_game.make_move(best_move[0], best_move[1])
                        draw(my_game, Screen)
                        pygame.display.update()
                # Apply the first AI move if needed
                if my_game.is_use_ai and my_game.ai_turn == 1:
                    best_move = agent.get_move(my_game)
                    my_game.make_move(best_move[0], best_move[1])
            if not is_developer_mode:
                if not my_game.is_use_ai:
                    pass
                else:
                    if my_game.turn == my_game.ai_turn and my_game.get_winner() == -1:
                        best_move = agent.get_move(my_game)
                        my_game.make_move(best_move[0], best_move[1])
                        draw(my_game, Screen)
                        ai_thinking_btn.disable_button()
                        ai_thinking_btn.re_draw(Screen)
                        status = my_game.get_winner()
                        checking_winning(status)
                if pvp_btn.draw(Screen):
                    my_game.use_ai(False)
                    pvp_btn.disable_button()
                    aivp_btn.enable_button()
                if aivp_btn.draw(Screen):
                    my_game.use_ai(True)
                    aivp_btn.disable_button()
                    pvp_btn.enable_button()
                    agent = Agent(max_depth=my_game.hard_ai, XO=my_game.get_current_XO_for_AI(),algorithm = algorithm)
                    
                if aivai_btn.draw(Screen):
                    # Display combo boxes to select algorithms for AI 1 and AI 2
                    import tkinter as tk
                    from tkinter import ttk
                    from PIL import Image, ImageTk

                    root = tk.Tk()
                    root.withdraw()  # Hide the root window

                    # Create a new window for combo boxes
                    combo_window = tk.Toplevel(root)
                    combo_window.title("Select AI Algorithms")

                    bg_image = Image.open(r"D:\Trí tuệ nhân tạo\ABC\Caro-Game-AI\Caro-Game-AI\asset\background1.jpg")
                    bg_photo = ImageTk.PhotoImage(bg_image)
                    bg_label = tk.Label(combo_window, image=bg_photo)
                    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                    background_label = tk.Label(combo_window, image=bg_photo)
                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                    pixel_font = ("Courier New", 12, "bold")
                    label_fg = "#00FFFF"

                    window_bg = "#000000"  # Replace with a valid color code (e.g., black)
                    # Center the window on the screen
                    window_width, window_height = 300, 300
                    screen_width = combo_window.winfo_screenwidth()
                    screen_height = combo_window.winfo_screenheight()
                    x_position = (screen_width // 2) - (window_width // 2)
                    y_position = (screen_height // 2) - (window_height // 2)
                    combo_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

                    # Options for algorithms
                    algorithms = ["greedy", "genetic", "minimax"]

                    # Create a frame for better organization
                    frame = tk.Frame(combo_window, bg="#1E1E1E")  # Nền tối giống menu chính
                    frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=250)

                    # Title label
                    tk.Label(frame, text="Select AI Algorithms", font=("Courier New", 16, "bold"), fg="#00FFFF", bg="#1E1E1E").pack(pady=10)

                    # AI 1 Algorithm
                    tk.Label(frame, text="AI 1 Algorithm (X):", font=("Courier New", 12, "bold"), fg="#00FF00", bg="#1E1E1E").pack(anchor="w", padx=20, pady=5)
                    ai_1_combo = ttk.Combobox(frame, values=algorithms, state="readonly", font=("Courier New", 12))
                    ai_1_combo.set("minimax")
                    ai_1_combo.pack(fill="x", padx=20, pady=5)

                    # AI 2 Algorithm
                    tk.Label(frame, text="AI 2 Algorithm (O):", font=("Courier New", 12, "bold"), fg="#FF4500", bg="#1E1E1E").pack(anchor="w", padx=20, pady=5)
                    ai_2_combo = ttk.Combobox(frame, values=algorithms, state="readonly", font=("Courier New", 12))
                    ai_2_combo.set("minimax")
                    ai_2_combo.pack(fill="x", padx=20, pady=5)

                    def on_submit():
                        nonlocal ai_1_algorithm, ai_2_algorithm
                        ai_1_algorithm = ai_1_combo.get()
                        ai_2_algorithm = ai_2_combo.get()
                        combo_window.destroy()

                    # Submit button
                    submit_btn = tk.Button(frame, text="Submit", command=on_submit, font=("Courier New", 12, "bold"), bg="#444", fg="white",
                                            activebackground="#00FFFF", activeforeground="black", relief="raised", bd=3)
                    submit_btn.pack(pady=15)

                    root.wait_window(combo_window)

                    # Validate input and set default values if invalid
                    valid_algorithms = {"greedy", "genetic", "minimax"}
                    if ai_1_algorithm not in valid_algorithms:
                        ai_1_algorithm = "minimax"
                    if ai_2_algorithm not in valid_algorithms:
                        ai_2_algorithm = "minimax"

                    my_game.use_ai(True)
                    aivai_btn.disable_button()
                    aivp_btn.enable_button()
                    pvp_btn.enable_button()
                    dev_mode_setup['start'] = True
                    ai_thinking_btn.enable_button()
                    agent1 = Agent(
                        max_depth=3 if ai_1_algorithm == "minimax" else dev_mode_setup['ai_1_depth'],
                        XO=dev_mode_setup['ai_1'],
                        algorithm=ai_1_algorithm
                    )
                    agent2 = Agent(
                        max_depth=3 if ai_2_algorithm == "minimax" else dev_mode_setup['ai_2_depth'],
                        XO=dev_mode_setup['ai_2'],
                        algorithm=ai_2_algorithm
                    )

                    # Draw labels after algorithms are selected
                    draw_labels(ai_1_algorithm, ai_2_algorithm)

                    # Automatically let AI play against each other
                    while my_game.get_winner() == -1:
                        if my_game.turn == 1:
                            best_move = agent1.get_move(my_game)
                        else:
                            best_move = agent2.get_move(my_game)
                        my_game.make_move(best_move[0], best_move[1])
                        draw(my_game, Screen)
                        pygame.display.update()
                if ai_thinking_btn.draw(Screen):
                    pass
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = int(pos[0] // (WIDTH + MARGIN))
                    row = int(pos[1] // (HEIGHT + MARGIN))
                    if col < COLNUM and row < ROWNUM:
                        my_game.make_move(row, col)
                    status = my_game.get_winner()
                    if my_game.is_use_ai and my_game.turn == my_game.ai_turn:
                        ai_thinking_btn.enable_button()
                        ai_thinking_btn.re_draw(Screen)
                        draw(my_game, Screen)
            else:
                if start_button.draw(Screen):
                    if dev_mode_setup['start'] == False:
                        dev_mode_setup['start'] = True
                        ai_thinking_btn.enable_button()
                    else:
                        dev_mode_setup['start'] = False
                        ai_thinking_btn.disable_button()
                ai_thinking_btn.re_draw(Screen)
                if my_game.get_winner() == -1 and dev_mode_setup['start']:
                    if my_game.turn == 1:
                        best_move = agent1.get_move(my_game)
                        my_game.make_move(best_move[0], best_move[1])
                        status = my_game.get_winner()
                    else: 
                        best_move = agent2.get_move(my_game)
                        my_game.make_move(best_move[0], best_move[1])
                        status = my_game.get_winner()
        
        draw(my_game, Screen)
        checking_winning(status)
        clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    main()
