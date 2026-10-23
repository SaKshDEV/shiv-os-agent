
import unittest

from shiv_brain import normalize_voice_command, process_command


class TestShivBrain(unittest.TestCase):

    def test_hindi_time_command(self):
        result = normalize_voice_command("समय")
        self.assertEqual(result, "time")

    def test_hindi_greeting_command(self):
        result = normalize_voice_command("नमस्ते")
        self.assertEqual(result, "hello")

    def test_forget_name_command(self):
        command = normalize_voice_command("नाम भूल जा")
        result = process_command(command, "Saksham")
        self.assertEqual(result, "FORGET_NAME")

    def test_personalized_greeting(self):
        result = process_command("hello", "Saksham")
        self.assertEqual(result, "Hey Saksham bhai! Kaisa hai?")

    def test_exit_command(self):
        result = process_command("exit", "Saksham")
        self.assertEqual(result, "EXIT")

    def test_unknown_command(self):
        result = process_command("dance", "Saksham")
        self.assertEqual(
            result,
            "Ye command abhi samajh nahi aayi."
        )


if __name__ == "__main__":
    unittest.main()
