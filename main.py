from turtle import Screen
import Buttons as button
import pygame
import sys
import caro
import os
from agent import Agent

# -------------------------Setup----------------------------
# Định nghĩa màu

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (77, 199, 61)
RED = (199, 36, 55)
BLUE = (68, 132, 222)

# Kí hiệu lúc ban đầu
XO = 'X'
FPS = 120
# Số hàng, cột
ROWNUM = 18
COLNUM = 20
# Số dòng thắng
winning_condition = 5

# developer_mode: ai vs ai
# Đặt is_developer_mode = True nếu muốn cho ai đấu với ai

is_developer_mode = False
# is_developer_mode = True

dev_mode_setup = {
    'ai_1': 'X',
    'ai_2': 'O',
    'ai_1_depth': 1,
    'ai_2_depth': 3,
    'start': False,
}
# init game and ai
my_game = caro.Caro(ROWNUM, COLNUM, winning_condition, XO)

agent = Agent(max_depth=my_game.hard_ai,
                       XO=my_game.get_current_XO_for_AI())

agent1 = Agent(max_depth=dev_mode_setup['ai_1_depth'],
                       XO=dev_mode_setup['ai_1'])
agent2 = Agent(max_depth=dev_mode_setup['ai_2_depth'],
                       XO=dev_mode_setup['ai_2'])

Window_size = [1280, 720]


my_len_min = min(900/COLNUM, (720) / ROWNUM)
# Độ dày đường kẻ
MARGIN = my_len_min/15
my_len_min = min((900 - MARGIN)/COLNUM, (720 - MARGIN) / ROWNUM)
my_len_min = my_len_min - MARGIN
# Chiều dài, rộng mỗi ô
WIDTH = my_len_min
HEIGHT = my_len_min

Screen = pygame.display.set_mode(Window_size)
# path = "Caro/asset"
path = os.getcwd()
path = os.path.join(path, './asset')

# ------------------------------Load asset----------------------------------------
x_img = pygame.transform.smoothscale(pygame.image.load(
    path + "/X_caro.png").convert_alpha(), (my_len_min, my_len_min))
o_img = pygame.transform.smoothscale(pygame.image.load(
    path + "/O_caro.png").convert_alpha(), (my_len_min, my_len_min))
# load button images
start_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/start_btn.png').convert_alpha(), (240, 105))
exit_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/exit_btn.png').convert_alpha(), (240, 105))
replay_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/replay_btn.png').convert_alpha(), (240, 105))
undo_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/undo_btn.png').convert_alpha(), (240, 105))
ai_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/AI_IMAGE.png').convert_alpha(), (105, 105))
person_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/HUMAN_IMAGE.png').convert_alpha(), (105, 105))
ai_img_gray = pygame.transform.smoothscale(pygame.image.load(
    path + '/ai_gray.png').convert_alpha(), (105, 105))
person_img_gray = pygame.transform.smoothscale(pygame.image.load(
    path + '/human_gray.png').convert_alpha(), (105, 105))
h_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/h_btn.png').convert_alpha(), (80, 80))
h_img_gray = pygame.transform.smoothscale(pygame.image.load(
    path + '/h_btn_gray.png').convert_alpha(), (80, 80))
m_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/m_btn.png').convert_alpha(), (80, 80))
m_img_gray = pygame.transform.smoothscale(pygame.image.load(
    path + '/m_btn_gray.png').convert_alpha(), (80, 80))
e_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/e_btn.png').convert_alpha(), (80, 80))
e_img_gray = pygame.transform.smoothscale(pygame.image.load(
    path + '/e_btn_gray.png').convert_alpha(), (80, 80))
pvp_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/player_vs_player.jpg').convert_alpha(), (105, 105))
pvp_img_gray = pygame.transform.smoothscale(pygame.image.load(
    path + '/player_vs_player_gray.jpg').convert_alpha(), (105, 105))
aivp_img = pygame.transform.smoothscale(pygame.image.load(
    path + '/ai_vs_player.jpg').convert_alpha(), (105, 105))
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
# create button instances
start_button = button.Button(970, 200, start_img, start_img, 0.8)
replay_button = button.Button(970, 575, replay_img, replay_img, 0.8)
exit_button = button.Button(970, 485, exit_img, exit_img, 0.8)
undo_button = button.Button(970, 395, undo_img, undo_img, 0.8)
ai_btn = button.Button(970, 305, ai_img, ai_img_gray, 0.8)
person_btn = button.Button(1075, 305, person_img, person_img_gray, 0.8)
h_btn = button.Button(1100, 235, h_img, h_img_gray, 0.8)
m_btn = button.Button(1035, 235, m_img, m_img_gray, 0.8)
e_btn = button.Button(970, 235, e_img, e_img_gray, 0.8)
ai_thinking_btn = button.Button(
    1020, 30, ai_thinking_img, ai_thinking_img_gray, 0.8)
pvp_btn = button.Button(1075, 145, pvp_img, pvp_img_gray, 0.8)
aivp_btn = button.Button(970, 145, aivp_img, aivp_img_gray, 0.8)
logo_btn = button.Button(990, 660, logo_img, logo_img, 0.6)

