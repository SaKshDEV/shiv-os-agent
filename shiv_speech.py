import pyttsx3

_engine = None

def get_engine():
    global _engine

    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty("rate", 165)
        _engine.setProperty("volume", 1.0)

    return _engine

def speak(text):
    text = str(text).strip()

    if not text:
        return

    engine = get_engine()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("mummmy khana de do bhook lag rhi .")
