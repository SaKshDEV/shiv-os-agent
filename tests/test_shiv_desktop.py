import unittest
from unittest.mock import patch

from shiv_desktop import open_application

class TestShivDesktop(unittest.TestCase):

    @patch("shiv_desktop.subprocess.Popen")
    def test_open_notepad(self,mock_popen):
        success,message = open_application("notepad")

        self.assertTrue(success)
        self.assertEqual(message,"Notepad open ho gaya!")
        mock_popen.assert_called_once_with(["notepad.exe"])

    @patch("shiv_desktop.subprocess.Popen")
    def test_open_calculator(self, mock_popen):
        success, message = open_application("calculator")

        self.assertTrue(success)
        self.assertEqual(message, "Calculator open ho gaya!")
        mock_popen.assert_called_once_with(["calc.exe"])

    @patch("shiv_desktop.subprocess.Popen")
    def test_unknown_app_is_is_rejected(self, mock_popen):
        success, message = open_application("unknown_app")

        self.assertFalse(success)
        self.assertIn("approved applications", message)
        mock_popen.assert_not_called()

    @patch("shiv_desktop.subprocess.Popen")
    def test_app_name_is_normalized(self, mock_popen):
        success, message = open_application("  NOTEPAD  ")

        self.assertTrue(success)
        mock_popen.assert_called_once_with(["notepad.exe"])

    @patch(
        "shiv_desktop.subprocess.Popen",
        side_effect=OSError("Application launch failed")
    )
    def test_launch_error_is_handled(self, mock_popen):
        success, message = open_application("notepad")

        self.assertFalse(success)
        self.assertEqual(message, "notepad open nahi ho paaya.")


if __name__ == "__main__":
    unittest.main()     