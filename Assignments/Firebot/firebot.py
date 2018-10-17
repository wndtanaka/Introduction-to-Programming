import sys
from simulation import Simulation


# display map
def show_map(map, width, height, command):
    print('+' + '-' * (width * 2 - 1) + '+')
    for line in map:
        char_counter = 0
        print('|', end='')
        for tree in line:
            # if command is 'show height'
            if 'show' in command and 'height' in command:
                if tree.get_height() > 0 and tree.alive:
                    if char_counter < width - 1:
                        print(tree.get_height(), end=' ')
                    else:
                        print(tree.get_height(), end='')
                elif not tree.alive:
                    if char_counter < width - 1:
                        print('x', end=' ')
                    else:
                        print('x', end='')
                else:
                    if char_counter < width - 1:
                        print(" ", end=' ')
                    else:
                        print(" ", end='')
            # if command is 'show fire'
            if 'show' in command and 'fire' in command:
                if tree.get_fire_level() == 0 and not tree.is_on_fire() and tree.alive:
                    if char_counter < width - 1:
                        print(" ", end=' ')
                    else:
                        print(" ", end='')
                elif tree.is_on_fire() and tree.is_alive():
                    if char_counter < width - 1:
                        print(tree.get_fire_level(), end=' ')
                    else:
                        print(tree.get_fire_level(), end='')
                elif not tree.alive:
                    if char_counter < width - 1:
                        print('x', end=' ')
                    else:
                        print('x', end='')
                else:
                    if char_counter < width - 1:
                        print('.', end=' ')
                    else:
                        print('.', end='')
            char_counter += 1
        print('|')
    print('+' + '-' * (width * 2 - 1) + '+\n')


# start fire
def start_fire(map, x=None, y=None, width_region=None, height_region=None):
    # if not region fire
    if width_region is None and height_region is None:
        if x == 'all':  # if 'fire all'
            for line in map:
                for tree in line:
                    if not tree.is_on_fire() and tree.get_height() > 0:
                        tree.burn_tree()
        else:  # if a single fire
            map[y][x].burn_tree()
    else:  # if region fire
        if map[y][x].height > 0 and not map[y][x].on_fire:
            map[y][x].burn_tree()
        for i in range(height_region):
            for j in range(width_region):
                if not map[y + i][x + j].is_on_fire() and map[y + i][x + j].get_height() > 0:
                    map[y + i][x + j].burn_tree()


# extinguish fire
def extinguish_fire(map, x=None, y=None, width_region=None, height_region=None):
    # if not region extinguish
    if width_region is None and height_region is None:
        if x == 'all':  # if 'extinguish all'
            for line in map:
                for tree in line:
                    if tree.is_on_fire() and tree.fire_level > 0:
                        tree.extinguish_fire()
        else:  # if a single extinguish
            map[y][x].extinguish_fire()
    else:  # if region extinguish
        if map[y][x].height > 0:
            map[y][x].extinguish_fire()
        for i in range(height_region):
            for j in range(width_region):
                if map[y + i][x + j].is_on_fire() and map[y + i][x + j].fire_level > 0:
                    map[y + i][x + j].extinguish_fire()


# set wind direction
def set_wind(direction=None, wind=None):
    directions = ['all', 'none', 'east', 'south', 'west', 'north']
    if direction in directions:
        return direction
    return wind


# print status firebot
def get_status():
    print('''Day: {}\nWind: {}\n'''.format(current_day, wind))
    pass


# advance to next <days>
def next_days(current_day, map, wind, pollution, days=1):
    n = 0
    current_day += days
    # loop <days> times
    while n < days:
        # set wind effect to trees
        for line in map:
            for tree in line:
                if tree.is_on_fire() and (wind == 'east' or wind == 'all') and line.index(tree) < len(line) - 1 and \
                        map[map.index(line)][line.index(tree) + 1].height != 0:
                    map[map.index(line)][line.index(tree) + 1].wind_affected = True
                if tree.is_on_fire() and (wind == 'west' or wind == 'all') and line.index(tree) > 0 and \
                        map[map.index(line)][line.index(tree) - 1].height != 0:
                    map[map.index(line)][line.index(tree) - 1].wind_affected = True
                if tree.is_on_fire() and (wind == 'north' or wind == 'all') and map.index(line) > 0 and \
                        map[map.index(line) - 1][line.index(tree)].height != 0:
                    map[map.index(line) - 1][line.index(tree)].wind_affected = True
                if tree.is_on_fire() and (wind == 'south' or wind == 'all') and map.index(line) < len(map) - 1 and \
                        map[map.index(line) + 1][line.index(tree)].height != 0:
                    map[map.index(line) + 1][line.index(tree)].wind_affected = True
        # increment tree fire level and spread the fire if tree is wind affected
        for line in map:
            for tree in line:
                if tree.is_on_fire() and tree.alive:
                    tree.damage_tree()
                    tree.burn_tree()
                if tree.wind_affected and tree.alive:
                    tree.damage_tree()
                    tree.burn_tree()
        pollution = calculate_pollution(pollution)
        n += 1
    return current_day, pollution


