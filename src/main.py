import time 
from faker import Faker
fake = Faker()

welcome = "welcome to my typing game also called typer!\nLets test your typing speed\n--------------------------\n"
for w in welcome:
    print(w,end="",flush=True)
    time.sleep(0.1)
t = True
while t:
    start = "Type these sentences as fast as you can with accuracy\nRemeber that all sentences are case sensitive\nPress start when you are ready\n--------------------------\n"
    for s in start:
        print(s,end="",flush=True)
        time.sleep(0.1)
    start1 = input("---").strip().lower()
    if "start" in start1:
        sentence = fake.text(max_nb_chars=200)+"\n"
        for x in sentence:
            print(x,end="",flush=True)
            time.sleep(0.1)

        start_time = time.time()
        user_input=input("")
        end_time = time.time()
        accuracy = 0
        for u,x  in zip(sentence,user_input):
            if u == x:
                accuracy += 1
        a_accuracy =round( accuracy/len(sentence)*100,2)                     
                
                
        
        words = len(sentence.split(" "))
        total_time = end_time - start_time
    

        m = ""
        for s,u in zip(sentence,user_input):
            if s == u:
                m += s
            else:
                m += f"\033[91m{s}\033[0m"

        n = f"What you have to type:\n{sentence}\n"
        for l in n:
            print(l ,end = "",flush = True)
            time.sleep(0.1)

        nm = f"What you have typed:\n{m}\n"
        for lm in nm:
            print(lm ,end = "",flush = True)
            time.sleep(0.1)
        
        print(f"Your word per minute is --\n{round(words / total_time*60,2)}")
        print(f"Your accuracy is --\n{a_accuracy}%")
        l = True
        while l :
            retry = input("Want to test again? (yes/no)  ").strip().lower()
            if "no" in retry:
                l = False
                t = False
            if "yes" in retry:
                l = False
            if "yes" not in retry and "no" not in retry or "yes" in retry and "no" in retry:
                print("Broo type a valid input")    
    elif "end" in start1:
        p="Bye then."
        for i in p:
            print(i,end="",flush=True)
            time.sleep(0.1)
            t = False
    else:
        pr = "Type end to stop and start to start \n"
        for i in pr:
            print(i,end="",flush=True)
            time.sleep(0.1)
            