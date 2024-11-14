from datetime import datetime
import random
import time

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