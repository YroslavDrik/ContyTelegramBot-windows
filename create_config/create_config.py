import json


def get_create_config():
    #Bot parameters, folder paths, and other settings
    settings = {
        'TOKEN': "" ,
        'SAVE_DIR': "",
        'USER_ID': 0,
        'StickersList': [["Hello" , "CAACAgIAAxkBAAE5bu1om73PcfY--Pe2Iymii-d-CuuNaAACeoEAAve_4EhfQAf-L6BLfDYE"],["?" , "CAACAgIAAxkBAAE5byFom8CYIagxFHNsSsNDuMfdFSyFIQACMH0AAg1S4EgbgDusfNUUuzYE"],
    ]
    }

    answer_dist = {
        'greeting': "Hello {name}! I'm Conty, your PC assistant",
        'screenshot': "Here's your screenshot:",
        'ask_volume_action': "What volume level would you like?",
        'ask_custom_volume': "Please specify the volume percentage:",
        'volume_updated': "Done! The volume has been updated",
        'unknown': "Sorry, I didn't understand. Please use the menu options",
        'file_saved': "Saved and done: {filename}",
        'error_max_size': "⛔ Whoa! That file’s too big. Max is 20 MB",
        'back_home_menu': "Okay, sending you back to the main menu!",
        'no_access': "⛔ You don’t have access to this bot",
        'ask_shutdown_timer': "When should I turn off the PC?",
        'ask_playlist': "Which playlist would you like to play?",
        'shutdown_pc': "Turning off the PC!",
        'set_timer': "Timer Set For: ",
        'ask_music': "What music would you like to listen to?",
        'turning_on': "Turning it on, please wait a second...",
        'ask_would_you_like': "❓ What do you want to do?",
        'okay_doing': "Okay, on it!",
        'timer_disabled': "Timer has been turned off",
        'sleep_mode': "Switching to sleep mode",
        'start_download':"Download is in progress. Please wait...",
        'end_download':"Download is finished: {link}",
        'no_link': "No link was provided. Please send the link",
        'error_download': "ERROR: {error}",
        'close_program': "❌ Closing program, please wait...",
        'get_system_data': "📊 System Information: \nSystem: {system_name}\nRAM: {used_ram} / {total_ram} GB used \nCPU Load: {cpu_usage}% \n"

    }

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump([settings  , answer_dist], file, ensure_ascii=False, indent=4)

    print("Settings saved to config.json")
    return None