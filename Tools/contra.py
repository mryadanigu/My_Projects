import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Contra-like Game")

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")
background_img = pygame.image.load("background.png")

# Player class
class Player:
    def __init__(self):
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - self.rect.height - 50
        self.speed = 5
        self.bullets = []
        self.is_jumping = False
        self.jump_count = 10

    def move(self, dx):
        """Move the player left or right"""
        self.rect.x += dx * self.speed
        # Keep the player within screen boundaries
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

    def jump(self):
        """Allow the player to jump"""
        if not self.is_jumping:
            self.is_jumping = True

    def update_jump(self):
        """Update the player's jump"""
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

    def shoot(self):
        """Shoot a bullet"""
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(bullet)

    def update_bullets(self):
        """Update bullets position and remove out-of-bounds bullets"""
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def draw(self):
        """Draw the player and its bullets on the screen"""
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw()

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = 10

    def update(self):
        """Move the bullet upward"""
        self.rect.y -= self.speed

    def draw(self):
        """Draw the bullet on the screen"""
        screen.blit(self.image, self.rect)
        
# Enemy class
class Enemy:
    def __init__(self):
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-500, -50)
        self.speed = random.randint(2, 5)

    def update(self):
        """Move the enemy downward"""
        self.rect.y += self.speed
        # If enemy goes out of bounds, reset its position
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-500, -50)
            self.speed = random.randint(2, 5)

    def draw(self):
        """Draw the enemy on the screen"""
        screen.blit(self.image, self.rect)

# Main game loop
def game_loop():
    # Create player
    player = Player()

    # List to hold enemies
    enemies = [Enemy() for _ in range(5)]

    # Clock
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                elif event.key == pygame.K_UP:
                    player.jump()

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1)
        if keys[pygame.K_RIGHT]:
            player.move(1)

        # Update game objects
        player.update_jump()
        player.update_bullets()
        for enemy in enemies:
            enemy.update()

            # Check for collision with player's bullets
            for bullet in player.bullets:
                if bullet.rect.colliderect(enemy.rect):
                    player.bullets.remove(bullet)
                    enemies.remove(enemy)
                    enemies.append(Enemy())
                    break

        # Clear screen
        screen.blit(background_img, (0, 0))

        # Draw game objects
        player.draw()
        for enemy in enemies:
            enemy.draw()

        # Update display
        pygame.display.update()

        # Limit frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    game_loop()