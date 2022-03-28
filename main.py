def split_chars(text):
    return [char for char in text]


while True:
    selection = int(input("press '0' for encryption, press '1' for decryption, press '2' for exit\n"))
    text = input("Please enter text\n")
    text = text.upper()
    word = text.split(" ")
    final_text = ""
    if selection == 0:
        for x in word:
            text_chars = split_chars(x)
            for c in text_chars:
                character = ord(c) + 16
                if character > ord('Z'):
                    character = character - 26
                final_text += chr(character)
            final_text += ' '
    elif selection == 1:
        for x in word:
            text_chars = split_chars(x)
            for c in text_chars:
                character = ord(c) - 16
                if character < ord('A'):
                    character = character + 26
                final_text += chr(character)
            final_text += ' '
    else:
        break
    print(final_text)

