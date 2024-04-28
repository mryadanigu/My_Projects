import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Wars Game")

# Load images
ship_img = pygame.image.load("ship.png")
asteroid_img = pygame.image.load("asteroid.png")
laser_img = pygame.image.load("laser.png")

# Player class
class Player:
    def __init__(self):
        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 5
        self.lasers = []

    def move(self, dx):
        """Move the ship left or right"""
        self.rect.x += dx * self.speed
        # Keep the ship within screen boundaries
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

    def shoot(self):
        """Shoot a laser"""
        laser = Laser(self.rect.centerx, self.rect.top)
        self.lasers.append(laser)

    def update_lasers(self):
        """Update lasers position and remove out-of-bounds lasers"""
        for laser in self.lasers:
            laser.update()
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)

    def draw(self):
        """Draw the ship and its lasers on the screen"""
        screen.blit(self.image, self.rect)
        for laser in self.lasers:
            laser.draw()

# Laser class
class Laser:
    def __init__(self, x, y):
        self.image = laser_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = 10

    def update(self):
        """Move the laser upward"""
        self.rect.y -= self.speed

    def draw(self):
        """Draw the laser on the screen"""
        screen.blit(self.image, self.rect)

# Asteroid class
class Asteroid:
    def __init__(self):
        self.image = asteroid_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-500, -50)
        self.speed = random.randint(2, 5)

    def update(self):
        """Move the asteroid downward"""
        self.rect.y += self.speed
        # If asteroid goes out of bounds, reset its position
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-500, -50)
            self.speed = random.randint(2, 5)

    def draw(self):
        """Draw the asteroid on the screen"""
        screen.blit(self.image, self.rect)
    
# Main game loop
def game_loop():
    # Create player
    player = Player()

    # List to hold asteroids
    asteroids = [Asteroid() for _ in range(5)]

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

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1)
        if keys[pygame.K_RIGHT]:
            player.move(1)

        # Update game objects
        player.update_lasers()
        for asteroid in asteroids:
            asteroid.update()

            # Check for collision with player's ship
            if player.rect.colliderect(asteroid.rect):
                print("Game Over!")
                running = False

            # Check for collision with lasers
            for laser in player.lasers:
                if laser.rect.colliderect(asteroid.rect):
                    player.lasers.remove(laser)
                    asteroids.remove(asteroid)
                    asteroids.append(Asteroid())
                    break

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw game objects
        player.draw()
        for asteroid in asteroids:
            asteroid.draw()

        # Update display
        pygame.display.update()

        # Limit frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    game_loop()
    
