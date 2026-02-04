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

Handout code is provided in [adventure.py](adventure.py). This program can be run in Thonny or a Python environment of your choice.

Example interaction:

```
You are alone in a dark cave. There is a sword next to you.
1) Take the sword
2) Leave the cave
Enter your choice: 1
You take the sword and leave the cave.
A goblin sees you and attacks, but you block with your sword.
```

## Tasks

When run, your program should tell a story that includes various decision points that allow the reader experience alternate storylines. You won't be graded on the quality of your prose, but it might be more fun to explore a meaningful narrative.

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
