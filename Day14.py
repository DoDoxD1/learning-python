import random
from replit import clear
from art import logo_hl
from art import vs
from data import data

score = 0
while True:
    print(logo_hl)
    if(score>0): print(f"You're right! Current score: {score}.")
    person1 = random.choice(data)
    person2 = random.choice(data)
    print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}")
    print(vs)
    print(f"Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (choice=='a' and person1["follower_count"]>=person2["follower_count"]) or (choice=='b' and person1["follower_count"]<=person2["follower_count"]):
        score += 1
    else:
        break
    clear()
print(f"Sorry, that's wrong. Final score: {score}")