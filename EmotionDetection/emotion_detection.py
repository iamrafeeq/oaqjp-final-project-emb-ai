
import requests

def emotion_detector(text):
    # Check if input is blank
    if not text.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    # Send request to your NLP API/server
    response = requests.post("http://localhost:5000/emotionDetector", json={"text": text})
    
    # Handle bad requests
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    return response.json()
