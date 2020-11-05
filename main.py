import pygame, sys, random


def smooth_ground():
    screen.blit(ground, (ground_x_pos, 900))
    screen.blit(ground, (ground_x_pos + 600, 900))


def create_joint():
    random_joint_pos = random.choice(joint_height)
    new_joint = joint.get_rect(midtop=(700, random_joint_pos))
    return new_joint


def joint_movement(joints):
    for joint1 in joints:
        if score >= 0:
            joint1.centerx -= 5
        if score >= 10:
            joint1.centerx -= 0.5
        if score >= 20:
            joint1.centerx -= 0.5
        if score >= 30 :
            joint1.centerx -= 0.5
        if score >= 40 :
            joint1.centerx -= 0.5
    return joints


def draw_joints(joints):
    for joint1 in joints:
        screen.blit(joint, joint1)


def check_death(joints):
    for joint1 in joints:
        if emoji_hb.colliderect(joint1):
            return False

    if emoji_hb.top <= -10 or emoji_hb.bottom >= 900:
        return False

    return True


def score_display(game_state):
    if game_state == 'game':
        score_onscreen = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_onscreen.get_rect(center=(288, 100))
        screen.blit(score_onscreen, score_rect)

    if game_state == 'game_over':
        score_onscreen = game_font.render(f'Score: {int(score)} ', True, (255, 255, 255))
        score_rect = score_onscreen.get_rect(center=(288, 100))
        screen.blit(score_onscreen, score_rect)

        stoned_onscreen = game_font.render('Damn bro you are STONED', True, (255, 255, 255))
        stoned_rect = stoned_onscreen.get_rect(center=(288, 200))
        screen.blit(stoned_onscreen, stoned_rect)

        high_onscreen = game_font.render(f'HIGH-score: {int(high)}', True, (255, 255, 255))
        high_rect = high_onscreen.get_rect(center=(288, 300))
        screen.blit(high_onscreen, high_rect)

        restart_onscreen = game_font.render('Press W or S to restart', True, (255, 255, 255))
        restart_rect = restart_onscreen.get_rect(center=(288, 400))
        screen.blit(restart_onscreen, restart_rect)


pygame.init()
screen = pygame.display.set_mode((600, 1080))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('Arial', 40)

# variables
restart = 0
stoned = 0
emoji_movement = 0
emoji_hb = 0
life = True
score = 0
high = 0

bg = pygame.image.load('images/bg.png')
bg2 = pygame.image.load('images/bg2.png')
bg3 = pygame.image.load('images/bg3.png')
bg4 = pygame.image.load('images/bg4.png')
bgf = pygame.image.load('images/bgf.png')

ground = pygame.image.load('images/ground.jpg')
ground_x_pos = 0

emoji = pygame.image.load('images/emoji.png')
emoji_hb = emoji.get_rect(center=(100, 540))

joint = pygame.image.load('images/joint.png')

joint_list = []

SPAWNJOINT = pygame.USEREVENT
pygame.time.set_timer(SPAWNJOINT, 1200)
joint_height = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and life:
                if score >= 0:
                    emoji_movement -= 7
                if score >= 10:
                    emoji_movement -= 1
                if score >= 20:
                    emoji_movement -= 1
                if score >= 30:
                    emoji_movement -= 1
                if score >= 40:
                    emoji_movement -= 2

            if event.key == pygame.K_s and life:
                if score >= 0:
                    emoji_movement += 7
                if score >= 10:
                    emoji_movement += 1
                if score >= 20:
                    emoji_movement += 1
                if score >= 30:
                    emoji_movement += 1
                if score >= 40:
                    emoji_movement += 2

            if life == False:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    life = True
                    joint_list.clear()
                    emoji_hb.center = (100, 540)
                    score = 0

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_s or event.key == pygame.K_w:
                emoji_movement = 0

        if event.type == SPAWNJOINT:
            joint_list.append(create_joint())

    if score >= 0:
        screen.blit(bg, (0, 0))
    if score >= 10:
        screen.blit(bg2, (0, 0))
    if score >= 20:
        screen.blit(bg3, (0, 0))
    if score >= 30:
        screen.blit(bg4, (0, 0))
    if score >= 40:
        screen.blit(bgf, (0, 0))

    if life:
        # Emoji
        emoji_hb.centery += emoji_movement
        screen.blit(emoji, emoji_hb)
        life = check_death(joint_list)

        # Obstacles (joints)
        joint_list = joint_movement(joint_list)
        draw_joints(joint_list)
        ground_x_pos -= 1
        score += 0.005
        score_display('game')
    else:
        if score > high:
            high = score
        score_display('game_over')

    smooth_ground()
    if ground_x_pos <= -600:
        ground_x_pos = 0
    screen.blit(ground, (ground_x_pos, 900))

    pygame.display.update()
    clock.tick(144)
