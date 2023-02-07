import os,sys
import tkinter as tk
import tkinter.font as tkfont
import json

# Configuration
args = sys.argv[1:]

save_ids = os.path.exists("save_text.txt")

root = tk.Tk()
root.title("MonikA.I. Submod")
root.geometry("550x300")
#root.resizable(False, False)
root.configure(background='#333333')

def get_input():
    global USERNAME
    global PASSWORD
    global CHOOSE_CHARACTER
    global GAME_PATH
    global USE_CHARACTER_AI
    global USE_TTS
    global DEBUG_MODE
    global CONTINUE_FROM_LAST
    global KEEP_CONFIG
    global USE_CAMERA
    global TIME_INTERVALL
    USERNAME = username.get()
    PASSWORD = password.get()
    CHOOSE_CHARACTER = choose_character.get()
    USE_CHARACTER_AI = use_character_ai.get()
    USE_TTS = use_tts.get()
    GAME_PATH = game_path.get()
    DEBUG_MODE = debug_mode.get()
    CONTINUE_FROM_LAST = continue_from_last.get()
    KEEP_CONFIG = keep_config.get()
    USE_CAMERA = use_camera.get()
    TIME_INTERVALL = time_intervall.get()
    root.destroy()

username = tk.StringVar()
password = tk.StringVar()
choose_character = tk.StringVar()
use_character_ai = tk.StringVar()
use_tts = tk.StringVar()
game_path = tk.StringVar()
debug_mode = tk.StringVar()
continue_from_last = tk.StringVar()
keep_config = tk.StringVar()
use_camera = tk.StringVar()
time_intervall = tk.StringVar()

tk.Label(root, text="Email",bg='#333333',fg='white').grid(row=0, column=0)
tk.Label(root, text="Password",bg='#333333',fg='white').grid(row=1, column=0)
tk.Label(root, text="Game Path",bg='#333333',fg='white').grid(row=2, column=0)
tk.Label(root, text="Choose Character",bg='#333333',fg='white').grid(row=3, column=0)
tk.Label(root, text="Use Character AI",bg='#333333',fg='white').grid(row=5, column=0)
tk.Label(root, text="Use TTS",bg='#333333',fg='white').grid(row=6, column=0)
tk.Label(root, text="Use Debug Mode",bg='#333333',fg='white').grid(row=7, column=0)
tk.Label(root, text="Continue from last chat",bg='#333333',fg='white').grid(row=8, column=0)
tk.Label(root, text="Use Camera",bg='#333333',fg='white').grid(row=9, column=0)
tk.Label(root, text="Time Intervall For Camera",bg='#333333',fg='white').grid(row=9,column=3)

font = tkfont.Font(family="Helvetica", size=12, weight="bold")
#set font to keep config
tk.Label(root, text="Use Saved Config", font=font,bg='#333333',fg='white').grid(row=10, column=0)

tk.Entry(root, textvariable=username,width=25).grid(row=0, column=1)
tk.Entry(root, textvariable=password,show='*',width=25).grid(row=1, column=1)
tk.Entry(root, textvariable=game_path,width=25).grid(row=2, column=1)
# tk.Entry(root, textvariable=choose_character,width=10).grid(row=3, column=1)
#Make scrollable choice for choose_character between 0 and 1
char_menu = tk.OptionMenu(root, choose_character, "0", "1")
char_menu.config( bg='white',fg='black')
char_menu.grid(row=3, column=1)
tk.Entry(root, textvariable=time_intervall,width=10).grid(row=9, column=4)

tk.Radiobutton(root, text="Yes", variable=use_character_ai, value=True,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=5, column=1)
tk.Radiobutton(root, text="No", variable=use_character_ai, value=False,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=5, column=2)

tk.Radiobutton(root, text="Yes", variable=use_tts, value=True,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=6, column=1)
tk.Radiobutton(root, text="No", variable=use_tts, value=False,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=6, column=2)

tk.Radiobutton(root, text="Yes", variable=debug_mode, value=True,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=7, column=1)
tk.Radiobutton(root, text="No", variable=debug_mode, value=False,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=7, column=2)

tk.Radiobutton(root, text="Yes", variable=continue_from_last, value=True,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=8, column=1)
tk.Radiobutton(root, text="No", variable=continue_from_last, value=False,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=8, column=2)

tk.Radiobutton(root, text="Yes", variable=use_camera, value=True,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=9, column=1)
tk.Radiobutton(root, text="No", variable=use_camera, value=False,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=9, column=2)

tk.Radiobutton(root, text="Yes", variable=keep_config, value=True,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=10, column=1)
tk.Radiobutton(root, text="No", variable=keep_config, value=False,bg='#333333',activeforeground='white',fg='white',activebackground="#333333",selectcolor='#333333').grid(row=10, column=2)

#tk.Button(root, text="Submit", command=get_input,bg='#FF3399',fg='white').grid(row=11, column=1)
#center the button
button = tk.Button(root, text="Submit", command=get_input,bg='#FF3399',fg='white')
button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

if save_ids:
    with open("save_text.txt", "r") as f:
        string = f.read()
        GAME_PATH,USERNAME,PASSWORD = string.split(";")

    username.set(USERNAME)
    password.set(PASSWORD)
    game_path.set(GAME_PATH)

# if save_ids:
#     #Make button appear if the previous one was clicked
#     def on_select(v):
#         global GAME_PATH
#         if v == True:            
#             tk.Label(root, text="Change Game Path").grid(row=4, column=0)
#             tk.Entry(root, textvariable=game_path).grid(row=4, column=3)

