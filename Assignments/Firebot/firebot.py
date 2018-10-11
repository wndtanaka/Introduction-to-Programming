import sys
from simulation import Simulation


def show_map(map, width, height, command):
    map_h = len(map)  # height of the land
    line = -1
    print('+' + '-' * width + '+')
    for x in map:
        print('|', end='')
        for y in x:
            if 'show' in command and 'height' in command:
                if y.get_height() == 0:
                    print(" ", end='')
                else:
                    print(y.get_height(), end='')
            if 'show' in command and 'fire' in command:
                if y.get_fire_level() == 0 and not y.is_on_fire():
                    print(" ", end='')
                elif y.is_on_fire():
                    print(y.get_fire_level(), end='')
                else:
                    print('.', end='')
        print('|')
    print('+' + '-' * width + '+\n')


def start_fire(map, x=None, y=None, width_region=None, height_region=None):
    if x == 'all':
        for line in map:
            for tree in line:
                if not tree.is_on_fire() and tree.get_fire_level() != 0:
                    tree.burn_tree()
    else:
        map[y][x].burn_tree()


def set_wind(direction, wind):
    directions = ['all', 'none', 'east', 'south', 'west', 'north']
    if direction in directions:
        return direction
    return wind


def get_status():
    print('''Day: {}\nWind: {}\n'''.format(current_day, wind))
    pass


def next_days(current_day, map, days=1):
    n = 0
    current_day += days
    while n < days:
        for line in map:
            for tree in line:
                if tree.is_on_fire():
                    tree.burn_tree()
        n += 1
    return current_day


seed = int(sys.argv[1])  # random seed tree generator
width = int(sys.argv[2])  # width of the land
height = int(sys.argv[3])  # height of the land
current_day = 0
wind = 'none'
is_quit = False

sim = Simulation(seed, width, height)
map = sim.generate_trees(seed)
# print(len(map))
# show_map(map,width,height,'show height')
# show_map(map,width,height,'show fire')
# start_fire(map,4,0)
# show_map(map,width,height,'show fire')
# print(map[4][0].is_on_fire())

while not is_quit:
    if current_day == 0:
        print('''Day: {}\nWind: {}\n'''.format(1, wind))
        current_day += 1
    command = input('> ')
    command = command.lower()  # make the command lowercase
    command = command.split()
    if 'bye' in command:
        is_quit = True
        print('bye\n')
        break
    elif 'show' in command and 'height' in command:
        show_map(map, width, height, command)
    elif 'show' in command and 'fire' in command:
        show_map(map, width, height, command)
    elif 'fire' in command and len(command) >= 2:
        if len(command) == 3:
            x = int(command[1])
            y = int(command[2])
            if not map[y][x].on_fire:
                start_fire(map, x, y)
                print('Started a fire\n')
            else:
                print('No fires were started\n')
        elif len(command) == 5:
            x = int(command[1])
            y = int(command[2])
            width_region = int(command[3])
            height_region = int(command[4])
        elif len(command) == 2 and command[1] == 'all':
            print('Started a fire\n')
            start_fire(map, command[1])
            pass

    elif 'wind' in command and len(command) <= 2:
        wind = set_wind(command[1], wind)
        print('Set wind to {}\n'.format(wind))
    elif 'next' in command:
        if len(command) == 1:
            current_day = next_days(current_day, map)
            get_status()
        elif len(command) == 2:
            current_day = next_days(current_day, map, int(command[1]))
            get_status()
        pass
    elif 'status' in command:
        get_status()
