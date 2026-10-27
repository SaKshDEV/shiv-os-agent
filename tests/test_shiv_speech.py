import unittest
from unittest.mock import Mock, patch

import shiv_speech


class TestShivSpeech(unittest.TestCase):

    def setUp(self):
        self.original_engine = shiv_speech._engine
        shiv_speech._engine = None

    def tearDown(self):
        shiv_speech._engine = self.original_engine

    @patch("shiv_speech.pyttsx3.init")
    def test_speak_outputs_text(self, mock_init):
        mock_engine = Mock()
        mock_init.return_value = mock_engine

        shiv_speech.speak("Hello SHIV")

        mock_init.assert_called_once_with()
        mock_engine.say.assert_called_once_with("Hello SHIV")
        mock_engine.runAndWait.assert_called_once_with()

    @patch("shiv_speech.pyttsx3.init")
    def test_engine_is_reused_for_multiple_messages(self, mock_init):
        mock_engine = Mock()
        mock_init.return_value = mock_engine

        shiv_speech.speak("First test")
        shiv_speech.speak("Second test")
        shiv_speech.speak("Third test")

        mock_init.assert_called_once_with()
        self.assertEqual(mock_engine.say.call_count, 3)
        self.assertEqual(mock_engine.runAndWait.call_count, 3)

    @patch("shiv_speech.pyttsx3.init")
    def test_empty_text_is_ignored(self, mock_init):
        shiv_speech.speak("   ")

        mock_init.assert_not_called()


if __name__ == "__main__":
    unittest.main()