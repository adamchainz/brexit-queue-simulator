import time, random

from brexit.queue import Queue

#alien = Actor('truck')
#alien.pos = 500, 250 
#alien.angle += 90

lorry_id = 0

spacing = 150

def new_lorry():
    global lorry_id
    lorry_id += 1
    return lorry_id

banner = Actor("title")

def Truck(truckNo):
    myTruck = Actor('truck')
    myTruck.pos = 500 + truckNo * spacing, 250
    myTruck.angle = 90
    return myTruck

queue = Queue(5, delay_range=(6, 9))
queue.add(new_lorry())
queue.add(new_lorry())

WIDTH = 1000
HEIGHT = 500

trucks = {}

last_truck = 0

def maybe_add():
    global last_truck
    now = time.monotonic()
    if now > (last_truck + 5):
        queue.add(new_lorry())
        last_truck = now

def update():
    maybe_add()

    queue.check_complete()

    for idx, truck in enumerate(queue.queue):
        if truck not in trucks:
            trucks[truck] = Truck(truck)

        trucks[truck].desiredPos = idx * spacing + 200


    for truck_id, truck in trucks.items():
        
        if truck_id not in queue.queue:
            truck.desiredPos = -200

        if truck.pos[0] > truck.desiredPos:
            truck.pos = (truck.pos[0] - 5, truck.pos[1])


def draw():
    screen.clear()
    banner.draw()
    for truck in trucks.values():
        truck.draw()
