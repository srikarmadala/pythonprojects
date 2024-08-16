import random
import art
import gamedata

# Starting screen that prints the logo
print(art.logo[0])


# Function to get user choice
def user_choice():
    return input("Who has more followers? Type 'A' or 'B': ").lower()


# Function to generate a new random choice from game data
def get_random_choice():
    return gamedata.data[random.randint(0, len(gamedata.data) - 1)]


# Initialize the first choice and score
first_choice = get_random_choice()
score = 0

# Start the game loop
keep_going = True
while keep_going:
    second_choice = get_random_choice()

    # Ensure the second choice is different from the first
    while second_choice == first_choice:
        second_choice = get_random_choice()

    print(f"Compare A: {first_choice['name']}, {first_choice['description']}, from {first_choice['country']}")
    print(art.logo[1])
    print(f"Against B: {second_choice['name']}, {second_choice['description']}, from {second_choice['country']}")

    choice = user_choice()

    # Determine the correct answer
    if choice == "a" and first_choice['follower_count'] > second_choice['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}.")
        first_choice = second_choice  # Continue with the current winner
    elif choice == "b" and second_choice['follower_count'] > first_choice['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}.")
        first_choice = second_choice  # Continue with the current winner
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        keep_going = False

