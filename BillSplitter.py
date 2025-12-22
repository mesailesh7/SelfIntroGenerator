import textwrap

group = int(input("How many people are in the group?"))
groupName = []

for i in range(group):
    groupName.append(input("What is your name?"))

billTotal = int(input("what is the total amount of the bill"))

totalBill = billTotal / group

print(f"\n Total Bill: {billTotal}")
print(f"\n People: {groupName}")
print(f"\n Each person should pay {totalBill}")

for i in range(group):
    print(f"\n {groupName[i]} owes {totalBill}")
