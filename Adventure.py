import random

class Farm:
    def __init__(self):
        self.animals = []
        self.money = 100  # Starting money
        self.day = 1
        self.inventory = {'feed': 10}  # Starting with some feed

    def add_animal(self, animal, cost):
        if self.money >= cost:
            self.animals.append({'type': animal, 'status': 'happy', 'health': 100, 'fed_today': False})
            self.money -= cost
            print(f"You have added a {animal} to your farm. It cost ${cost}.")
        else:
            print(f"Sorry, you don't have enough money to buy a {animal}. You need ${cost} but you only have ${self.money}.")

    def list_animals(self):
        if not self.animals:
            print("You have no animals on your farm.")
        else:
            print("Animals on your farm:")
            for animal in self.animals:
                print(f" - {animal['type']} (Status: {animal['status']}, Health: {animal['health']}, Fed Today: {animal['fed_today']})")
        print(f"Current balance: ${self.money}")
        print(f"Inventory: {self.inventory}")

    def feed_animal(self, animal_type):
        if self.inventory['feed'] <= 0:
            print("You don't have enough feed.")
            return

        for animal in self.animals:
            if animal['type'] == animal_type:
                animal['status'] = 'happy'
                animal['health'] = min(animal['health'] + 10, 100)
                animal['fed_today'] = True
                self.inventory['feed'] -= 1
                print(f"You have fed the {animal_type}. It is now happy and its health is {animal['health']}.")
                return
        print(f"You don't have a {animal_type} to feed.")

    def sell_animal(self, animal_type, price):
        for animal in self.animals:
            if animal['type'] == animal_type:
                self.animals.remove(animal)
                self.money += price
                print(f"You have sold a {animal_type} for ${price}.")
                return
        print(f"You don't have a {animal_type} to sell.")

    def earn_money(self, amount):
        self.money += amount
        print(f"You have earned ${amount}. Current balance: ${self.money}")

    def buy_feed(self, quantity, cost_per_feed):
        total_cost = quantity * cost_per_feed
        if self.money >= total_cost:
            self.inventory['feed'] += quantity
            self.money -= total_cost
            print(f"You have bought {quantity} feed for ${total_cost}.")
        else:
            print(f"Sorry, you don't have enough money to buy {quantity} feed. You need ${total_cost} but you only have ${self.money}.")

    def next_day(self):
        self.day += 1
        print(f"\nDay {self.day}:")
        self.daily_events()
        self.check_animal_health()
        for animal in self.animals:
            animal['fed_today'] = False  # Reset the fed status for the new day

    def daily_events(self):
        events = ["good_weather", "bad_weather", "nothing"]
        event = random.choice(events)
        if event == "good_weather":
            print("It's a sunny day! Your animals are happier.")
            for animal in self.animals:
                animal['status'] = 'happy'
        elif event == "bad_weather":
            print("It's a rainy day. Your animals are a bit stressed.")
            for animal in self.animals:
                animal['status'] = 'stressed'
        else:
            print("Nothing special happened today.")

    def check_animal_health(self):
        for animal in self.animals:
            if not animal['fed_today']:
                animal['health'] -= 20
                print(f"Your {animal['type']} was not fed today and its health is now {animal['health']}.")
            if animal['health'] <= 20 and animal['health'] > 0:
                print(f"Warning: Your {animal['type']} is in poor health (Health: {animal['health']}). Feed it soon!")
            if animal['health'] <= 0:
                print(f"Sadly, your {animal['type']} has died.")
                self.animals.remove(animal)

    def perform_task(self, task):
        if task == "sell_produce":
            amount = random.randint(10, 30)
            self.earn_money(amount)
            print(f"You sold produce and earned ${amount}.")

def main():
    farm = Farm()
    animal_costs = {'cow': 50, 'chicken': 20, 'sheep': 30}  # Define costs for each type of animal
    animal_prices = {'cow': 40, 'chicken': 15, 'sheep': 25}  # Define selling prices for each type of animal
    feed_cost_per_unit = 5  # Define the cost per unit of feed

    while True:
        print("\nWelcome to your farm!")
        print("1. Add an animal")
        print("2. List animals")
        print("3. Feed an animal")
        print("4. Sell an animal")
        print("5. Earn money")
        print("6. Perform a task")
        print("7. Buy feed")
        print("8. Next day")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            animal = input("What animal do you want to add? (cow, chicken, sheep) ").lower()
            if animal in animal_costs:
                farm.add_animal(animal, animal_costs[animal])
            else:
                print("Invalid animal. Please choose from cow, chicken, or sheep.")
        elif choice == '2':
            farm.list_animals()
        elif choice == '3':
            animal = input("Which animal do you want to feed? (cow, chicken, sheep) ").lower()
            farm.feed_animal(animal)
        elif choice == '4':
            animal = input("Which animal do you want to sell? (cow, chicken, sheep) ").lower()
            if animal in animal_prices:
                farm.sell_animal(animal, animal_prices[animal])
            else:
                print("Invalid animal. Please choose from cow, chicken, or sheep.")
        elif choice == '5':
            amount = int(input("How much money did you earn? "))
            farm.earn_money(amount)
        elif choice == '6':
            task = input("Which task do you want to perform? (sell_produce) ").lower()
            farm.perform_task(task)
        elif choice == '7':
            quantity = int(input("How many units of feed do you want to buy? "))
            farm.buy_feed(quantity, feed_cost_per_unit)
        elif choice == '8':
            farm.next_day()
        elif choice == '9':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()