from pygame import *

back = (47, 250, 223)
window = display.set_mode((600, 500))
window.fill(back)
display.set_caption('Ping Pong')

clock = time.Clock()
FPS = 60
game = True

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

Left_player = Player('racket.png', 0, 250, 20, 100, 10)
Right_player = Player('racket.png', 580, 250, 20, 100, 10)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(back)

    Left_player.reset()
    Left_player.update_l()

    Right_player.reset()
    Right_player.update_r()


    display.update()
    clock.tick(FPS)
