import sys
from pathlib import Path

from huggingface_hub import snapshot_download

MODEL_ID = "sulabhkatiyar/indic-tiny-tts-hindi"

print("SHIV: Hindi voice model download ho raha hai...")

model_dir = snapshot_download(MODEL_ID)
sys.path.insert(0, model_dir)

from indic_tiny_tts import TinyTTS

print("SHIV: Voice model load ho raha hai...")

tts = TinyTTS.from_pretrained(MODEL_ID, device="cpu")

text = (
    "हर हर महादेव। "
    "वत्स, अपने मन को शांत रखो। "
    "धैर्य और करुणा के साथ आगे बढ़ो। "
    "मैं तुम्हारी सहायता के लिए यहाँ हूँ।"
)

print("SHIV: Hindi speech generate ho rahi hai...")

audio = tts.synthesize(text, voice="male", speed=0.92)
output_file = Path(__file__).with_name("shiv_hindi_test.wav")
tts.save_wav(audio, str(output_file))

print(f"SHIV: Audio save ho gaya: {output_file}")