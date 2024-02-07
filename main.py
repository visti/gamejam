import pyxel

class Character:
    def __init__(self):
        self.i = 0  # Character's state
        self.direction = 1  # Initial direction of state change

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
        pyxel.blt(0, 0, self.i, 0, 0, 16, 16)


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("resources.pyxres")
        self.character = Character()  # Create a Character instance
        self.frame_counter = 0  # Frame counter for update control
        pyxel.run(self.update, self.draw)

    def update(self):
        self.frame_counter += 1
        if self.character.should_update(self.frame_counter):
            self.character.update_state()  # Update character based on internal logic

    def draw(self):
        pyxel.cls(0)  # Clear screen
        self.character.draw()  # Delegate drawing to the Character instance

App()

