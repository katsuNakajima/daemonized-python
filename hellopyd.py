#!/usr/bin/python3
import time
def main():
    filepath = "/tmp/hello.log"
    log = open(filepath,'a')
    log.write("hello!\n")

if __name__ == '__main__':
    while True:
        main()
        time.sleep(30)
