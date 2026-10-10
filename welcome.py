#Step 1 - paste this in and run it so you can see what it does:


name = "Amina"
print("Hello, " + name + "! Welcome to PLP.")

name = "Brian"
print("Hello, " + name + "! Welcome to PLP.")

name = "Fatuma"
print("Hello, " + name + "! Welcome to PLP.")### Step 2: Define the welcome function with the missing return line
def welcome(name):
    # Return the greeting sentence here, using the name
    return f"Hello, {name}! Welcome to PLP."

# Step 3 & 4: Call the function three times and print the results
print(welcome("Amina"))
print(welcome("Brian"))
print(welcome("Fatuma"))
