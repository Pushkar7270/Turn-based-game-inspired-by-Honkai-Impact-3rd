import time


def print_slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()
