"""
Adventure Game Scoring System

1. Starting Score
   Every player starts with 0 points at the beginning of the game.

2. Exploration Rewards
   - Finding the Sword in the Cave: +10 points
   - Checking the cave again (curiosity): +1 point
   - Knocking on the House (optional): +0 points (neutral, risk-based)

3. Combat Outcomes
   - Fight with Sword of Slaying (victory): +20 points
   - Fight with Dagger (defeat): -10 points
   - Run Away from Enemy: -2 points

4. Optional Bonus
   You can add more points to encourage exploration:
   - Entering every area at least once: +1 point
   - Trying all options in a field/cave: +1-5 points per unique action
"""

import time
import random


def print_pause(message, delay=2):
    """Print a message with a short pause."""
    print(message)
    time.sleep(delay)


def valid_input(prompt, options):
    """Ask for valid input until the player enters a valid choice."""
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        print_pause("Sorry, that’s not a valid option.", 1)


def show_score(score):
    """Display the current score."""
    print_pause(f"[ Current Score: {score} ]", 1)


def intro(enemy, weapon, score):
    """Introduce the player to the game setting."""
    print_pause(
        "You find yourself standing in an open field, filled with grass "
        "and yellow wildflowers."
    )
    print_pause(
        f"Rumor has it that a wicked {enemy} lurks nearby, terrifying "
        "the village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        f"In your hand, you hold your trusty (but not very effective) "
        f"{weapon}."
    )
    show_score(score)


def field(enemy, weapon, special_weapon_found, score):
    """The player chooses where to go."""
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = valid_input("What would you like to do? (1 or 2): ", ["1", "2"])
    show_score(score)
    if choice == "1":
        house(enemy, weapon, special_weapon_found, score)
    else:
        cave(enemy, weapon, special_weapon_found, score)


def cave(enemy, weapon, special_weapon_found, score):
    """Handle exploring the cave."""
    if not special_weapon_found:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock...")
        print_pause(f"You have found the magical Sword of {enemy} Slaying!")
        print_pause(
            "You discard your old dagger and take the sword with you."
        )
        weapon = "Sword of Slaying"
        special_weapon_found = True
        score += 10  # reward for finding the special weapon
    else:
        print_pause("You peer into the cave again.")
        print_pause("You've been here before. It's just an empty cave now.")
        score += 1  # small reward for curiosity
    show_score(score)
    field(enemy, weapon, special_weapon_found, score)


def house(enemy, weapon, special_weapon_found, score):
    """Handle entering the house."""
    print_pause("You walk up to the door of the house.")
    print_pause(
        f"You are about to knock when the door opens "
        f"and out steps a {enemy}."
    )
    print_pause(f"Eep! This is the {enemy}’s house!")
    print_pause(f"The {enemy} attacks you!")
    if weapon == "dagger":
        print_pause("You feel under-prepared for this fight...")
    show_score(score)
    fight(enemy, weapon, special_weapon_found, score)


def fight(enemy, weapon, special_weapon_found, score):
    """Handle fighting or running away."""
    choice = valid_input(
        "Would you like to (1) fight or (2) run away? ", ["1", "2"]
    )
    if choice == "1":
        if weapon == "Sword of Slaying":
            print_pause(
                f"As the {enemy} lunges, you raise your glowing "
                "Sword of Slaying!"
            )
            print_pause(
                f"The {enemy} takes one look at your sword... and flees!"
            )
            print_pause(
                f"You have rid the village of the {enemy}. "
                "Victory is yours!"
            )
            score += 20
        else:
            print_pause("You fight bravely...")
            print_pause(f"But your dagger is no match for the {enemy}.")
            print_pause("You have been defeated.")
            score -= 10
    else:
        print_pause(
            "You run back into the field. Luckily, you don’t seem "
            "to have been followed."
        )
        score -= 2
        show_score(score)
        field(enemy, weapon, special_weapon_found, score)
        return  # keep game alive if fleeing

    show_score(score)
    print_pause(f"Your final score is: {score}")


def play_game():
    """Main game loop."""
    play = True

    while play:
        enemies = ["troll", "dragon", "pirate", "wicked faerie"]
        enemy = random.choice(enemies)
        weapon = "dagger"
        special_weapon_found = False
        score = 0

        intro(enemy, weapon, score)
        field(enemy, weapon, special_weapon_found, score)

        # Ask if player wants to play again
        choice = valid_input(
            "Would you like to play again? (y/n): ",
            ["y", "n"]
        )
        if choice == "n":
            print_pause("Thanks for playing! Goodbye.", 1)
            play = False
        else:
            print_pause("\nExcellent! Restarting the game...\n", 1)


if __name__ == "__main__":
    play_game()
