with open("./Input/Letters/starting_letter.txt") as start_latter:
    template_latter = start_latter.readlines()
    print(template_latter)

with open("./Input/Names/invited_names.txt") as names_file:
    all_names = names_file.readlines()

for name in all_names:
    name = name.strip("\n")
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_latter:
        for text in template_latter:
            new_text = text.replace("[name]", name)

            output_latter.write(new_text)
