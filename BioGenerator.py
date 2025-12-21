import textwrap

name = input("What is your name? ").strip()
profession = input("What is your profession? ").strip()
Passion = input("What is your Passion? ").strip()
Emoji = input("What is your Emjoin? ").strip()
Website = input("What is your Website? ").strip()

print("\n Choose your Style: ")
print("1. Simple Lines")
print("2. Vertical Flairs")
print("3 Emoji Sandwich")

style = input("Enter 1,2 or 3:").strip()

def generate_bio(style):
    if style == "1":
        return f"{Emoji} {name} | {profession} \n {Passion} \n {Website}"
    elif style == "2":
        return f"{Emoji} {name} \n {profession} \n {Passion} \n {Website}🔥"
    elif style == "3":
        return f"{Emoji * 3}\n {name} - {profession} \n {Passion} \n {Website} \n {Emoji*3}"

bio = generate_bio(style)
print("\n Your stylish bio:")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a text file (y/n").lower()

if(save == "y"):
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File saved")