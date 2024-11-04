import pygame, simpleGE, random

class Star(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("star.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Alien(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("alien.png")
        self.setSize(80, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("space.png")
        
        self.sndStar = simpleGE.Sound("starCollectSound.mp3")
        self.numStars = 10
        
        self.alien = Alien(self)
        self.star = Star(self)
        
        self.stars = []
        for i in range(self.numStars):
            self.stars.append(Star(self))
        
        self.sprites = [self.alien,
                        self.stars]
        
    def process(self):
        for star in self.stars:
            if star.collidesWith(self.alien):
                star.reset()
                self.sndStar.play()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()