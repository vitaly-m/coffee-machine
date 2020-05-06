# Write your code here
class CoffeeMachine:
    fill_options = ["Write how many ml of water do you want to add:",
                    "Write how many ml of milk do you want to add:",
                    "Write how many grams of coffee beans do you want to add:",
                    "Write how many disposable cups of coffee do you want to add:"]

    def __init__(self, water, milk, beans, cups, money):
        self.avail_resources = [["water", water],
                           ["milk", milk],
                           ["coffee beans", beans],
                           ["disposable cups", cups]]
        self.avail_money = money
        self.state = "command"
        self.fill_state = 0

    def __str__(self):
        resources = "The coffee machine has:\n"
        for r in self.avail_resources:
            resources += f"{r[1]} of {r[0]}\n"
        resources += f"${self.avail_money} of money"
        return resources

    def buy(self, coffee, price):
        for i in range(len(coffee)):
            if self.avail_resources[i][1] - coffee[i] < 0:
                print("Sorry, not enough ", self.avail_resources[i][0])
                break
        else:
            print("I have enough resources, making you a coffee!")
            self.avail_money += price
            for i in range(len(coffee)):
                self.avail_resources[i][1] -= coffee[i]

    def take(self):
        print("I gave you $#".replace("#", str(self.avail_money)))
        self.avail_money = 0

    def fill(self, resource_id, amount):
        self.avail_resources[resource_id][1] += amount

    def state_greeting(self):
        if self.state == "command":
            return "Write action (buy, fill, take, remaining, exit):"
        elif self.state == "buy":
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
        elif self.state == "fill":
            return CoffeeMachine.fill_options[self.fill_state]
        else:
            return None

    def do_operation(self, operation):
        if self.state == "command":
            if operation == "exit":
                return False
            elif operation == "buy":
                self.state = "buy"
            elif operation == "fill":
                self.state = "fill"
                self.fill_state = 0
            elif operation == "remaining":
                print(self)
            elif operation == "take":
                self.take()
        elif self.state == "buy":
            if operation == "1":
                self.buy([250, 0, 16, 1], 4)
            elif operation == "2":
                self.buy([350, 75, 20, 1], 7)
            elif operation == "3":
                self.buy([200, 100, 12, 1], 6)
            self.state = "command"
        elif self.state == "fill":
            if self.fill_state < len(CoffeeMachine.fill_options):
                self.fill(self.fill_state, int(operation))
                self.fill_state += 1
                if self.fill_state == len(CoffeeMachine.fill_options):
                    self.state = "command"
        return True


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

print(coffee_machine.state_greeting())
while coffee_machine.do_operation(input()):
    print(coffee_machine.state_greeting())
