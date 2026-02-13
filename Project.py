import random

def generate_ticket():
    numbers = random.sample(range(1, 91), 15)
    numbers.sort()
    return numbers

def check_full_house(ticket, marked):
    return set(ticket) == set(marked)

def play_tambola():
    print("Welcome to Tambola Game\n")

    players = int(input("Enter number of players: "))
    tickets = {}
    marked_numbers = {}
    
    for i in range(1, players + 1):
        ticket = generate_ticket()
        tickets[i] = ticket
        marked_numbers[i] = []
        print(f"\nPlayer {i} Ticket: {ticket}")

    numbers = list(range(1, 91))
    random.shuffle(numbers)

    print("\nGame Started!\n")

    for number in numbers:
        input("Press Enter to draw next number...")
        print(f"Number Drawn: {number}")

        for i in range(1, players + 1):
            if number in tickets[i]:
                marked_numbers[i].append(number)
                print(f"Player {i} marked {number}")

                if check_full_house(tickets[i], marked_numbers[i]):
                    print(f"\n🎉 Player {i} wins Full House!")
                    return

    print("Game Over!")

play_tambola()
