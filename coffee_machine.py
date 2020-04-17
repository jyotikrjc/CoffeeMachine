stock = [400, 540, 120, 9, 550]     # water, milk, beans, cups, money
class CoffeeMachine:
    stock = [400, 540, 120, 9, 550]

    def __init__(self):
        water=400
        milk=540
        beans=120
        cups=9
        money=550

    def state(self):
        global stock
        print(f'The coffee machine has\n'
              f'{stock[0]} of water\n'
              f'{stock[1]} of milk\n'
              f'{stock[2]} of coffee beans\n'
              f'{stock[3]} of disposable cups\n'
              f'${stock[4]} of money\n')
    def sell(self,coffee_type):
        global stock
        inputs_names = ['water', 'milk', 'coffee beans', 'disposable cups', 'price']
        inputs = [['espresso', 'latte', 'cappuccino'],
                  [250, 0, 16, 1, 4],   # espresso needs
                  [350, 75, 20, 1, 7],  # latte needs
                  [200, 100, 12, 1, 6]]     # cappuccino needs
        if coffee_type != 'back':
            coffee_type = int(coffee_type)
            a = True
            for i in range(0, 4):
                if stock[i] < int(inputs[coffee_type][i]):
                    print(f'Sorry, not enough {inputs_names[i]}!')
                    a = False
            if a:
                print('I have enough resources, making you a coffee!')
                for i in range(0, 4):
                    stock[i] -= inputs[coffee_type][i]
                stock[4] += inputs[coffee_type][4]
        print('')
        pass


    def fill(self,stock1):
        global stock
        stock[0] +=stock1[0]
        stock[1] +=stock1[1]
        stock[2] +=stock1[2]
        stock[3] +=stock1[3]
        print('')
        pass


    def take(self):
        global stock
        print(f'I gave you ${stock[4]}\n')
        stock[4] = 0
        pass


coffee_machine=CoffeeMachine()
stock1=[0,0,0,0]
while True:
                    action = input('Write action (buy, fill, take, remaining, exit):\n')
                    print('')
                    if action == 'exit':
                        break
                    elif action == 'remaining':
                        coffee_machine.state()
                    elif action == 'buy':
                        coffee_type = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n'))
                        coffee_machine.sell(coffee_type)
                    elif action == 'fill':
                        stock1[0] = int(input(f'Write how many ml of water do you want to add:\n'))
                        stock1[1] = int(input(f'Write how many ml of milk do you want to add:\n'))
                        stock1[2] = int(input(f'Write how many grams of coffee beans do you want to add:\n'))
                        stock1[3] = int(input(f'Write how many disposable cups of coffee do you want to add:\n'))
                        coffee_machine.fill(stock1)
                    elif action == 'take':
                        coffee_machine.take()
                    else:
                        print("Option doesn't exist")
                    pass
