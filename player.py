from circleshape import *
from constants import *



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0

    def triangle(self): # returns points for drawing shapes on screen
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): # draws a shape on screen
        pygame.draw.polygon(screen, pygame.Color(255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):  # rotates player object 
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt): # moves player object 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt): # calls movement methods to update position based on key input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)