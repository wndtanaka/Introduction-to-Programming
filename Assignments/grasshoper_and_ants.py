class Menu:
    def __init__(self):
        # hold variables
        self.is_alive = True
        self.is_holding_food = False
        self.food_count = 0
        self.food_left = 3
        # TODO Make the level length and ants placement random generated
        self.level = ['[]', 'G', '.', '.', '.', 'a', '.', '.', 'a', '.', 'a', '.', '[***]']
        self.is_home = True
        self.nearby_nest = False
        self.player = 'G'
        self.game_won = False
        self.index = 99


def main():
    # while the player is alive, this part of code will keep looping
    while m.is_alive and not m.game_won:
        # Generate level
        for i in m.level[0:-1]:
            print(i, end=' ')
        print(m.level[-1])
        # Game is won if the food count is 3 or more
        if m.food_count >= 3:
            print("Congratulations Grasshopper, you now have enough food to last the winter!")
            m.game_won = True
            break
        # asking for user input
        command = input("Input your move: ").upper()
        # quitting the game
        if command == 'QUIT':
            print('Goodbye Grasshopper')
            break
        # move_indexing function will return index that will be pass into move function
        index = move_indexing(command)
        # if the input is correct (no error)
        if index != 99:
            m.level = move(index, m.level)
        else:
            print("Invalid command")


# this function to translate command to index number
def move_indexing(command):
    command = command.upper()
    if command == 'WALK L':
        index = -1
    elif command == 'WALK R':
        index = 1
    elif command == 'HOP L':
        index = -2
    elif command == 'HOP R':
        index = 2
    elif command == 'PICK UP':
        index = 10
    elif command == 'DROP':
        index = 20
    else:
        # This will be index error
        index = 99
    return index


# this function 'generate' new level after player movement
def move(index, level):
    if -2 <= index <= 2:
        # predict next move location and store it into new variable
        next_move = level.index(m.player) + index
        try:
            # if step into ants
            if level[next_move] == 'a':
                print("Arrgh!! An Ant attacked you. Game over.")
                m.is_alive = False
                return level
            # out of bounds catching error
            if level[next_move] != '.':
                if index == -1 or index == -2:
                    level[1] = m.player
                    if not m.is_home:
                        level[next_move - index] = '.'
                if index == 1 or index == 2:
                    level[-2] = m.player
                    if not m.nearby_nest:
                        level[next_move - index] = '.'
            else:
                level[next_move] = m.player
                level[next_move - index] = '.'
        # error catching
        except IndexError:
            level[-2] = m.player
            if not m.nearby_nest:
                level[next_move - index] = '.'
    # dropping food if input is DROP and is next to home
    if index == 20 and m.is_home:
        if m.is_holding_food:
            m.is_holding_food = False
            m.food_count += 1
            m.player = 'G'
            level[level.index('G*')] = m.player
            print("Drop food")
        else:
            print("Not holding any food!")
    elif index == 20 and not m.is_home:
        print("Not in home")
    # steal food if input is PICK UP and is nearby ants nest and also food available is more than zero
    if index == 10 and m.nearby_nest and m.food_left > 0:
        # can only pick up one food at a time
        if not m.is_holding_food:
            m.is_holding_food = True
            m.player = 'G*'
            level[level.index('G')] = m.player
            m.food_left -= 1
            print("Picking up food")
        else:
            print("Can only carry one food at a time")
    # if not in ants nest or no more food to steal
    elif index == 10 and (not m.nearby_nest or m.food_left <= 0):
        print("Nothing to steal")
    # True if the player is next to Home
    m.is_home = True if m.level[1] == m.player else False
    # True if the player is next to Nest
    m.nearby_nest = True if m.level[-2] == m.player else False
    if m.food_left == 2:
        level[-1] = '[**]'
    elif m.food_left == 1:
        level[-1] = '[*]'
    elif m.food_left == 0:
        level[-1] = '[]'
    if m.food_count == 1:
        level[0] = '[*]'
    elif m.food_count == 2:
        level[0] = '[**]'
    elif m.food_count == 3:
        level[0] = '[***]'
    return level


if __name__ == "__main__":
    m = Menu()
    print("""
    Welcome to the Grasshopper and the Ants
    You a Grasshopper that starving during winter and has no food to survive.
    Steal food from the Ants.
    Avoid the colony or pay the consequences.
    How to play:
    WALK L = Move 1 tile to the left
    WALK R = Move 1 tile to the right
    HOP L = Move 2 tile to the left
    HOP R = Move 2 tile to the right
    PICK UP = Pick up food from Ant's Nest
    DROP = Drop food to your home
    QUIT = Quit the game
    """)
    main()
