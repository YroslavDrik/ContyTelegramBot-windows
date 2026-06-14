import asyncio

import pyautogui
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message
from pyautogui import screenshot
from aiogram import Bot, Dispatcher, types, F
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import os
import random
import re
import ctypes
import create_keyboard
import keyboard
import json
import create_config
import data_system

try:
    with open("config.json", "r", encoding="utf-8") as file:
        config_data = json.load(file)
except FileNotFoundError:
    create_config.get_create_config()
    with open("config.json", "r", encoding="utf-8") as file:
        config_data = json.load(file)

settings = config_data[0]
answer_dist = config_data[1]

TOKEN = settings["TOKEN"]
SAVE_DIR = settings["SAVE_DIR"]
ALLOWED_USER_IDS = {settings["USER_ID"]}

MAX_FILE_SIZE = 20 * 1024 * 1024

list_stickers = settings['StickersList']

list_volume = [
        "🔈 0%", "🔉 10%", "🔉 20%", "🔉 30%", "🔉 40%",
        "🔊 50%", "🔊 60%", "🔊 70%", "🔊 80%", "🔊 90%", "🔊 100%"
    ]
list_timers = [
        "⏱ 15 Min", "⏱ 30 Min", "⏱ 45 Min", "⏱ 1 Hour", "⏱ 2 Hours",
        "⏱ 3 Hours", "⏱ 4 Hours", "⏱ 5 Hours", "⏱ 6 Hours", "⏱ 7 Hours"
    ]


dp = Dispatcher()
bot = Bot(token=TOKEN)

keyboard_main = create_keyboard.get_keyboard_main()

keyboard_change_volume = create_keyboard.get_keyboard_change_volume()

keyboard_change_volume_custom = create_keyboard.get_keyboard_change_volume_custom()

keyboard_playback_control = create_keyboard.get_keyboard_playback_control()

keyboard_ask_shutdown_timer = create_keyboard.get_keyboard_ask_shutdown_timer()

class AllowedUsersFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ALLOWED_USER_IDS


@dp.message(CommandStart(), AllowedUsersFilter())
async def command_start_handler(message: types.Message) -> None:
    name = message.from_user.full_name
    await message.answer_sticker(list_stickers[0][1])
    await message.answer(answer_dist['greeting'].format(name=name), reply_markup=keyboard_main)


@dp.message(AllowedUsersFilter(), F.document | F.photo | F.video | F.audio | F.voice)
async def handle_any_file(message: types.Message):
    file_id = None
    filename = None
    file_size = None
    subdir = None

    if message.photo:
        file_id = message.photo[-1].file_id
        filename = f"{message.from_user.id}_{message.message_id}.jpg"
        file_size = message.photo[-1].file_size
        subdir = "Pictures"
    elif message.document:
        file_id = message.document.file_id
        filename = message.document.file_name
        file_size = message.document.file_size
        mime_type = message.document.mime_type
        if mime_type.startswith("video/"):
            subdir = "Videos"
        elif mime_type.startswith("image/"):
            subdir = "Pictures"
        elif mime_type.startswith("audio/"):
            subdir = "Music"
        else:
            subdir = "Documents"
    elif message.video:
        file_id = message.video.file_id
        filename = f"{message.from_user.id}_{message.message_id}.mp4"
        file_size = message.video.file_size
        subdir = "Videos"
    elif message.audio:
        file_id = message.audio.file_id
        filename = f"{message.from_user.id}_{message.message_id}.mp3"
        file_size = message.audio.file_size
        subdir = "Music"
    elif message.voice:
        file_id = message.voice.file_id
        filename = f"{message.from_user.id}_{message.message_id}.ogg"
        file_size = message.voice.file_size
        subdir = "Voice"

    if file_size and file_size > MAX_FILE_SIZE:
        await message.reply(answer_dist["error_max_size"])
        return

    if file_id and filename:
        file = await bot.get_file(file_id)
        file_path = file.file_path
        save_path = os.path.join(SAVE_DIR, subdir)
        os.makedirs(save_path, exist_ok=True)
        destination = os.path.join(save_path, filename)
        await bot.download_file(file_path, destination)
        await message.reply(answer_dist['file_saved'].format(filename=filename))

