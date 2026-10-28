import sys
import re
import pyttsx3
import sounddevice as sd
from huggingface_hub import snapshot_download


MODEL_ID = "sulabhkatiyar/indic-tiny-tts-hindi"
SAMPLE_RATE = 24000
SPEECH_SPEED = 0.92

_english_engine = None
_hindi_engine = None


def get_english_engine():
    global _english_engine

    if _english_engine is None:
        _english_engine = pyttsx3.init()
        _english_engine.setProperty("rate", 165)
        _english_engine.setProperty("volume", 1.0)

    return _english_engine


def get_hindi_engine():
    global _hindi_engine

    if _hindi_engine is None:
        print("SHIV: Hindi voice load ho rahi hai...")

        model_dir = str(snapshot_download(MODEL_ID))

        if model_dir not in sys.path:
            sys.path.insert(0, model_dir)

        from indic_tiny_tts import TinyTTS

        _hindi_engine = TinyTTS.from_pretrained(
            MODEL_ID,
            device="cpu",
        )

    return _hindi_engine

def to_hindi_speech_text(message):
    message = str(message).strip()

    hindi_numbers = {
        0: "शून्य", 1: "एक", 2: "दो", 3: "तीन",
        4: "चार", 5: "पाँच", 6: "छह", 7: "सात",
        8: "आठ", 9: "नौ", 10: "दस", 11: "ग्यारह",
        12: "बारह", 13: "तेरह", 14: "चौदह",
        15: "पंद्रह", 16: "सोलह", 17: "सत्रह",
        18: "अठारह", 19: "उन्नीस", 20: "बीस",
        21: "इक्कीस", 22: "बाईस", 23: "तेईस",
        24: "चौबीस", 25: "पच्चीस", 26: "छब्बीस",
        27: "सत्ताईस", 28: "अट्ठाईस", 29: "उनतीस",
        30: "तीस", 31: "इकतीस", 32: "बत्तीस",
        33: "तैंतीस", 34: "चौंतीस", 35: "पैंतीस",
        36: "छत्तीस", 37: "सैंतीस", 38: "अड़तीस",
        39: "उनतालीस", 40: "चालीस", 41: "इकतालीस",
        42: "बयालीस", 43: "तैंतालीस", 44: "चवालीस",
        45: "पैंतालीस", 46: "छियालीस", 47: "सैंतालीस",
        48: "अड़तालीस", 49: "उनचास", 50: "पचास",
        51: "इक्यावन", 52: "बावन", 53: "तिरपन",
        54: "चौवन", 55: "पचपन", 56: "छप्पन",
        57: "सत्तावन", 58: "अट्ठावन", 59: "उनसठ",
    }

    def spoken_name(name):
        known_names = {
            "saksham": "सक्षम",
        }
        return known_names.get(name.lower(), name)

    fixed_replies = {
        "Tera naam kya hai bhai?":
            "तुम्हारा नाम क्या है, भाई?",
        "Naya naam kya rakhu bhai?":
            "तुम्हारा नया नाम क्या रखूँ, भाई?",
        "Ye command abhi samajh nahi aayi.":
            "यह कमांड अभी समझ नहीं आई।",
        "Notepad open ho gaya!":
            "नोटपैड खुल गया है।",
        "Calculator open ho gaya!":
            "कैलकुलेटर खुल गया है।",
        "Naam khali nahi ho sakta.":
            "नाम खाली नहीं हो सकता।",
        "Theek hai bhai, milte hain phir!":
            "ठीक है भाई, फिर मिलेंगे।",
        "Har Har Mahadev!":
            "हर हर महादेव।",
    }

    time_match = re.search(
        r"Abhi time hai\s+(\d{1,2}):(\d{2})"
        r"(?::\d{2})?\s*(AM|PM)",
        message,
        re.IGNORECASE,
    )

    if time_match:
        hour = int(time_match.group(1)) % 12
        minute = int(time_match.group(2))
        period = time_match.group(3).upper()

        hour = hour or 12

        if period == "AM":
            day_period = "रात" if hour < 5 or hour == 12 else "सुबह"
        elif hour == 12:
            day_period = "दोपहर"
        elif hour < 5:
            day_period = "दोपहर"
        elif hour < 8:
            day_period = "शाम"
        else:
            day_period = "रात"

        hour_word = hindi_numbers[hour]

        if minute == 0:
            return f"अभी {day_period} के {hour_word} बजे हैं।"

        minute_word = hindi_numbers[minute]

        return (
            f"अभी {day_period} के {hour_word} बजकर "
            f"{minute_word} मिनट हुए हैं।"
        )

    if message.startswith("Har Har Mahadev,"):
        name = message[len("Har Har Mahadev,"):].strip().rstrip("!")

        if name:
            return f"हर हर महादेव, {spoken_name(name)}। तुम्हारा स्वागत है।"

        return "हर हर महादेव। तुम्हारा स्वागत है।"

    greeting_match = re.fullmatch(
        r"Hey (.+?) bhai! Kaisa hai\?",
        message,
        re.IGNORECASE,
    )

    if greeting_match:
        name = spoken_name(greeting_match.group(1).strip())
        return f"अरे {name} भाई, कैसे हो?"

    if message.startswith("Samajh gaya bhai"):
        return "समझ गया भाई। अब तुम्हें नए नाम से बुलाऊँगा।"

    return fixed_replies.get(message, message)

def speak(text):
    text = str(text).strip()

    if not text:
        return

    has_hindi = any(
        "\u0900" <= character <= "\u097F"
        for character in text
    )

    if has_hindi:
        engine = get_hindi_engine()
        audio = engine.synthesize(
            text,
            voice="male",
            speed=SPEECH_SPEED,
        )

        sd.play(audio, samplerate=SAMPLE_RATE)
        sd.wait()

    else:
        engine = get_english_engine()
        engine.say(text)
        engine.runAndWait()


if __name__ == "__main__":
    speak("हर हर महादेव। मैं शिव हूँ।")
    speak("Your personal AI companion.")