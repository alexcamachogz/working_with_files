import shutil

NAMES_FILE = "./Input/Names/invited_names.txt"
EMAIL_FILE = "./Input/Letters/starting_letter.txt"

with open(NAMES_FILE, "r") as file:
    for line in file:
        # Save the current name and create the invitation file path
        name = line.strip()
        file_name = f"./Output/ReadyToSend/{name}.txt"

        # Copy starting_letter to ReadyToSend folder
        shutil.copy(EMAIL_FILE, file_name)

        # Open new file and read the content
        with open(file_name, "r") as invitation:
            content = invitation.read()

        # Replace the [name] placeholder with the current name
        modified_content = content.replace("[name]", name)

        # Save the invitation with the current name
        with open(file_name, "w") as final_invitation:
            final_invitation.write(modified_content)

print("New invitations are created")
