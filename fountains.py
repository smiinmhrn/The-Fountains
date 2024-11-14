from datetime import datetime
import random
import time
import threading

# creating a lock so with that make sure only one tread can accsess printing
print_lock = threading.Lock()

# control the time of being on and off 
def control_fountain(fountain_id, on_time, off_time):

    # fountain start in current time and print the giving format
    with print_lock:
        start_time = datetime.now().strftime("%H:%M:%S")
        print(f"Fountain {fountain_id} started in : {start_time}")

    #sleep the time as being on
    time.sleep(on_time)

    # fountain end in current time and print the giving format
    with print_lock:
        end_time = datetime.now().strftime("%H:%M:%S")
        print(f"Fountain {fountain_id} ended in : {end_time}")
    
    #sleep the time as being off
    time.sleep(off_time)


# control the fountains start and end sequentially
def sequential_fountains():
    print("[ Sequential Fountains ]")
    
    # creat 3 treads as fountains and in each treads run the control_fountain fonction and give the fountain id, on time and off time (randomly) as args
    fountain1 = threading.Thread(target=control_fountain, args=(1, random.randint(1, 5), random.randint(1, 5)))
    fountain2 = threading.Thread(target=control_fountain, args=(2, random.randint(1, 5), random.randint(1, 5)))
    fountain3 = threading.Thread(target=control_fountain, args=(3, random.randint(1, 5), random.randint(1, 5)))

    # fountain[n].start start the fountain and fountain[n].join() make sure that the first thread do the job and finish and then run the other line
    fountain1.start()
    fountain1.join()  
    fountain2.start()
    fountain2.join()  
    fountain3.start()
    fountain3.join()


def pairs_fountains():
    print("\n[ Pairs of Fountains ]")
    
    # creat the pair of fountains that want to start. it includes a tupels that contains fountains id
    pairs = [(1,2), (1,3), (2,3)]


    # for each pair creat a same random time for on and off and creat a thread as fountains
    for pair in pairs:
        on_time = random.randint(1, 5)
        off_time = random.randint(1, 5)

        threads = []

        for fountain_id in pair:

            thread = threading.Thread(target=control_fountain, args=(fountain_id, on_time, off_time))
            threads.append(thread)
            thread.start()
    
        for thread in threads:
            thread.join()


sequential_fountains()
pairs_fountains()
