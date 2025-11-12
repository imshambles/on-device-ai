import unittest
from unittest.mock import patch, mock_open
from note_organizer import organize_note

class TestVoceNote(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_organize_note(self, mock_file):
        # Test "to-do" note
        organize_note("add milk to my to-do list")
        mock_file.assert_called_with("todos.txt", "a")
        mock_file().write.assert_called_with("- add milk to my to-do list\n")

        # Test "reminder" note
        organize_note("remind me to call the doctor")
        mock_file.assert_called_with("reminders.txt", "a")
        mock_file().write.assert_called_with("- remind me to call the doctor\n")

        # Test "general" note
        organize_note("this is a general note")
        mock_file.assert_called_with("notes.txt", "a")
        mock_file().write.assert_called_with("- this is a general note\n")

if __name__ == '__main__':
    unittest.main()
