import random

# Lists for different parts of the story
openings = ["Once upon a time", "In a faraway land", "It was a dark and stormy night", "Long ago, in a kingdom far away"]
characters = ["a brave knight", "a curious explorer", "a mischievous wizard", "a determined detective"]
settings = ["a mystical forest", "an ancient castle", "a bustling city", "a deserted island"]
conflicts = ["must save the kingdom from a great evil", "searches for a legendary treasure", "solves a mysterious murder case", "learns to overcome their deepest fears"]
twists = ["discovers a shocking secret", "befriends an unexpected ally", "faces a betrayal from a trusted friend", "unravels a hidden prophecy"]
emotions = ["love", "loss", "hope", "fear"]
endings = ["and they lived happily ever after", "leaving behind a legacy that would never be forgotten", "forever changed by their extraordinary journey", "realizing that the true treasure was friendship all along"]

# Generate a random story
def generate_story():
    opening = random.choice(openings)
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    twist = random.choice(twists)
    emotion = random.choice(emotions)
    ending = random.choice(endings)

    story = f"{opening}, {character} set out on a quest in {setting}. Along the way, they {conflict} but soon {twist}. As they journeyed, they grappled with feelings of {emotion}. In the end, {ending}."

    return story
