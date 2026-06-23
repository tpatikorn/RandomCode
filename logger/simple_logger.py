import os
import datetime

filename = f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log"

if not os.path.exists(filename):
    pass

with open(filename, "w+", encoding="utf8") as log:
    while True:
        text = input("next item: ")
        if text == ":q":
            log.write(f"[{datetime.datetime.now()}] {text}\n")
            break
        log.write(f"[{datetime.datetime.now()}] {text}\n")