#             tk.Label(root, text="Change email").grid(row=0, column=0)
#             tk.Entry(root, textvariable=username).grid(row=0, column=3)

#             tk.Label(root, text="Change password").grid(row=1, column=0)
#             tk.Entry(root, textvariable=password,show='*').grid(row=1, column=3)
#         else:
#             with open("save_text.txt", "r") as f:
#                 string = f.read()
#                 GAME_PATH,USERNAME,PASSWORD = string.split(";")
#             #Write GAME_PATH in the box
#             tk.Label(root, text="Change Game Path").grid(row=4, column=0)
#             tk.Entry(root, textvariable=game_path).grid(row=4, column=3)
#             game_path.set(GAME_PATH)

#             tk.Label(root, text="Change email").grid(row=0, column=0)
#             tk.Entry(root, textvariable=username).grid(row=0, column=3)
#             username.set(USERNAME)

#             tk.Label(root, text="Change password").grid(row=1, column=0)
#             tk.Entry(root, textvariable=password,show='*').grid(row=1, column=3)
#             password.set(PASSWORD)

#     tk.Label(root, text="Change Game Path").grid(row=4, column=0)
#     change_game_path = tk.BooleanVar()

#     yes_change = tk.Radiobutton(root, text="Yes", variable=change_game_path, value=True)
#     yes_change.grid(row=4, column=1)
#     yes_change.config(command=lambda: on_select(True))

#     no_change = tk.Radiobutton(root, text="No", variable=change_game_path, value=False)
#     no_change.grid(row=4, column=2)
#     no_change.config(command=lambda: on_select(False))

#     tk.Label(root, text="Change email").grid(row=0, column=0)
#     change_email = tk.BooleanVar()

#     yes_change = tk.Radiobutton(root, text="Yes", variable=change_email, value=True)
#     yes_change.grid(row=0, column=1)
#     yes_change.config(command=lambda: on_select(True))

#     no_change = tk.Radiobutton(root, text="No", variable=change_email, value=False)
#     no_change.grid(row=0, column=2)
#     no_change.config(command=lambda: on_select(False))

#     tk.Label(root, text="Change password").grid(row=1, column=0)
#     change_password = tk.BooleanVar()

#     yes_change = tk.Radiobutton(root, text="Yes", variable=change_password, value=True)
#     yes_change.grid(row=1, column=1)
#     yes_change.config(command=lambda: on_select(True))

#     no_change = tk.Radiobutton(root, text="No", variable=change_password, value=False)
#     no_change.grid(row=1, column=2)
#     no_change.config(command=lambda: on_select(False))

# else:
#     game_path = tk.StringVar()
#     tk.Label(root, text="Game Path").grid(row=4, column=0)
#     tk.Entry(root, textvariable=game_path).grid(row=4, column=1)

#     username = tk.StringVar()
#     tk.Label(root, text="Email").grid(row=0, column=0)
#     tk.Entry(root, textvariable=username).grid(row=0, column=1)

#     password = tk.StringVar()
#     tk.Label(root, text="Password").grid(row=1, column=0)
#     tk.Entry(root, textvariable=password, show='*').grid(row=1, column=1)
    
root.mainloop()

KEEP_CONFIG = int(KEEP_CONFIG)
if KEEP_CONFIG:
    if not os.path.exists("config.json"):
        raise Exception("config.json not found")
    with open("config.json", "r") as f:
        config = json.load(f)
        GAME_PATH = config["GAME_PATH"]
        USERNAME = config["USERNAME"]
        PASSWORD = config["PASSWORD"]
        USE_TTS = config["USE_TTS"]
        USE_CHARACTER_AI = config["USE_CHARACTER_AI"]
        DEBUG_MODE = config["DEBUG_MODE"]
        CONTINUE_FROM_LAST = config["CONTINUE_FROM_LAST"]
        CHOOSE_CHARACTER = config["CHOOSE_CHARACTER"]
        USE_CAMERA = config["USE_CAMERA"]
        TIME_INTERVALL = config["TIME_INTERVALL"]

#Write game_path to a file
if GAME_PATH != "" and USERNAME != "" and PASSWORD != "":
    with open("save_text.txt", "w") as f:
        f.write(GAME_PATH + ";" + USERNAME + ";" + PASSWORD)

USE_TTS = int(USE_TTS)
USE_CHARACTER_AI = int(USE_CHARACTER_AI)
DEBUG_MODE = int(DEBUG_MODE)
CONTINUE_FROM_LAST = int(CONTINUE_FROM_LAST)
USE_CAMERA = int(USE_CAMERA)
TIME_INTERVALL = int(TIME_INTERVALL)

#Save config to a json file
CONFIG = {
    "GAME_PATH": GAME_PATH,
    "USE_TTS": USE_TTS,
    "USE_CHARACTER_AI": USE_CHARACTER_AI,
    "DEBUG_MODE": DEBUG_MODE,
    "CONTINUE_FROM_LAST": CONTINUE_FROM_LAST,
    "USERNAME": USERNAME,
    "PASSWORD": PASSWORD,
    "CHOOSE_CHARACTER": CHOOSE_CHARACTER,
    "USE_CAMERA": USE_CAMERA,
    "TIME_INTERVALL": TIME_INTERVALL
}

with open("config.json", "w") as f:
    json.dump(CONFIG, f)