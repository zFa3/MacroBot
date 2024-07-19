import pynput.keyboard, time

def eval_k(key):
    global toggle, keys, lastKey
    if str(key) == "Key.media_volume_mute":
        toggle = not toggle
        print("\033c", f"LIVE: {toggle}")
    if toggle:
        try:
            pressedKey = str(key.char)
        except:
            pressedKey = str(key)
        try:
            keys[str(pressedKey)] += 1
            if not str(pressedKey) == lastKey:
                doubled_keys[str(pressedKey)] += 1
                lastKey = pressedKey
        except: pass
        with open("keystrokes.txt", "a+", encoding="utf-8") as file:
            file.write(f"\n{pressedKey}")
    else:
        try:
            with open('keys.txt', 'w') as file:
                for i, t, in enumerate(keys):
                    file.write(f"{t} : count - {keys[t]}\n")
                    #print(f"{t} : count - {keys[t]}\n")
            with open('Doubled_keys.txt', 'w') as file:
                for i, t, in enumerate(keys):
                    file.write(f"{t} : count - {doubled_keys[t]}\n")
                    #print(f"{t} : count - {keys[t]}\n")
        except: print("Error Accessing File")
def start():
    global keys, toggle, doubled_keys, lastKey
    toggle = True
    lastKey = " "
    keys = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0,
            '1':0,
            '2':0,
            '3':0,
            '4':0,
            '5':0,
            '6':0,
            '7':0,
            '8':0,
            '9':0,
            '0':0,
            '-':0,
            '=':0,
            '[':0,
            ']':0,
            ';':0,
            "'":0,
            '.':0,
            '/':0,
            ',':0,
            '_':0,
            '+':0,
            '{':0,
            '}':0,
            ':':0,
            '"':0,
            "Key.tab":0,
            "Key.caps_lock":0,
            "Key.shift":0,
            "Key.ctrl_l":0,
            "Key.cmd":0,
            "Key.cmd":0,
            "Key.alt_l":0,
            "Key.alt_gr":0,
            "Key.ctrl_r":0,
            "Key.down":0,
            "Key.left":0,
            "Key.up":0,
            "Key.right":0,
            "Key.down":0,
            "Key.shift_r":0,
            "Key.enter":0,
            "Key.space":0,
            "Key.backspace":0,
            "Key.esc":0
    }
    doubled_keys = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0,
            '1':0,
            '2':0,
            '3':0,
            '4':0,
            '5':0,
            '6':0,
            '7':0,
            '8':0,
            '9':0,
            '0':0,
            '-':0,
            '=':0,
            '[':0,
            ']':0,
            ';':0,
            "'":0,
            '.':0,
            '/':0,
            ',':0,
            '_':0,
            '+':0,
            '{':0,
            '}':0,
            ':':0,
            '"':0,
            "Key.tab":0,
            "Key.caps_lock":0,
            "Key.shift":0,
            "Key.ctrl_l":0,
            "Key.cmd":0,
            "Key.cmd":0,
            "Key.alt_l":0,
            "Key.alt_gr":0,
            "Key.ctrl_r":0,
            "Key.down":0,
            "Key.left":0,
            "Key.up":0,
            "Key.right":0,
            "Key.down":0,
            "Key.shift_r":0,
            "Key.enter":0,
            "Key.space":0,
            "Key.backspace":0,
            "Key.esc":0
    }
    keyboard_listener = pynput.keyboard.Listener(on_press=eval_k)
    with keyboard_listener:
        keyboard_listener.join()
start()