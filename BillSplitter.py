import textwrap


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number")


group = int(input("How many people are in the group?"))
groupName = []

for i in range(group):
    groupName.append(input("What is your name?"))

billTotal = get_float("what is the total amount of the bill")

totalBill = round(billTotal / group, 2)

print(f"\n Total Bill: {billTotal}")
print(f"\n People: {groupName}")
print(f"\n Each person should pay {totalBill}")

for i in range(group):
    print(f"\n {groupName[i]} owes {totalBill}")
