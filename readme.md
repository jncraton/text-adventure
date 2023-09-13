Text Adventure
==============

The purpose of this lab is to create a piece of [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction) in the form of a text adventure game. If you are unfamiliar with the text adventure genre, [Colassal Cave Adventure](https://rickadams.org/adventure/advent/) or [AI Dungeon](https://play.aidungeon.io/main/newGame) are examples.

Requirements
------------

When run, your program should tell a story that includes various decision points that allow the reader experience alternate storylines. You won't be graded on the quality of your prose, but it might be more fun to explore a meaningful narrative.

On the technical end, your program must include the following:

- `input` to collect instructions from the user as needed
- `print` to display your narrative to the user
- `if`, `elif`, and `else` to branch into different parts of the story
- `exit` to end your program as needed

Your storyline much branch at least 4 times, and use all of `if`, `elif`, and `else` at least once.

Example
-------

Here is an example start to a possible fantasy narrative:

```python
print("You are alone in a dark cave. There is a sword next to you.")
print("1) Take the sword")
print("2) Leave the cave")

choice = input("Enter your choice: ")

if choice == '2':
    print("You leave the cave and are immediate killed by a goblin.")
    exit()

print("You take the sword and leave the cave.")
print("A goblin sees you attacks, but you block with your sword.")
```