# print data
def display_data(map, pollution):
    total_tree = 0
    burnt_tree = 0
    for line in map:
        for tree in line:
            if (tree.alive and tree.height > 0) or tree.on_fire or (not tree.alive and tree.height == 0):
                total_tree += 1
            if not tree.alive:
                burnt_tree += 1
    print('Damage: {:.2f}%'.format(burnt_tree / total_tree * 100))
    print('Pollution: {}\n'.format(pollution))


def calculate_pollution(pol):
    total_fire_level = 0
    total_tree_height = 0
    for line in map:
        for tree in line:
            if tree.alive and tree.height > 0:
                total_tree_height += tree.get_height()
            if tree.is_on_fire() and tree.fire_level > 0 and tree.alive:
                total_fire_level += tree.get_fire_level()
    pollution = pol + total_fire_level - total_tree_height
    if pollution <= 0:
        pollution = 0
    return pollution


def display_help():
    print('''BYE
HELP

DATA
STATUS

NEXT <days>
SHOW <attribute>

FIRE <region>
WIND <direction>
EXTINGUISH <region>\n''')


try:
    if len(sys.argv) != 4:
        raise ValueError
    seed = int(sys.argv[1])  # random seed tree generator
    width = int(sys.argv[2])  # width of the land
    height = int(sys.argv[3])  # height of the land
    if height < 0 or width < 0 or seed < 0:
        raise ValueError
    current_day = 0
    current_pollution = 0
    wind = 'none'
    is_quit = False

    sim = Simulation(seed, width, height)
    map = sim.generate_trees(seed)

    while not is_quit:
        if current_day == 0:
            print('''Day: {}\nWind: {}\n'''.format(1, wind))
            current_day += 1
        command = input('> ')
        if command == '':
            is_quit = True
            print('bye')
            break
        command = command.lower()  # make the command lowercase
        command = command.split()  # separate the command into list
        if 'bye' in command and len(command) == 1:
            is_quit = True
            print('bye')
            break
        elif 'show' in command and 'height' in command and len(command) == 2:
            show_map(map, width, height, command)
        elif 'show' in command and 'fire' in command and len(command) == 2:
            show_map(map, width, height, command)
        elif 'fire' in command and 'fire' == command[0] and 2 <= len(command) <= 5:
            can = True
            if len(command) > 2:
                for i in range(1, len(command)):
                    if not command[i].isdigit():
                        print('Invalid command\n')
                        can = False
                        break
            if can:
                if len(command) == 3:
                    x = int(command[1])
                    y = int(command[2])
                    if x < width and y < height:
                        if not map[y][x].on_fire and map[y][x].height > 0:
                            start_fire(map, x, y)
                            print('Started a fire\n')
                        else:
                            print('No fires were started\n')
                    else:
                        print('Invalid command\n')
                elif len(command) == 5 and int(command[3]) > 0 and int(command[4]) > 0:
                    x = int(command[1])
                    y = int(command[2])
                    if x < width and y < height:
                        region_h = False
                        region_w = False
                        if int(command[3]) + x <= width:
                            width_region = int(command[3])
                            region_w = True
                        if int(command[4]) + y <= height:
                            height_region = int(command[4])
                            region_h = True
                        if region_w and region_h:
                            can_region_fire = False
                            for i in range(height_region):
                                for j in range(width_region):
                                    if not map[y + i][x + j].on_fire and map[y + i][x + j].alive and map[y + i][
                                        x + j].height > 0:
                                        can_region_fire = True
                                        break
                                    else:
                                        can_region_fire = False
                                if can_region_fire:
                                    break
                            if can_region_fire:
                                start_fire(map, x, y, width_region, height_region)
                                print('Started a fire\n')
                            else:
                                print('No fires were started\n')
                        else:
                            print('Invalid command\n')
                    else:
                        print('Invalid command\n')
                elif len(command) == 2 and command[1] == 'all':
                    check_fire = False
                    for line in map:
                        for tree in line:
                            if not tree.on_fire and tree.height > 0:
                                check_fire = True
                                break
                            else:
                                check_fire = False
                        if check_fire:
                            break
                    if check_fire:
                        print('Started a fire\n')
                        start_fire(map, command[1])
                    else:
                        print('No fires were started\n')
                else:
                    print('Invalid command\n')
        elif 'extinguish' in command and 'extinguish' == command[0] and 2 <= len(command) <= 5:
            can = True
            if len(command) > 2:
                for i in range(1, len(command)):
                    if not command[i].isdigit():
                        print('Invalid command\n')
                        can = False
                        break
            if can:
                if len(command) == 3:
                    x = int(command[1])
                    y = int(command[2])
                    if x < width and y < height:
                        if map[y][x].on_fire and map[y][x].fire_level > 0 and map[y][x].alive:
                            extinguish_fire(map, x, y)
                            print('Extinguished fires\n')
                        else:
                            print('No fires to extinguish\n')
                    else:
                        print('Invalid command\n')
                elif len(command) == 5 and int(command[3]) > 0 and int(command[4]) > 0:
                    x = int(command[1])
                    y = int(command[2])
                    if x < width and y < height:
                        region_h = False
                        region_w = False
                        if int(command[3]) + x <= width:
                            width_region = int(command[3])
                            region_w = True
                        if int(command[4]) + y <= height:
                            height_region = int(command[4])
                            region_h = True
                        if region_w and region_h:
                            can_region_extinguish = False
                            for i in range(height_region):
                                for j in range(width_region):
                                    if map[y + i][x + j].is_on_fire() and map[y + i][x + j].alive:
                                        can_region_extinguish = True
                                        break
                                    else:
                                        can_region_extinguish = False
                                if can_region_extinguish:
                                    break
                            if can_region_extinguish:
                                extinguish_fire(map, x, y, width_region, height_region)
                                print('Extinguished fires\n')
                            else:
                                print('No fires to extinguish\n')
                        else:
                            print('Invalid command\n')
                    else:
                        print('Invalid command\n')
                elif len(command) == 2 and command[1] == 'all':
                    check_fire = False
                    for line in map:
                        for tree in line:
                            if tree.fire_level > 0 and tree.height > 0:
                                check_fire = True
                                break
                            else:
                                check_fire = False
                        if check_fire:
                            break
                    if check_fire:
                        print('Extinguished fires\n')
                        extinguish_fire(map, command[1])
                    else:
                        print('No fires to extinguish\n')
                else:
                    print('Invalid command\n')
        elif 'wind' in command and len(command) == 2:
            wind_dir = ['all', 'none', 'east', 'south', 'west', 'north']
            if command[1] in wind_dir:
                wind = set_wind(command[1], wind)
                print('Set wind to {}\n'.format(wind))
            else:
                print('Invalid command\n')
        elif 'next' in command and 1 <= len(command) <= 2:
            can = True
            if len(command) == 2:
                if not command[1].isdigit() or int(command[1]) <= 0:
                    print('Invalid command\n')
                    can = False
            if can:
                if len(command) == 1:
                    current_day, current_pollution = next_days(current_day, map, wind, current_pollution)
                    get_status()
                    data_checked = False
                elif len(command) == 2:
                    current_day, current_pollution = next_days(current_day, map, wind, current_pollution,
                                                               int(command[1]))
                    get_status()
                    data_checked = False
        elif 'status' in command and len(command) == 1:
            get_status()
        elif 'help' in command and len(command) == 1:
            display_help()
        elif 'data' in command and len(command) == 1:
            display_data(map, current_pollution)
        else:
            print('Invalid command\n')
except EOFError:
    print('\nbye')
except AssertionError:
    print('Usage: python firebot.py <seed> <width> <height>')
except ValueError:
    print('Usage: python firebot.py <seed> <width> <height>')
except ArithmeticError:
    print('Invalid command')
