from pygame import *

back = (47, 250, 223)
window = display.set_mode((600, 500))
window.fill(back)
display.set_caption('Ping Pong')

clock = time.Clock()
FPS = 60
game = True
game_over = False
winner = None
font.init()
my_font = font.Font(None, 48)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.speed_x = player_speed
        self.speed_y = player_speed
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.y <= 0 or self.rect.y >= 500 - 20:
            self.speed_y = -self.speed_y

    def collide_left(self, left_player):
        if self.rect.colliderect(left_player.rect) and self.speed_x < 0:
            self.speed_x = -self.speed_x
    
    def collide_right(self, right_player):
        if self.rect.colliderect(right_player.rect) and self.speed_x > 0:
            self.speed_x = -self.speed_x

    def check_area(self):
        if self.rect.x <= 0:
            return 'right'
        elif self.rect.x >=  600 - 20:
            return 'left'

Left_player = Player('racket.png', 0, 250, 20, 100, 10)
Right_player = Player('racket.png', 580, 250, 20, 100, 10)

Ball = Enemy('tenis_ball.png', 300, 250, 20, 20, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not game_over:
        window.fill(back)

        Left_player.update_l()
        Left_player.reset()

        Right_player.update_r()
        Right_player.reset()

        Ball.update()
        Ball.collide_left(Left_player)
        Ball.collide_right(Right_player)
        Ball.reset()

        result = Ball.check_area()
        if result == 'right':
            game_over = True
            winner = 'Левый игрок победил!'
        elif result == 'left':
            game_over = True
            winner = 'Правый игрок победил!'
        
    else:
        window.fill(back)
        text = my_font.render(winner, True, (255, 0, 0))
        text_rect = text.get_rect(center=(300, 250))
        window.blit(text, text_rect)

    display.update()
    clock.tick(FPS)
