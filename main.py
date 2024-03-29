import pyxel

class Character:
    def __init__(self, x, y):
        self.i = 0  # Character's current animation frame
        self.x = x
        self.y = y
        self.direction = 1  # Initial direction of animation frames

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

class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.last_move_direction = 'right'  # Default direction
    
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2  # Move left
            self.last_move_direction = 'left'
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2  # Move right
            self.last_move_direction = 'right'
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2  # Move up
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2  # Move down

    def draw(self):
        # Determine sprite width and direction for flipping
        sprite_width = 16
        flip_offset = 0
        
        if self.last_move_direction == 'left':
            sprite_width = -16  # Flip sprite by making width negative
            flip_offset = 16  # Adjust for flipping around the center

        # The x position is adjusted to compensate for the sprite width when flipped
        x_position = self.x - flip_offset // 2 + 8 if self.last_move_direction == 'left' else self.x + flip_offset // 2

        pyxel.blt(x_position, self.y, self.i, 0, 16, sprite_width, 16, 0)
        


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("resources.pyxres")
        self.characters = []  # List to hold character instances
        self.player = None  # Separate reference to the player
        self.frame_counter = 0
        
        # Character creation
        self.create_character(20, 0)
        self.create_character(40, 20)
        self.create_character(60, 60)
        self.spawn_player(0, 50)
        
        pyxel.run(self.update, self.draw)
    
    def create_character(self, x, y):
        # Create a new character and set its position
        new_character = Character(x, y)
        new_character.position(x, y)
        # Append the new character to the characters list
        self.characters.append(new_character)
    
    def spawn_player(self, x, y):
            player = Player(x, y)
            self.player = player  # Keep a reference to the player
            self.characters.append(player)  # Also add to characters list for drawing

    def update_characters(self):
        # Update all characters if necessary
        for character in self.characters:
            if character.should_update(self.frame_counter):
                character.update_state()

    def update(self):
        self.frame_counter += 1
        self.update_characters()
        if self.player:  # Ensure player exists before calling update
            self.player.update()

    def draw(self):
        pyxel.cls(0)  # Clear screen
        for character in self.characters:
            character.draw()
App()
