# TODO: Create a letter using "starting_letter.txt" and "invited_names.txt"

# Practice opening
# with open("Output/ReadyToSend/example.txt") as file:
#     template = file.read()
#     print(template)

# TODO 1: Place the names in "invited_names.txt" into a list, each as a single item
with open("./Input/Names/invited_names.txt") as ppl_file:
    persons = ppl_file.readlines()

# TODO 2: Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as template_file:
    template = template_file.read()

    # TODO 3: Save the letters in the folder "ReadyToSend".
    for person in persons:
        invite = template.replace("[name]", person.strip())  # .strip method removes spaces before and after a string.
        with open(f"./Output/ReadyToSend/invitation_{person.strip()}.txt", mode="w") as invitation:
            invitation.write(invite)

# Documentation
# https://www.w3schools.com/python/ref_file_readlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_string_strip.asp
