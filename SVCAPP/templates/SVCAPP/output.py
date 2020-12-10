import os
import time



def update():
    while True:
        file = open("output.html", "w")
 
        # Running the aforementioned command and saving its output
        output = os.popen('wmic process get description, processid').read()

        file.write(output)
        file.close()
        time.sleep(10)

update()