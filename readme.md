# Text Adventure

This program creates a piece of [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction) in the form of a text adventure game. If you are unfamiliar with the text adventure genre, [Colassal Cave Adventure](https://rickadams.org/adventure/advent/) is one example.

## Learning Outcomes

After completing this experience, learners will be able to:

1. Use `input` to collect user instructions
2. Use `print` to display narrative text
3. Implement conditional logic with `if`, `elif`, and `else`
4. Use nested conditional statements to manage complex narrative paths
5. Control program flow using `exit`

## Usage

Run your program using Python:

```bash
python adventure.py
```

Example interaction:

```
You are alone in a dark cave. There is a sword next to you.
1) Take the sword
2) Leave the cave
Enter your choice: 1
You take the sword and leave the cave.
A goblin sees you and attacks, but you block with your sword.
```

## Testing

if choice == "2":
    print("You leave the cave. You are killed by a goblin outside.")
    exit()

print("You take the sword and leave the cave.")
print("A goblin sees you and attacks, but you block with your sword.")
```

## Tasks

1. Define the starting point of your narrative in `adventure.py`.
2. Use `input` to collect choices from the player.
3. Implement at least four `if` statements to branch the story.
4. Use `elif` and `else` at least once each to handle multiple options and defaults.
5. Create at least one nested `if` statement for a multi-layered decision.
6. Use `exit()` to end the story at appropriate points.

## Resources

- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Colossal Cave Adventure](https://rickadams.org/adventure/advent/)
