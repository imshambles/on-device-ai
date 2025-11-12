def organize_note(text):
    """Organizes the note into a text file."""
    lower_text = text.lower()
    if "to do" in lower_text or "to-do" in lower_text or "add to my to-do list" in lower_text:
        with open("todos.txt", "a") as f:
            f.write(f"- {text}\n")
        print("Added to to-do list.")
    elif "remind me to" in lower_text or "set a reminder" in lower_text:
        with open("reminders.txt", "a") as f:
            f.write(f"- {text}\n")
        print("Added to reminders.")
    else:
        with open("notes.txt", "a") as f:
            f.write(f"- {text}\n")
        print("Added to general notes.")
