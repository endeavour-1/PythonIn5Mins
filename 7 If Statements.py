temperature = input("Enter the Temperature: ")

if int(temperature) > 30:
    print("It's a Hot Day !")
    print("Drink Plenty of Water")
elif int(temperature) > 20:
    print("It's a Nice day !")
elif int(temperature) > 10:
    print("It's a bit Cold")
elif int(temperature) < 10:
    print("It's a Very Cold Day !")
    print("Stay Safe, Stay Warm")
print("Call 911 , for Assistance.")

