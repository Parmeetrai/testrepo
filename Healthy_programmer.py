from pip import main
from pygame import mixer
from datetime import datetime
from time import time

def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
        break

def log_now(msg):
    with open("myfile.txt","a") as f:
        f.write(f"{msg} at {datetime.now()}\n")


if __name__ == '__main__':
    init_pani = time()     
    init_exer =  time()
    init_eye = time()
    water_secs = 5
    ex_secs = 10
    eye_secs = 4
while True:

    if time() - init_pani > water_secs:
        print("Drink water and enter drank when done")
        music("water.wav",'drank')
        init_water = time()
        log_now("Drank water at") 

    if time() - init_eye > eye_secs:
        print("Do eye exercise and write eyedone")
        music("water.wav",'eyedone')
        init_eyes = time()
        log_now("Eye exercise done at") 

    if time() - init_exer > ex_secs:
        print("Do exercise and write exdone")
        music("water.wav",'exdone')
        init_ex = time()
        log_now("Exercise done at")            