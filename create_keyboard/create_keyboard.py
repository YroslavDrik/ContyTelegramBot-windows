from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_main():
    keyboard_main = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⏯️ Playback Control")],
            [KeyboardButton(text="🖼 Take Screenshot")] ,
            [KeyboardButton(text="🔊 Change Volume")],
            [KeyboardButton(text="🌙 Sleep Mode")],
            [KeyboardButton(text="😃 Tell a Joke")],
            [KeyboardButton(text="⏱ Set Timer for Shutdown")],
            [KeyboardButton(text="🔌 Shut Down")],
            [KeyboardButton(text="🖥️ Get System Data")],
            [KeyboardButton(text="❌ ALT + F4")],

        ],
        resize_keyboard=True)
    return keyboard_main


def get_keyboard_change_volume():
    keyboard_change_volume = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔉 Set Custom Volume"),
                KeyboardButton(text="🔊 Set Max Volume"),
                KeyboardButton(text="🔈 Set Mute"),
                KeyboardButton(text="↩️ Back to Home"),
            ],
        ],
        resize_keyboard=True
    )
    return keyboard_change_volume

def get_keyboard_change_volume_custom():
    keyboard_change_volume_custom = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🔈 0%")], [KeyboardButton(text="🔉 10%")], [KeyboardButton(text="🔉 20%")],
                  [KeyboardButton(text="🔉 30%")], [KeyboardButton(text="🔉 40%")], [KeyboardButton(text="🔊 50%")],
                  [KeyboardButton(text="🔊 60%")], [KeyboardButton(text="🔊 70%")], [KeyboardButton(text="🔊 80%")],
                  [KeyboardButton(text="🔊 90%")], [KeyboardButton(text="🔊 100%")],
                  [KeyboardButton(text="↩️ Back to Home")], ],
        resize_keyboard=True
    )
    return keyboard_change_volume_custom

def get_keyboard_playback_control():
    keyboard_playback_control = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="⏮️"),
                KeyboardButton(text="▶️"),
                KeyboardButton(text="⏭️")
            ],
            [
                KeyboardButton(text="↩️ Back to Home")
            ]
        ],
        resize_keyboard=True
    )
    return keyboard_playback_control

def get_keyboard_ask_shutdown_timer():
    keyboard_ask_shutdown_timer = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⏱ 15 Min")],
            [KeyboardButton(text="⏱ 30 Min")],
            [KeyboardButton(text="⏱ 45 Min")],
            [KeyboardButton(text="⏱ 1 Hour")],
            [KeyboardButton(text="⏱ 2 Hours")],
            [KeyboardButton(text="⏱ 3 Hours")],
            [KeyboardButton(text="⏱ 4 Hours")],
            [KeyboardButton(text="⏱ 5 Hours")],
            [KeyboardButton(text="⏱ 6 Hours")],
            [KeyboardButton(text="⏱ 7 Hours")],
            [KeyboardButton(text="⏱ Cancel Shutdown Timer")],
            [KeyboardButton(text="↩️ Back to Home")],
        ],
        resize_keyboard=True
    )
    return keyboard_ask_shutdown_timer

