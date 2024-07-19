#!usr/bin/env python

# pip install pynput
# pip install keyboard
# time and threading should be included
# with python


# import the libs
import time, threading, keyboard as kb
from pynput.mouse import Controller, Button, Listener
from pynput.keyboard import Listener, KeyCode

# set all variables
mouse = Controller()

TOGGLE_KEY_L = KeyCode(char="[")
TOGGLE_KEY_R = KeyCode(char="]")
TOGGLE_KEY_D = KeyCode(char="\\")
TOGGLE_KEY_S = KeyCode(char="=")
TOGGLE_KEY_T = KeyCode(char=".")
TOGGLE_KEY_CUSTOM = KeyCode(char="-")

FAILSAFE_KEY = "Key.media_volume_mute"

Failsafe_active = False

RMB_clicker = LMB_clicker = scroll_active = custom = False
burst_click = 0

while True:
    print("All delays measured in seconds")
    x = input(f"Autoclicker delay -  LMB {TOGGLE_KEY_L} : RMB {TOGGLE_KEY_R}:      ")
    click = int(input(f"# of burst clicks (when you click {TOGGLE_KEY_D}):      "))
    x2 = input(f"Burst delay:      ")
    x3 = int(input(f"Mouse scroll Lines  (when you click {TOGGLE_KEY_S}):      "))
    write_message = input(f"Type Message (when you click {TOGGLE_KEY_T})")
    try: x = float(x); x2 = float(x2)
    except: print("Invalid")
    else: d = x; break

key = input(f"Key:      ")

def Autoclicker():
    global burst_click
    while True:
        if not Failsafe_active:
            if RMB_clicker: 
                mouse.click(Button.right, 1); time.sleep(d)
            elif LMB_clicker: 
                mouse.click(Button.left, 1); time.sleep(d)
            elif int(burst_click):
                mouse.click(Button.right, 1)
                time.sleep(x2)
                burst_click -= 1
            elif scroll_active:
                mouse.scroll(0, x3)
                time.sleep(0.25)
            elif custom:
                # mouse.click(Button.right, 1); time.sleep(d)
                pass
            else: time.sleep(1)
        else: time.sleep(1)


def toggle(key):
    global RMB_clicker, LMB_clicker, burst_click, Failsafe_active, scroll_active, custom
    if str(key) == FAILSAFE_KEY:
        burst_click = 0; RMB_clicker = LMB_clicker = scroll_active = False; Failsafe_active = not Failsafe_active; print("\033c", f"LIVE: {not Failsafe_active}   DELAY: {d}   ACTIVE: {bool(RMB_clicker or LMB_clicker) and not Failsafe_active} -> L:{LMB_clicker}   R:{RMB_clicker}   C:{burst_click}   scroll_active:{scroll_active}")
    elif key == TOGGLE_KEY_R:
        RMB_clicker = not RMB_clicker; print("\033c", f"LIVE: {not Failsafe_active}   DELAY: {d} : {x2}   ACTIVE: {bool(RMB_clicker or LMB_clicker) and not Failsafe_active} -> L:{LMB_clicker}   R:{RMB_clicker}   C:{burst_click}   scroll_active:{scroll_active}")
    elif key == TOGGLE_KEY_L:
        LMB_clicker = not LMB_clicker; print("\033c", f"LIVE: {not Failsafe_active}   DELAY: {d} : {x2}   ACTIVE: {bool(RMB_clicker or LMB_clicker) and not Failsafe_active} -> L:{LMB_clicker}   R:{RMB_clicker}   C:{burst_click}   scroll_active:{scroll_active}")
    elif key == TOGGLE_KEY_D:
        burst_click = click; print("\033c", f"LIVE: {not Failsafe_active}   DELAY: {d} : {x2}   ACTIVE: {bool(RMB_clicker or LMB_clicker) and not Failsafe_active} -> L:{LMB_clicker}   R:{RMB_clicker}   C:{burst_click}   scroll_active:{scroll_active}")
    elif key == TOGGLE_KEY_CUSTOM:
        custom = not custom; print("\033c", f"LIVE: {not Failsafe_active}   DELAY: {d} : {x2}   ACTIVE: {bool(RMB_clicker or LMB_clicker) and not Failsafe_active} -> L:{LMB_clicker}   R:{RMB_clicker}   C:{burst_click}   scroll_active:{scroll_active}")
    elif key == TOGGLE_KEY_S:
        scroll_active = not scroll_active; print("\033c", f"LIVE: {not Failsafe_active}   DELAY: {d} : {x2}   ACTIVE: {bool(RMB_clicker or LMB_clicker) and not Failsafe_active} -> L:{LMB_clicker}   R:{RMB_clicker}   C:{burst_click}   scroll_active:{scroll_active}")
    elif key == TOGGLE_KEY_T and not Failsafe_active:
        kb.write(f"{write_message}"); kb.press("Enter")

click_thread = threading.Thread(target=Autoclicker).start()
with Listener(on_press=toggle) as keyboard_listener:
    keyboard_listener.join()
