This game is an old school style dungeon crawler. A 3D first person
point of view is simulated with sprites drawn from far to close
based on the player's position.

Standard WASD to move, with E and Q to rotate compass direction.

The left moust button attacks if an enemy is in range.

The goal is to kill all the enemies (red triangles on the map).

Sources
https://opengameart.org/
https://game-icons.net/
https://www.pygame.org/docs/
https://www.geeksforgeeks.org/pygame-character-animation/

Attributions:
Heroine Dusk is created by Clint Bellanger http://clintbellanger.net Ascension: Adventure Tiles by Chris Leclair/XCVG (xcvgsystems.net) [CC-BY-SA 3.0] based on Heroine Dusk by Clint Bellanger (heroinedusk.com) [CC-BY-SA 3.0]
Include "Clint Bellanger" and Stephen "Redshrike" Challener along with your credits. You may optionally provide a link back to Heroine Dusk (http://heroinedusk.com) or Clint's personal site (http://clintbellanger.net). Goblin concept by Justin Nichol
Credit goes to: 3DRealms, Devolver Digital (widescreen edits), osjclatchford (hands) and Capstone (bits from Fate).

AI Logs:

you
How best to code a spritesheet in pygame

ddb
To code a spritesheet in Pygame, you'll need to follow these general steps:

Load the Spritesheet: Use pygame.image.load() to load your spritesheet image.
Extract Individual Sprites: Use pygame.Surface.subsurface() or similar methods to extract individual sprites from the spritesheet.
Animate Sprites: Create a list of these individual sprites and iterate through them to animate your character or object.
Here's a brief outline:

Load the Spritesheet:

spritesheet = pygame.image.load('path_to_spritesheet.png')
Extract Sprites:

sprite = spritesheet.subsurface(pygame.Rect(x, y, width, height))
Animate:

sprites = [sprite1, sprite2, sprite3, ...]
Can you try implementing these steps and let me know if you encounter any specific issues?

#######################################
you
Can I use gamestate as a parameter inside of methods for objects in the gamestate?

ddb
Yes, you can use gamestate as a parameter inside methods for objects in the gamestate. This can be useful for accessing and modifying the overall game state from within individual objects. Just ensure that you pass the gamestate object when calling these methods.

Would you like to share some code or a specific example where you're considering this approach?

you
Is that proper coding though? In Rust, for example, the compiler doesn't like that very much. It works in python though.

ddb
Using gamestate as a parameter inside methods for objects in the gamestate is a common practice in Python and can be perfectly fine. It allows objects to interact with the overall game state, which can be useful for complex interactions.

However, it's important to manage dependencies carefully to avoid tight coupling. One way to mitigate this is by using interfaces or abstract classes to define the interactions between objects and the game state.

Would you like to discuss a specific scenario or example where you're considering this approach?

########################################
you
Delta time in pygame?

ddb
Delta time in Pygame is used to ensure that your game runs at a consistent speed regardless of the frame rate. You can calculate delta time by measuring the time elapsed between frames.

Here's a general approach:

Initialize a Clock:

clock = pygame.time.Clock()
Calculate Delta Time in the Game Loop:

delta_time = clock.tick(60) / 1000  # 60 FPS, convert milliseconds to seconds
Use Delta Time:

position += speed * delta_time
This ensures that your game logic is frame rate independent. Try implementing this and let me know if you have any questions!

########################################
you
Can I use gamestate as a parameter inside of methods for objects in the gamestate?

ddb
Yes, you can use gamestate as a parameter inside methods for objects in the gamestate. This can be useful for accessing and modifying the overall game state from within individual objects. Just ensure that you pass the gamestate object when calling these methods.

Would you like to share some code or a specific example where you're considering this approach?

you
Is that proper coding though? In Rust, for example, the compiler doesn't like that very much. It works in python though.

ddb
Using gamestate as a parameter inside methods for objects in the gamestate is a common practice in Python and can be perfectly fine. It allows objects to interact with the overall game state, which can be useful for complex interactions.

However, it's important to manage dependencies carefully to avoid tight coupling. One way to mitigate this is by using interfaces or abstract classes to define the interactions between objects and the game state.

Would you like to discuss a specific scenario or example where you're considering this approach?

##################################