import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "Try consulting a doctor..."


def unknown():
    response = ["Can you please check the spelling of your symptoms ",
                "Sorry please re-write",
                "Unable to find the disease based on your symptoms",
                "Try writing other symptoms!!"][
        random.randrange(4)]
    return response