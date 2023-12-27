import pygame
import time

width, height = 1280, 720

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
run = True

fps = 60
font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 80)


paddle_width, paddle_height = 20, 200

paddle_one = pygame.Rect(20, 200, paddle_width, paddle_height)
paddle_two = pygame.Rect(width - (2 * paddle_width), 200, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - 20, height // 2 - 20, 40, 40)

paddle_one_y_vel = 0
paddle_two_y_vel = 0
paddle_speed = 10

ball_speed = 5
factor = 1
ball_x_vel = ball_speed 
ball_y_vel = ball_speed

score_one = 0
score_two = 0

rounds = 3
isOver = False

def reset_game():
    time.sleep(1)
    ball.x = width // 2 - 20
    ball.y = height // 2 - 20
    
while run:
    clock.tick(fps)
    factor += 0.001

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                paddle_one_y_vel = 1
            elif event.key == pygame.K_w:
                paddle_one_y_vel = -1
            elif event.key == pygame.K_UP:
                paddle_two_y_vel = -1
            elif event.key == pygame.K_DOWN:
                paddle_two_y_vel = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                paddle_one_y_vel = 0
            elif event.key == pygame.K_w:
                paddle_one_y_vel = 0
            elif event.key == pygame.K_UP:
                paddle_two_y_vel = 0
            elif event.key == pygame.K_DOWN:
                paddle_two_y_vel = 0

    paddle_one.y += paddle_one_y_vel * paddle_speed
    paddle_two.y += paddle_two_y_vel * paddle_speed

    paddle_one.y = max(0, min(paddle_one.y, height - paddle_one.height))
    paddle_two.y = max(0, min(paddle_two.y, height - paddle_two.height))

    ball.x += ball_x_vel * factor
    ball.y += ball_y_vel * factor

    factor += 0.001

    if ball.colliderect(paddle_one) or ball.colliderect(paddle_two):
        ball_x_vel = -ball_x_vel  

    if ball.top <= 0 or ball.bottom >= height:
        ball_y_vel = -ball_y_vel 

    if ball.right <= 0:
        score_two += 1
        reset_game()
        factor = 1
        
    elif ball.left >= width:
        score_one += 1
        reset_game()
        factor = 1

    result_string = ''

    if (score_one >= rounds):
        result_string = 'Player 1 has Won'
        isOver = True
    elif (score_two >= rounds):
        result_string = 'Player 2 has Won'
        isOver = True

    result_text = font.render(result_string, True, (255, 255, 255))

    score_one_text = font.render(f'{score_one}', True, (255, 255, 255))
    score_two_text = font.render(f'{score_two}', True, (255, 255, 255))

    screen.fill((0, 0, 0))

    screen.blit(score_one_text, (width // 4, 20))
    screen.blit(score_two_text, (width - (width // 4), 20))
    screen.blit(result_text, ((width // 2) - (result_text.get_width() // 2), 20))
    pygame.draw.rect(screen, (255, 255, 255), paddle_one)
    pygame.draw.rect(screen, (255, 255, 255), paddle_two)
    pygame.draw.circle(screen, (255, 255, 255), ball.center, ball.width // 2)

    pygame.display.flip()

    if isOver:
        time.sleep(2)
        run = False


pygame.quit()
