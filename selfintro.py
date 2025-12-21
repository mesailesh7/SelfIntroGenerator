# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import datetime

name = input("What is your name").strip()
age = input("How old are you").strip()
city = input("Which city do you life in?").strip()
profession = input("What is your favorite profession").strip()
hobby = input("What is your favorite hobby").strip()

intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}"
    f"I work as {profession} and I absolutely enjoy {hobby} in my free time"
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)