@dp.message(AllowedUsersFilter())
async def handle_buttons(message: types.Message):
    if message.text == "🖼 Take Screenshot":
        screenshot = pyautogui.screenshot()
        screenshot_path = "images/screenshot.png"
        screenshot.save(screenshot_path)
        await message.answer_photo(photo=types.FSInputFile(screenshot_path), caption=answer_dist["screenshot"])
    elif message.text == "❌ ALT + F4":
        keyboard.press_and_release("Alt+F4")
        await message.answer(answer_dist["close_program"])
    elif message.text == "🔌 Shut Down":
        await message.answer(answer_dist["shutdown_pc"])
        os.system("shutdown /s /t 0")

    elif message.text == "⏱ Set Timer for Shutdown":
        await message.answer(answer_dist["ask_custom_volume"], reply_markup=keyboard_ask_shutdown_timer)

    elif message.text == "🖥️ Get System Data":
        (system_name, used_ram, total_ram, cpu_usage, disk_usage) = data_system.get_system_data()
        data_system.record_data()
        disk_str = ""
        for disk in disk_usage:
            disk_str += f"Disk name: {disk[3][:-1]} {disk[1]} / {disk[2]} GB\n"
        await message.answer(answer_dist["get_system_data"].format(system_name = system_name, used_ram = used_ram , total_ram = total_ram , cpu_usage = cpu_usage , ) + disk_str)

    elif message.text == "🌙 Sleep Mode":
        await message.answer(answer_dist["sleep_mode"], reply_markup=keyboard_main)
        ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
    elif message.text in list_timers:
        text = message.text
        numbers = int(re.sub(r'\D', '', text))
        if numbers > 10:
            delay = numbers * 60
            os.system(f"shutdown /s /t {delay}")
        else:
            delay = numbers * 3600
            os.system(f"shutdown /s /t {delay}")
        await message.answer(answer_dist["set_timer"] + str(message.text), reply_markup=keyboard_main)

    elif message.text == "⏱ Cancel Shutdown Timer":
        os.system("shutdown -a")
        await message.answer(answer_dist['okay_doing'], reply_markup=keyboard_main)

    elif message.text == "⏯️ Playback Control":
        await message.answer(answer_dist["ask_would_you_like"], reply_markup=keyboard_playback_control)

    elif message.text == "▶️":
        keyboard.press_and_release('play/pause media')
    elif message.text == "⏭️":
        keyboard.press_and_release('next track')

    elif message.text == "⏮️":
        keyboard.press_and_release('previous track')

    elif message.text == "🔊Change Volume":
        await message.answer(answer_dist["ask_custom_volume"], reply_markup=keyboard_change_volume)

    elif message.text == "↩️ Back to Home":
        await message.answer(answer_dist['back_home_menu'], reply_markup=keyboard_main)

    elif message.text == "🔉 Set Custom Volume":
        await message.answer(answer_dist["ask_custom_volume"], reply_markup=keyboard_change_volume_custom)

    elif message.text == "🔊 Set Max Volume":
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(1, None)
        await message.answer(answer_dist["volume_updated"], reply_markup=keyboard_main)

    elif message.text == "🔈 Set Mute":
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(0, None)
        await message.answer(answer_dist["volume_updated"], reply_markup=keyboard_main)

    elif message.text in list_volume:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volumeInt = int(message.text.split()[1][:-1]) / 100
        volume.SetMasterVolumeLevelScalar(volumeInt, None)
        await message.answer(answer_dist["volume_updated"], reply_markup=keyboard_main)

    else:
        result = random.choice([True, False])
        if result:
            await message.answer_sticker(list_stickers[1][1])
        else:
            await message.answer(answer_dist["unknown"])


@dp.message()
async def handle_not_allowed(message: types.Message):
    if message.from_user.id not in ALLOWED_USER_IDS:
        await message.answer(answer_dist["no_access"])


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
