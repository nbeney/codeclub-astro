# Import what we need from the adventurelib library.
from adventurelib import when, start, Bag, Item

# Define the action to pick an object and add it to the bag.
@when("pick THING")
def pick(thing):
    bag.add(Item(thing))
    print(f"You have {len(bag)} items in your bag now.")

# Define the action to check what is in the bag.
@when("check")
def check_bag():
    if len(bag) == 0:
        print(f"Your bag is empty!")
    else:
        print(f"You have {', '.join(str(item) for item in bag)}")

# Define the action to take an object from the bag and throw it.
@when("throw THING")
def throw(thing):
    if thing in bag:
        bag.take(thing)
        if len(bag) == 0:
            print(f"Your bag is empty now!")
        else:
            print(f"You have {len(bag)} items left in your bag.")
    else:
        print(f"Sorry, you have no {thing} in your bag!")

if __name__ == "__main__":
    # Initialize some variables.
    bag = Bag()

    # Start the event loop. This should be the last line of your program.
    start()
