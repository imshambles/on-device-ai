# VoceNote: Your Voice-Powered Note-Taking Assistant

VoceNote is a desktop application designed to streamline your note-taking process using the power of your voice. Inspired by the convenience of tools like Wispr Flow, VoceNote allows you to instantly capture your thoughts, to-do items, and reminders by simply pressing a hotkey and speaking. It's designed to be a seamless addition to your workflow, helping you stay organized without breaking your focus.

## 🚀 Overview

In a fast-paced digital environment, capturing fleeting ideas is crucial. VoceNote eliminates the friction of traditional note-taking by providing a rapid, voice-first interface. Press a key, say what's on your mind, and let the application handle the transcription and organization. The goal is to make note-taking as natural as speaking.

## ✨ Features

- **Hotkey Activation**: A globally accessible hotkey (e.g., the `Fn` key) allows you to start and stop recording from any application.
- **High-Fidelity Transcription**: Utilizes advanced speech recognition to accurately convert your voice into text.
- **Intelligent Organization**: Automatically sorts your notes into categories like `to-do lists` and `reminders` based on the content of your speech.
- **Minimalist Design**: Runs discreetly in the background, ensuring it's there when you need it without being intrusive.
- **Local and Private**: All your notes are stored locally on your machine, ensuring your data remains private.

## 🛠️ High-Level Development Plan

This project will be developed in the following phases:

1.  **Core Voice-to-Text Engine**:
    -   Implement the fundamental audio recording and speech-to-text transcription service using a Python library.
2.  **Global Hotkey Listener**:
    -   Integrate a cross-platform library to listen for a specific key combination to trigger the recording function.
3.  **Note Categorization Logic**:
    -   Develop a simple NLP-based classifier to analyze the transcribed text and identify keywords to sort notes into `todos.txt`, `reminders.txt`, and `general_notes.txt`.
4.  **File Management**:
    -   Create a system for creating, appending, and managing the text files where the notes will be stored.
5.  **Future Enhancements (Optional)**:
    -   Develop a simple GUI for viewing and managing notes.
    -   Add support for custom hotkeys and categories.
    -   Integrate with calendar and to-do applications.

## 🤝 Contributing

This is an open-source project, and contributions are welcome. Please refer to `CONTRIBUTING.md` for guidelines on how to get involved.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
