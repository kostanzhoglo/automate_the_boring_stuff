import random

messages = ["It is certain", 
    "It is decidely so", 
    "Yes", 
    "Reply hazy try again", 
    "Ask again later", 
    "Concentrate and ask again", 
    "My reply is no", 
    "Outlook not good", 
    "Very doubtful"]

print(random.choice(messages))
# same thing as above...  
    # print(messages[random.randint(0, len(messages) - 1)])