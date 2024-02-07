import pyxel

class Character:
    def __init__(self):
        self.i = 0  # Character's state
        self.x = 0
        self.y = 0
        self.direction = 1  # Initial direction of state change

    def position(self, x, y):
        self.x = x
        self.y = y

    def should_update(self, frame_counter):
        # Determine if the character should update based on the frame counter
        return frame_counter % 5 == 0

    def update_state(self):
        # Update the character's state
        self.i += self.direction
        if self.i == 2 and self.direction == 1:
            self.direction = -1
        elif self.i == 0 and self.direction == -1:
            self.direction = 1

    def draw(self):
        # Draw the character based on its current state
        pyxel.blt(self.x, self.y, self.i, 0, 0, 16, 16, 0)


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("resources.pyxres")
        self.characters = []  # List to hold character instances
        self.frame_counter = 0  # Frame counter for update control
        
        # Create and position characters
        self.character = Character()
        self.character.position(0, 0)
        self.characters.append(self.character)
        
        self.enemy = Character()
        self.enemy.position(10, 10)
        self.characters.append(self.enemy)
        
        pyxel.run(self.update, self.draw)

    def update_characters(self):
        # Update all characters if necessary
        for character in self.characters:
            if character.should_update(self.frame_counter):
                character.update_state()

    def update(self):
        self.frame_counter += 1
        self.update_characters()

    def draw(self):
        pyxel.cls(0)  # Clear screen
        for character in self.characters:
            character.draw()

App()
