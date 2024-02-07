import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("resources.pyxres")
        self.i = 0  # Initialize counter for the image state
        self.direction = 1  # Direction of increment: 1 for up, -1 for down
        self.frame_counter = 0  # Frame counter to track when to update
        pyxel.run(self.update, self.draw)

    def update(self):
        self.frame_counter += 1  # Increment frame counter each frame

        # Only update `self.i` every 5th frame
        if self.frame_counter % 5 == 0:
            self.i += self.direction
            # When reaching the peak (2) or returning to start (0), change direction
            if self.i == 2 and self.direction == 1:
                self.direction = -1  # Start decrementing
            elif self.i == 0 and self.direction == -1:
                self.direction = 1  # Start incrementing

    def draw(self):
        pyxel.cls(0)  # Clear screen
        pyxel.text(30, 30, str(self.i), 1)
        # Draw sprite based on self.i, ensure sprite coordinates are correct
        # Assuming each sprite is 16 pixels apart on the texture page
        pyxel.blt(0, 0, self.i, 0, 0, 16, 16)

App()
