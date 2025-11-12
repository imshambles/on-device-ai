import speech_recognition as sr
from pynput import keyboard
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from note_organizer import organize_note

# --- Configuration ---
HOTKEY = keyboard.Key.fn
SAMPLE_RATE = 44100
CHANNELS = 1
FILENAME = "output.wav"

# --- State ---
is_recording = False
audio_data = []

def on_press(key):
    """Handles key press events."""
    global is_recording, audio_data
    if key == HOTKEY and not is_recording:
        print("Recording started...")
        is_recording = True
        audio_data = []  # Clear previous recording

def on_release(key):
    """Handles key release events."""
    global is_recording
    if key == HOTKEY and is_recording:
        print("Recording stopped.")
        is_recording = False
        process_audio()
        return False  # Stop the listener

def process_audio():
    """Processes the recorded audio."""
    if not audio_data:
        print("No audio data recorded.")
        return

    print("Transcribing audio...")
    # Convert to numpy array
    audio_np = np.concatenate(audio_data, axis=0)

    # Save the recorded data as a WAV file
    write(FILENAME, SAMPLE_RATE, audio_np)

    # Transcribe the audio file
    recognizer = sr.Recognizer()
    with sr.AudioFile(FILENAME) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Transcription: {text}")
            organize_note(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


def record_audio():
    """Records audio from the microphone."""
    global audio_data
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, callback=callback):
        print("VoceNote is running. Press and hold the Fn key to record.")
        # The listener will run in the main thread and block until it is stopped.
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if is_recording:
        audio_data.append(indata.copy())

if __name__ == "__main__":
    record_audio()
