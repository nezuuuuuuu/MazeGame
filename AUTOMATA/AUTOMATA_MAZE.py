import pygame
import random
import sys
import plotDFA
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# map
maze = [    
    [  1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
    [  1,      2,      3,      4,      1,      5,      1,      6,      7,      8,      9,     10,     11,      1,     12,     13,      1,     14,     15,      1],
    [  1,     16,      1,     17,      1,     18,      1,     19,      1,      1,      1,      1,     20,      1,     21,      1,     22,     23,     24,      1],
    [  1,     25,      1,     26,     27,     28,     29,     30,      1,     31,     32,      1,     33,      1,     34,     35,     36,      1,     37,      1],
    [  1,     38,      1,      1,      1,      1,      1,     39,      1,     40,      1,      1,     41,      1,      1,      1,     42,      1,     43,      1],
    [  1,     44,     45,     46,     47,     48,     49,     50,      1,     51,     52,     53,     54,     55,     56,     57,     58,     59,     60,      1],
    [  1,     61,      1,      1,      1,      1,      1,      1,     62,      1,      1,     63,      1,      1,      1,      1,     64,      1,     65,      1],
    [  1,     66,      1,     67,      1,      1,      1,     68,     69,     70,      1,     71,      1,      1,      1,      1,     72,      1,      1,      1],
    [  1,     73,      1,     74,     75,     76,     77,     78,      1,     79,     80,     81,      1,      1,      1,      1,      1,     82,      1,      1],
    [  1,     83,      1,     84,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,     85,     86,     87,     88,      1,      1],
    [  1,     89,     90,     91,     92,     93,     94,     95,      1,      1,     96,     97,     98,     99,      1,      1,      1,    100,      1,      1],
    [  1,    101,      1,    102,      1,      1,    103,      1,      1,      1,    104,      1,      1,    105,      1,      1,      1,    106,      1,      1],
    [107,    108,      1,    109,      1,    110,    111,    112,    113,    114,    115,    116,    117,    118,      1,    119,      1,    120,      1,      1],
    [  1,    121,      1,    122,      1,      1,    123,      1,      1,    124,      1,    125,      1,    126,    127,    128,    129,    130,      1,      1],
    [  1,    131,    132,      1,      1,      1,    133,      1,      1,      1,      1,    134,      1,      1,      1,      1,      1,    135,      1,      1],

    [  1,    136,    137,      1,      1,      1,    138,      1,      1,      1,      1,    139,      1,      1,      1,      1,      1,    140,      1,      1],
    [  1,    141,    142,    143,    144,    145,    146,    147,      1,    148,    149,    150,    151,      1,    152,    153,    154,    155,    156,      1],
    [  1,    157,      1,    158,      1,    159,    160,    161,      1,    162,      1,      1,    163,      1,    164,    165,    166,    167,      1,      1],
    [  1,    168,      1,    169,      1,      1,    170,    171,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
]

transition_table =None
TILE_SIZE = 32
player_x = None
player_y = None

goal_x = None
goal_y = None
starting = None

goal=None

state=None
current_state=None
goal_state= None
ctr=0


def draw_play_again_button():
    font = pygame.font.SysFont(None, 48)
    text = font.render("Play Again", True, BLACK)
    rect = text.get_rect(center=(SCREEN_WIDTH -200, SCREEN_HEIGHT - 400))
    screen.blit(text, rect)
    return rect

def initialize_game():

    global player_x, player_y, goal_x, goal_y, starting, goal, state, current_state, goal_state, transition_table,ctr
    ctr =0
    # Transition table
    transition_table =[
   [2, 2, 16, 3],
[3, 2, 3, 4],
[4, 3, 17, 4],
[5, 5, 18, 5],
[6, 6, 19, 7],
[7, 6, 7, 8],
[8, 7, 8, 9],
[9, 8, 9, 10],
[10, 9, 10, 11],
[11, 10, 20, 11],
[12, 12, 21, 13],
[13, 12, 13, 13],
[14, 14, 23, 15],
[15, 14, 24, 15],
[2, 16, 25, 16],
[4, 17, 26, 17],
[5, 18, 28, 18],
[6, 19, 30, 19],
[11, 20, 33, 20],
[12, 21, 34, 21],
[22, 22, 36, 23],
[14, 22, 23, 24],
[15, 23, 37, 24],
[16, 25, 38, 25],
[17, 26, 26, 27],
[27, 26, 27, 28],
[18, 27, 28, 29],
[29, 28, 29, 30],
[19, 29, 39, 30],
[31, 31, 40, 32],
[32, 31, 32, 32],
[20, 33, 41, 33],
[21, 34, 34, 35],
[35, 34, 35, 36],
[22, 35, 42, 36],
[24, 37, 43, 37],
[25, 38, 44, 38],
[30, 39, 50, 39],
[31, 40, 51, 40],
[33, 41, 54, 41],
[36, 42, 58, 42],
[37, 43, 60, 43],
[38, 44, 61, 45],
[45, 44, 45, 46],
[46, 45, 46, 47],
[47, 46, 47, 48],
[48, 47, 48, 49],
[49, 48, 49, 50],
[39, 49, 50, 50],
[40, 51, 51, 52],
[52, 51, 52, 53],
[53, 52, 63, 54],
[41, 53, 54, 55],
[55, 54, 55, 56],
[56, 55, 56, 57],
[57, 56, 57, 58],
[42, 57, 64, 59],
[59, 58, 59, 60],
[43, 59, 65, 60],
[44, 61, 66, 61],
[62, 62, 69, 62],
[53, 63, 71, 63],
[58, 64, 72, 64],
[60, 65, 65, 65],
[61, 66, 73, 66],
[67, 67, 74, 67],
[68, 68, 78, 69],
[62, 68, 69, 70],
[70, 69, 79, 70],
[63, 71, 81, 71],
[64, 72, 72, 72],
[66, 73, 83, 73],
[67, 74, 84, 75],
[75, 74, 75, 76],
[76, 75, 76, 77],
[77, 76, 77, 78],
[68, 77, 78, 78],
[70, 79, 79, 80],
[80, 79, 80, 81],
[71, 80, 81, 81],
[82, 82, 88, 82],
[73, 83, 89, 83],
[74, 84, 91, 84],
[85, 85, 85, 86],
[86, 85, 86, 87],
[87, 86, 87, 88],
[82, 87, 100, 88],
[83, 89, 101, 90],
[90, 89, 90, 91],
[84, 90, 102, 92],
[92, 91, 92, 93],
[93, 92, 93, 94],
[94, 93, 103, 95],
[95, 94, 95, 95],
[96, 96, 104, 97],
[97, 96, 97, 98],
[98, 97, 98, 99],
[99, 98, 105, 99],
[88, 100, 106, 100],
[89, 101, 108, 101],
[91, 102, 109, 102],
[94, 103, 111, 103],
[96, 104, 115, 104],
[99, 105, 118, 105],
[100, 106, 120, 106],
[107, 107, 107, 108],
[101, 107, 121, 108],
[102, 109, 122, 109],
[110, 110, 110, 111],
[103, 110, 123, 112],
[112, 111, 112, 113],
[113, 112, 113, 114],
[114, 113, 124, 115],
[104, 114, 115, 116],
[116, 115, 125, 117],
[117, 116, 117, 118],
[105, 117, 126, 118],
[119, 119, 128, 119],
[106, 120, 130, 120],
[108, 121, 131, 121],
[109, 122, 122, 122],
[111, 123, 133, 123],
[114, 124, 124, 124],
[116, 125, 134, 125],
[118, 126, 126, 127],
[127, 126, 127, 128],
[119, 127, 128, 129],
[129, 128, 129, 130],
[120, 129, 135, 130],
[121, 131, 136, 132],
[132, 131, 137, 132],
[123, 133, 138, 133],
[125, 134, 139, 134],
[130, 135, 140, 135],
[131, 136, 141, 137],
[132, 136, 142, 137],
[133, 138, 146, 138],
[134, 139, 150, 139],
[135, 140, 155, 140],
[136, 141, 157, 142],
[137, 141, 142, 143],
[143, 142, 158, 144],
[144, 143, 144, 145],
[145, 144, 159, 146],
[138, 145, 160, 147],
[147, 146, 161, 147],
[148, 148, 162, 149],
[149, 148, 149, 150],
[139, 149, 150, 151],
[151, 150, 163, 151],
[152, 152, 164, 153],
[153, 152, 165, 154],
[154, 153, 166, 155],
[140, 154, 167, 156],
[156, 155, 156, 156],
[141, 157, 168, 157],
[143, 158, 169, 158],
[145, 159, 159, 160],
[146, 159, 170, 161],
[147, 160, 171, 161],
[148, 162, 162, 162],
[151, 163, 163, 163],
[152, 164, 164, 165],
[153, 164, 165, 166],
[154, 165, 166, 167],
[155, 166, 167, 167],
[157, 168, 168, 168],
[158, 169, 169, 169],
[160, 170, 170, 171],
[161, 170, 171, 171],
]
  

    starting = random.randint(2, 171)
    goal = random.randint(2, 171)

    while goal == starting:
        goal = random.randint(2, 171)
    
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == starting:
                player_x = col
                player_y = row
                break  

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == goal:
                goal_x = col
                goal_y = row
                break

    state = starting
    current_state = state
    goal_state = goal

    transition_table[goal - 2] = [goal] * 4 
    plotDFA.set_start_and_accept(plotDFA.mydict[starting],[f'q{goal-2}'])
    plotDFA.plot_dfa()
   




def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_won_text():
    font = pygame.font.SysFont(None, 100)
    text = font.render("YOU WON!!!!!!", True, GREEN)
    rect = text.get_rect(center=(SCREEN_WIDTH - 665, SCREEN_HEIGHT // 2))
    screen.blit(text, rect)

def is_wall(x, y):
    if 0 <= x < len(maze[0]) and 0 <= y < len(maze):
        return maze[y][x] == 1
    return True

running = True
clock = pygame.time.Clock()


initialize_game()  
while running:
    screen.fill(WHITE)
    draw_maze()
    pygame.draw.rect(screen, GREEN, (goal_x * TILE_SIZE, goal_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.draw.circle(screen, RED, 
                   (player_x * TILE_SIZE + TILE_SIZE // 2, player_y * TILE_SIZE + TILE_SIZE // 2), 
                   TILE_SIZE // 2)
    play_again_button_rect=draw_play_again_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_again_button_rect.collidepoint(mouse_pos):
                    print('New Game')
                    initialize_game()  
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                state=transition_table[state-2][1]
                print(f'state: q{state-2}', end=', ')
                if(state != current_state):
                    current_state=state
                    ctr+=1
                    player_x -= 1          

            if event.key == pygame.K_d:
                state=transition_table[state-2][3]
                print(f'state: q{state-2}', end=', ')
                if(state != current_state):
                    player_x += 1
                    ctr+=1
                    current_state=state


            if event.key == pygame.K_w:
                state=transition_table[state-2][0]
                print(f'state: q{state-2}', end=', ')
                if(state != current_state):
                    player_y -= 1
                    ctr+=1
                    current_state=state
                
            if event.key == pygame.K_s:
                state=transition_table[state-2][2]
                print(f'state: q{state-2}', end=', ')
                if(state != current_state):
                    player_y += 1
                    ctr+=1
                    current_state=state
            print(f'move count:{ctr}')

    if state == goal_state:
        draw_won_text()
            
    pygame.display.flip()
    clock.tick(10) 
