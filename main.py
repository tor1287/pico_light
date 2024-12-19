import light_button as light_but
import time

def main():
    while True:
        light_but.light_red()
        time.sleep(1)
        light_but.light_green()
        time.sleep(1)
        light_but.light_blue()
        time.sleep(1)

if __name__ == "__main__":
    main()