
import unittest
from unittest.mock import Mock, patch

import shiv_voice


class TestShivVoice(unittest.TestCase):

    def test_recognized_text_is_returned(self):
        fake_audio = Mock()
        fake_audio.tobytes.return_value = b"fake audio"

        fake_recognizer = Mock()
        fake_recognizer.AcceptWaveform.return_value = True
        fake_recognizer.Result.return_value = (
            '{"text": "namaste shiv"}'
        )

        with (
            patch("shiv_voice.MODEL_PATH") as model_path,
            patch("shiv_voice.get_model", return_value=object()),
            patch(
                "shiv_voice.KaldiRecognizer",
                return_value=fake_recognizer
            ),
            patch(
                "shiv_voice.sd.rec",
                return_value=fake_audio
            ),
            patch("shiv_voice.sd.wait"),
        ):
            model_path.is_dir.return_value = True

            result = shiv_voice.listen_once()

        self.assertEqual(result, "namaste shiv")

    def test_final_result_is_used_when_needed(self):
        fake_audio = Mock()
        fake_audio.tobytes.return_value = b"fake audio"

        fake_recognizer = Mock()
        fake_recognizer.AcceptWaveform.return_value = False
        fake_recognizer.FinalResult.return_value = (
            '{"text": "samay"}'
        )

        with (
            patch("shiv_voice.MODEL_PATH") as model_path,
            patch("shiv_voice.get_model", return_value=object()),
            patch(
                "shiv_voice.KaldiRecognizer",
                return_value=fake_recognizer
            ),
            patch(
                "shiv_voice.sd.rec",
                return_value=fake_audio
            ),
            patch("shiv_voice.sd.wait"),
        ):
            model_path.is_dir.return_value = True

            result = shiv_voice.listen_once()

        self.assertEqual(result, "samay")

    def test_empty_speech_returns_empty_text(self):
        fake_audio = Mock()
        fake_audio.tobytes.return_value = b"fake audio"

        fake_recognizer = Mock()
        fake_recognizer.AcceptWaveform.return_value = True
        fake_recognizer.Result.return_value = '{"text": ""}'

        with (
            patch("shiv_voice.MODEL_PATH") as model_path,
            patch("shiv_voice.get_model", return_value=object()),
            patch(
                "shiv_voice.KaldiRecognizer",
                return_value=fake_recognizer
            ),
            patch(
                "shiv_voice.sd.rec",
                return_value=fake_audio
            ),
            patch("shiv_voice.sd.wait"),
        ):
            model_path.is_dir.return_value = True

            result = shiv_voice.listen_once()

        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
