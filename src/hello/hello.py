def make_greeting(name, formality):
    return (
        "Greetings and felicitations, {}!".format(name)
        if formality
        else "Hello, {}!".format(name)
    )
