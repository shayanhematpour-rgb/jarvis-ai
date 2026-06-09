print("Jarvis AI started...")
from speech.speak import speak
from speech.listen import listen

speak("Jarvis is online")

while True:
    command = listen().lower()

    if "hello" in command:
        speak("Hello boss")

    elif "your name" in command:
        speak("I am Jarvis")

    elif "stop" in command:
        speak("Goodbye")
        break

    else:
        speak("I did not understand")
      
