from gtts import gTTS
import asyncio

import os

async def trigger_alarm(volume=50):
    alarm_message = "Warning! Fire is detected.q"
    
    tts = gTTS(text=alarm_message, lang='en')

    tts.save('alarm.mp3')

    # Playing the sound (using 'start' command for Windows)
    os.system(f"start alarm.mp3")
    await asyncio.sleep(0.4)


trigger_alarm(volume=50)
