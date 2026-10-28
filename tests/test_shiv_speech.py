import unittest
from unittest.mock import Mock, patch

import shiv_speech


class TestShivSpeech(unittest.TestCase):

    def setUp(self):
        self.original_english_engine = shiv_speech._english_engine
        self.original_hindi_engine = shiv_speech._hindi_engine

        shiv_speech._english_engine = None
        shiv_speech._hindi_engine = None

    def tearDown(self):
        shiv_speech._english_engine = self.original_english_engine
        shiv_speech._hindi_engine = self.original_hindi_engine

    def test_speak_outputs_text(self):
        mock_engine = Mock()

        with patch(
            "shiv_speech.pyttsx3.init",
            return_value=mock_engine,
        ) as mock_init:

            shiv_speech.speak("Hello SHIV")

        mock_init.assert_called_once_with()
        mock_engine.say.assert_called_once_with("Hello SHIV")
        mock_engine.runAndWait.assert_called_once_with()

    def test_engine_is_reused_for_multiple_messages(self):
        mock_engine = Mock()

        with patch(
            "shiv_speech.pyttsx3.init",
            return_value=mock_engine,
        ) as mock_init:

            shiv_speech.speak("First test")
            shiv_speech.speak("Second test")
            shiv_speech.speak("Third test")

        mock_init.assert_called_once_with()
        self.assertEqual(mock_engine.say.call_count, 3)
        self.assertEqual(mock_engine.runAndWait.call_count, 3)

    def test_empty_text_is_ignored(self):
        with patch("shiv_speech.pyttsx3.init") as mock_init:
            shiv_speech.speak("   ")

        mock_init.assert_not_called()

    def test_hindi_text_uses_hindi_engine(self):
        mock_engine = Mock()
        mock_audio = object()
        mock_engine.synthesize.return_value = mock_audio

        with (
            patch(
                "shiv_speech.get_hindi_engine",
                return_value=mock_engine,
            ),
            patch("shiv_speech.sd.play") as mock_play,
            patch("shiv_speech.sd.wait") as mock_wait,
        ):
            shiv_speech.speak("हर हर महादेव।")

        mock_engine.synthesize.assert_called_once_with(
            "हर हर महादेव।",
            voice="male",
            speed=shiv_speech.SPEECH_SPEED,
        )

        mock_play.assert_called_once_with(
            mock_audio,
            samplerate=shiv_speech.SAMPLE_RATE,
        )
        mock_wait.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()