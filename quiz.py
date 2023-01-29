import pygame
import random
###################################################################################
# 기본 초기화!!!!!!!! (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

#FPS
clock = pygame.time.Clock()
###################################################################################
# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 1-1. 배경
background = pygame.image.load("C:/pygame_basic/background2.png")

# 1-2. 캐릭터
character = pygame.image.load("C:/pygame_basic/character2.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - (character_width / 2)
character_y_pos = screen_height - character_height
# 1-2. 캐릭터 이동 위치
to_x = 0
character_speed = 0.6

# 2. 똥 만들기
enemy = pygame.image.load("C:/pygame_basic/enemy2.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

# 2-1. 똥2 만들기
enemy2 = pygame.image.load("C:/pygame_basic/enemy3.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = random.randint(0, screen_width - enemy2_width)
enemy2_y_pos = 0
enemy2_speed = 10

game_font = pygame.font.SysFont("hack", 80, True, False)
game_over = game_font.render(str("GAME OVER"), True, (0,0,0))

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 3-1. 똥 위치 정의
    enemy_y_pos += enemy_speed
    enemy2_y_pos += enemy2_speed

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    if enemy_y_pos > screen_height or enemy2_y_pos > screen_height:
        if enemy_y_pos > screen_height:
            enemy_x_pos = random.randint(0, screen_width - enemy_width)
            enemy_y_pos = 0
        elif enemy2_y_pos > screen_height:
            enemy2_x_pos = random.randint(0, screen_width - enemy2_width)
            enemy2_y_pos = 0

    # ★ 화면에 그리기 (캐릭터/이미지 추가할 때마다 그려주기)
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))
    
    if character_rect.colliderect(enemy_rect) or character_rect.colliderect(enemy2_rect):
        screen.blit(game_over, (18, 270))
        running = False
    
    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()