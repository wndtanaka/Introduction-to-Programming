from cargo import Cargo
from depot import Depot
from truck import Truck


def new_depot(name, packages):
    depot = Depot(name)
    for c in packages:
        depot.add_cargo(c)
    return depot


def output_all(depots, trucks, idx):
    print("===Iteration {}===".format(idx))
    for t in trucks:
        output_truck(t)
    print()
    for d in depots:
        output_depot(d)
    print()


def output_depot(depot):
    if len(depot.get_contents()) > 0:
        print("Depot {} contains:".format(depot.get_name()))
        for c in depot.get_contents():
            print(c.get_description())
    else:
        print("Depot {} is empty".format(depot.get_name()))


def output_truck(truck):
    if not truck.has_stopped():
        if len(truck.get_contents()) > 0:
            print("Truck {} contains:".format(truck.get_name()))
            for c in truck.get_contents():
                print(c.get_description())
        else:
            print("Truck {} is empty".format(truck.get_name()))
    else:
        print("Truck Stop {} has stopped".format(truck.get_name()))


def simple_sim():
    routes = [
        new_depot("Bluefield", [
            Cargo('Utensils', "Washington"),
            Cargo('TVs', "Carrington")
        ]),
        new_depot("Jamestown", [
            Cargo('Phones', "Dartfield"),
            Cargo('Computers', "Bloomington")
        ]),
        new_depot("Washington", []),
        new_depot("Carrington", [
            Cargo('Toys', 'Bloomington')
        ]),
        new_depot("Bloomington", []),
        new_depot("Dartfield", [])
    ]

    t1 = Truck("Iron Giant", 4,
               [routes[0], routes[2], routes[4], routes[5]])
    t2 = Truck("The Train", 2,
               [routes[0], routes[1], routes[3], routes[4], routes[5]])

    trucks = [t1, t2]
    iteration = 1
    all_trucks_stopped = False

    while not all_trucks_stopped:
        all_trucks_stopped = True  # assume true
        output_all(routes, trucks, iteration)

        for t in trucks:
            if not t.has_stopped():
                all_trucks_stopped = False  # at least one truck is still moving
                d = t.current_depot()  # get the current depot of the truck
                d.take_cargo(t)  # the depot will take cargo to the truck
                d.give_cargo(t)  # the depot will give cargo to the truck
                t.move()  # the truck will move to the next depot

        # output_all(routes, trucks, iteration)
        iteration += 1


simple_sim()
