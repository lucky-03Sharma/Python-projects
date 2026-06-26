import random 

subjects = ["The government",
        "Virat Kohli",
        "Scientists",
        "Celebrities",
        "Politicians",
        "Tech companies",
        "Doctors", 
        "AutoRikshaw driver from Delhi"
        "Shah Rukh Khan" , 
        "Nirmala Sitaraman"
        ]
actions = ["announced",
              "revealed",
              "claimed",
              "denied",
              "confirmed",
              "warned",
              "criticized",
              "praised",
              "investigated",
              "proposed"
             ]

places= [
    "New Delhi",
    "in Mumbai local train",
    "in the sky",
    "on the moon",
    "in the ocean",
    "in the desert",
    "in the mountains",
    "in the forest",
    " at the end of the day ",
    "inside the parliament",
    "during the ipl match"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"{subject} {action} {place}."
    print(f"\n{headline}")

    user_input = input("Do you want to generate another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        break

print("Thank you for using the Fake News Generator!")    