person_btn.disable_button()
m_btn.disable_button()
pvp_btn.disable_button()
ai_thinking_btn.disable_button()
if (is_developer_mode == True):
    aivp_btn.disable_button()
    pvp_btn.disable_button()
    ai_btn.disable_button()
    person_btn.disable_button()
    h_btn.disable_button()
    m_btn.disable_button()
    e_btn.disable_button()
    ai_thinking_btn.disable_button()

pygame.display.set_caption('Caro game by nhóm 12 Trí tuệ nhân tạo')
pygame.display.set_icon(icon_img)
pygame.init()


# Loop until the user clicks the close button.
done = False
status = None
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ----------------------- Function ------------------------------------


def logo():
    font = pygame.font.Font('freesansbold.ttf', 36)
    text = font.render('By AI - nhóm 12', True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (1100, 700)
    Screen.blit(text, textRect)
    # logo_btn.draw(Screen)
    if is_developer_mode:
        font = pygame.font.Font('freesansbold.ttf', 36)
        text = font.render('Developer_Mode', True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (1080, 160)
        Screen.blit(text, textRect)


def draw(this_game: caro.Caro, this_screen):
    # Draw logo first (preserve existing logo functionality)
    logo()
    
    # Background color for the board
    board_background = (245, 222, 179)  # Light wooden color typical of Go boards
    
    # Draw board background
    board_width = (MARGIN + WIDTH) * COLNUM + MARGIN
    board_height = (MARGIN + HEIGHT) * ROWNUM + MARGIN
    pygame.draw.rect(this_screen, board_background, [MARGIN, MARGIN, board_width - MARGIN * 2, board_height - MARGIN * 2])
    
    # Draw grid lines (thinner, more Go-like)
    line_color = (50, 50, 50)  # Dark gray for grid lines
    line_thickness = 1
    
    # Vertical lines
    for column in range(COLNUM + 1):
        start_pos = (MARGIN + (MARGIN + WIDTH) * column, MARGIN)
        end_pos = (MARGIN + (MARGIN + WIDTH) * column, MARGIN + (MARGIN + HEIGHT) * ROWNUM)
        pygame.draw.line(this_screen, line_color, start_pos, end_pos, line_thickness)
    
    # Horizontal lines
    for row in range(ROWNUM + 1):
        start_pos = (MARGIN, MARGIN + (MARGIN + HEIGHT) * row)
        end_pos = (MARGIN + (MARGIN + WIDTH) * COLNUM, MARGIN + (MARGIN + HEIGHT) * row)
        pygame.draw.line(this_screen, line_color, start_pos, end_pos, line_thickness)
    
    # Draw star points (like in Go board)
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
    
    # Draw X and O pieces
    for row in range(ROWNUM):
        for column in range(COLNUM):
            center = (
                int(MARGIN + (MARGIN + WIDTH) * column + WIDTH / 2),
                int(MARGIN + (MARGIN + HEIGHT) * row + HEIGHT / 2)
            )
            
            # Tính toán vị trí để vẽ hình ảnh
            img_pos = (
                int(MARGIN + (MARGIN + WIDTH) * column),
                int(MARGIN + (MARGIN + HEIGHT) * row)
            )
            
            if this_game.grid[row][column] == 'X':
                # Sử dụng hình ảnh X thay vì vẽ
                this_screen.blit(x_img, img_pos)
            
            elif this_game.grid[row][column] == 'O':
                # Sử dụng hình ảnh O thay vì vẽ
                this_screen.blit(o_img, img_pos)


    
    # Highlight last move
    if len(this_game.last_move) > 0:
        last_move_row, last_move_col = this_game.last_move[-1][0], this_game.last_move[-1][1]
        center = (
            int(MARGIN + (MARGIN + WIDTH) * last_move_col + WIDTH / 2),
            int(MARGIN + (MARGIN + HEIGHT) * last_move_row + HEIGHT / 2)
        )
        pygame.draw.circle(this_screen, (255, 0, 0), center, 5)  # Small red dot for last move
        
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
            # print(self.last_move)
            # print(last_move, type(last_move), type(last_move[0]))
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
            # print(self.last_move)
            # print(last_move, type(last_move), type(last_move[0]))
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
    pass


def checking_winning(status):
    if status == 2:
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render('Draw', True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (int(Window_size[0]/2), int(Window_size[1]/2))
        Screen.blit(text, textRect)
        # done = True
    if status == 0:
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render('X wins', True, RED, GREEN)
        textRect = text.get_rect()
        textRect.center = (int(Window_size[0]/2), int(Window_size[1]/2))
        Screen.blit(text, textRect)
        # done = True
    if status == 1:
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render('O wins', True, BLUE, GREEN)
        textRect = text.get_rect()
        textRect.center = (int(Window_size[0]/2), int(Window_size[1]/2))
        Screen.blit(text, textRect)
        # done = True


# --------- Main Program Loop -------------------------------------------
while not done:
    for event in pygame.event.get():  # User did something

# ---------------- Undo button ---------------------------------------------
        if undo_button.draw(Screen):  # Ấn nút Undo
            Undo(my_game)
            print("Undo")
            pass
# --------------Exit button--------------------------------------------
        if exit_button.draw(Screen):  # Ấn nút Thoát
            print('EXIT')
            # quit game
            done = True
# --------------Replay button-------------------------------------------
        if replay_button.draw(Screen):  # Ấn nút Chơi lại
            print('Replay')
            my_game.reset()
            re_draw()
# ---------Normal mode---------------------------------------------------
        if not is_developer_mode:
    # ------------- Setup button---------------------------------------------
            if len(my_game.last_move) > 0:
                pass
            if not my_game.is_use_ai:
                pass
            else:
    # --------------------- AI turn-------------------------------------------
                if my_game.turn == my_game.ai_turn:
                    if my_game.get_winner() == -1:
    # ---------------------AI MAKE MOVE---------------------------------------- ==================================
                        # my_game.random_ai()                                    #||  Here is where to change AI  ||
                        best_move = agent.get_move(my_game)                      #||                              ||
                        my_game.make_move(best_move[0], best_move[1])            #||                              ||
                        # pygame.time.delay(500)                                   #||          (❁´◡`❁)           ||
    # ------------------------------------------------------------------------- =================================
                        draw(my_game, Screen)
                    ai_thinking_btn.disable_button()
                    ai_thinking_btn.re_draw(Screen)
                    status = my_game.get_winner()
                    checking_winning(status)
                else:
                    pass

    # -----------pvp button----------------------------------------------------
            if pvp_btn.draw(Screen):
                my_game.use_ai(False)
                pvp_btn.disable_button()
                aivp_btn.enable_button()
                print("P_P")
                pass
    # ------------ai vs p button------------------------------------------------
            if aivp_btn.draw(Screen):
                my_game.use_ai(True)
                aivp_btn.disable_button()
                pvp_btn.enable_button()
                

                agent = Agent(max_depth=my_game.hard_ai,
                                    XO=my_game.get_current_XO_for_AI())
                print("AI_P")
                pass
    # --------------Draw ai thinking button ------------------------------------
            if ai_thinking_btn.draw(Screen):
                pass
    # ----------hard button-----------------------------------------------------
            if h_btn.draw(Screen):
                h_btn.disable_button()
                m_btn.enable_button()
                e_btn.enable_button()
                my_game.change_hard_ai("hard")
                

                agent = Agent(max_depth=my_game.hard_ai,
                                    XO=my_game.get_current_XO_for_AI())
                print("Hard")
                pass
    # ----------medium button---------------------------------------------------
            if m_btn.draw(Screen):
                h_btn.enable_button()
                m_btn.disable_button()
                e_btn.enable_button()
                my_game.change_hard_ai("medium")
                

                agent = Agent(max_depth=my_game.hard_ai,
                                    XO=my_game.get_current_XO_for_AI())
                print("Medium")
                pass
    # -------------easy button--------------------------------------------------
            if e_btn.draw(Screen):
                h_btn.enable_button()
                m_btn.enable_button()
                e_btn.disable_button()
                my_game.change_hard_ai("easy")
                

                agent = Agent(max_depth=my_game.hard_ai,
                                    XO=my_game.get_current_XO_for_AI())
                print("Easy")
                pass
    # -------Choose person play first button------------------------------------
            if person_btn.draw(Screen):  # Ấn nút Chọn người đi trước
                person_btn.disable_button()
                ai_btn.enable_button()
                my_game.set_ai_turn(2)
                

                agent = Agent(max_depth=my_game.hard_ai,
                                        XO=my_game.get_current_XO_for_AI())
                print("Human")
                pass
    # -------Choose AI play first button------------------------------------
            if ai_btn.draw(Screen):  # Ấn nút Chọn AI đi trước
                ai_btn.disable_button()
                person_btn.enable_button()
                my_game.set_ai_turn(1)
                

                agent = Agent(max_depth=my_game.hard_ai,
                                XO=my_game.get_current_XO_for_AI())
                print("AI")
                pass

    # -----------------checking is exit game? ------------------------------
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                # Set the screen background
    # -------Find pos mouse clicked and make a move-------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = int(pos[0] // (WIDTH + MARGIN))
                row = int(pos[1] // (HEIGHT + MARGIN))
                # print(pos, col, row)
                if col < COLNUM and row < ROWNUM:
                    my_game.make_move(row, col)
                status = my_game.get_winner()
                if my_game.is_use_ai and my_game.turn == my_game.ai_turn:
                    ai_thinking_btn.enable_button()
                    ai_thinking_btn.re_draw(Screen)
                    draw(my_game, Screen)
# ---------------Develop-mode-----------------------------------------
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
# ------ Draw screen---------------------------------------------------
    draw(my_game, Screen)
# -------- checking winner --------------------------------------------
    checking_winning(status)
# Limit to 999999999 frames per second
    clock.tick(FPS)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

pygame.time.delay(50)
quit()
pygame.quit()
sys.exit()
