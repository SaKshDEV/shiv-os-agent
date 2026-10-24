import json
from pathlib import Path

import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = (
    Path(__file__).parent
    / "models"
    / "vosk-model-small-hi-0.22"
)

SAMPLE_RATE = 16000
RECORD_SECONDS = 5

_model = None

def get_model():
    global _model

    if _model is None:
        print("SHIV: Spech model load ho raha hai...")
        _model = Model(str(MODEL_PATH))

    return _model    


def listen_once():
    if not MODEL_PATH.is_dir():
        raise FileNotFoundError(
            f"Speech model folder not found: {MODEL_PATH}"
        )

    print("SHIV: Speech model load ho raha hai...")
    model = get_model()
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    print("SHIV: Ab 5 seconds tak clearly bolo!")
    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    has_result = recognizer.AcceptWaveform(audio.tobytes())

    if has_result:
        result = json.loads(recognizer.Result())
    else:
        result = json.loads(recognizer.FinalResult())

    return result.get("text", "").strip()


if __name__ == "__main__":
    recognized_text = listen_once()

    if recognized_text:
        print(f"SHIV heard: {recognized_text}")
    else:
        print("SHIV: Speech recognize nahi hui. Dobara try kar.")

     