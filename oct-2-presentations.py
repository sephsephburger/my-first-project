mylista = [1, 2, 3]
print(mylista * 3)
# Outputs: [1, 2, 3, 1, 2, 3, 1, 2, 3]

temperature = 20
city = "Seoul"
sunpower = 2000
spffactor = 50
message = f"You will be hit with sunpower {sunpower/spffactor}"
message_2 = f"{city} is {temperature} degrees."

print(temperature)
print(message)
print(message_2)

listofspf = [25, 35, 50, 60]

print(listofspf)

for i in listofspf:
    print("String")

for i in listofspf:
    print(i)

if temperature < 35:
    print("I am cool.")

while temperature < 35:
    print("I am cool.")
    temperature = temperature + 5