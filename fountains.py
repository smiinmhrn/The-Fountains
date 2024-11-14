from datetime import datetime
import random
import time
import threading

# control the time of being on and off 
def control_fountain(fountain_id):

    # fountain start in current time and print the giving format
    start_time = datetime.now().strftime("%H:%M:%S")
    print(f"Fountain {fountain_id} started in : {start_time}")

    # calculate the time of being on randomly from 1 to 5 secend and sleep the time
    on_time = random.randint(1, 5)
    time.sleep(on_time)

    # fountain end in current time and print the giving format
    end_time = datetime.now().strftime("%H:%M:%S")
    print(f"Fountain {fountain_id} started in : {end_time}")

    # calculate the time of being off randomly from 1 to 5 secend and sleep the time
    off_time = random.randint(1, 5)
    time.sleep(off_time)

def sequential_fountains():
    print("[ Sequential Fountains ]")
    
    # creat 3 treads as fountains and in each treads run the control_fountain fonction and give the fountain id as args
    fountain1 = threading.Thread(target=control_fountain, args=(1,))
    fountain2 = threading.Thread(target=control_fountain, args=(2,))
    fountain3 = threading.Thread(target=control_fountain, args=(3,))

    # fountain[n].start start the fountain and fountain[n].join() make sure that the first thread do the job and finish and then run the other line
    fountain1.start()
    fountain1.join()  
    fountain2.start()
    fountain2.join()  
    fountain3.start()
    fountain3.join()

sequential_fountains()