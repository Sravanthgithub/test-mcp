import random

def random_message():
    messages = [
        "Hello, world!",
        "Today is a great day!",
        "Random number: {}".format(random.randint(1, 100)),
        "Python is awesome!",
        "Keep coding!",
        "Automate everything!",
        "Testing random lines.",
        "GitHub automation FTW!",
        "Always commit your code!",
        "AI bots are cool!"
    ]
    for msg in messages:
        print(msg)

if __name__ == "__main__":
    random_message()