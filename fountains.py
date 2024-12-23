from datetime import datetime
import random
import time
import threading
from itertools import product

# creating a lock so with that make sure only one thread can access printing
print_lock = threading.Lock()

# control the time of being on and off and cycles
def control_fountain(fountain_id, color=None):
    
    cycles = random.randint(1, 3)

    for i in range(cycles):

        on_time = random.randint(1, 5)
        off_time = random.randint(1, 5)

        if i == cycles - 1:
            off_time = 0
        
        with print_lock:
            start_time = datetime.now().strftime("%H:%M:%S")
            if color:
                print(f"Fountain {fountain_id} (Color: {color}) started in : {start_time}")
            else:
                print(f"Fountain {fountain_id} started in : {start_time}")

        time.sleep(on_time)

        with print_lock:
            end_time = datetime.now().strftime("%H:%M:%S")
            if color:
                print(f"Fountain {fountain_id} (Color: {color}) finished in : {end_time}")
            else:
                print(f"Fountain {fountain_id} finished in : {end_time}")

        time.sleep(off_time)


# control the fountains start and end sequentially
def sequential_fountains():
    print("[ Sequential Fountains ]")
    
    threads = [
        threading.Thread(target=control_fountain, args=(1,)),
        threading.Thread(target=control_fountain, args=(2,)),
        threading.Thread(target=control_fountain, args=(3,))
    ]

    for thread in threads:
        thread.start()
        thread.join()
        print() # to seprate the fountains


# control the fountains start and end two by two
def pairs_fountains():
    print("\n[ Pairs of Fountains ]")
    
    pairs = [(1,2), (1,3), (2,3)]

    for pair in pairs:
        threads = []
        for fountain_id in pair:
            thread = threading.Thread(target=control_fountain, args=(fountain_id,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        print() # to seprate the combinations      


# control the fountains start all together and end with color and without it
def all_simultaneously(use_colors=True):

    if use_colors:
        print("\n[ All fountains simultaneously with color variations ]")
    else:
        print("\n[ All fountains simultaneously ]")

    # possible colors for fountains if they includes colores
    colors = ["Blue", "Red", "Green"] if use_colors else [""]

    # Generate all possible combinations for fountains
    color_combinations = list(product(colors, repeat=3))

    # Loop through each color combination
    for combo in color_combinations:
        threads = [
            threading.Thread(target=control_fountain, args=(1, combo[0])),
            threading.Thread(target=control_fountain, args=(2, combo[1])),
            threading.Thread(target=control_fountain, args=(3, combo[2]))
        ]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print()  # to separate the color combination

#call the functions
sequential_fountains()
pairs_fountains()
all_simultaneously(False)
all_simultaneously()