"""
server.py

This module contains a Flask web application for emotion detection.
It uses the EmotionDetection.emotion_detector function to process user input
and returns the detected emotions in a formatted response.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Handle GET and POST requests for the emotion detection application.

    GET: Render the input form.
    POST: Process the submitted text using the emotion_detector function
          and return the formatted result or an error message if the input
          is invalid or blank.

    Returns:
        Rendered HTML template with the result variable.
    """
    result = None
    if request.method == 'POST':
        text = request.form.get('text_to_analyze')
        
        if text and text.strip():
            result_dict = emotion_detector(text)
            if result_dict['dominant_emotion'] is None:
                result = "Invalid text! Please try again!"
            else:
                result = (
                    f"For the given statement, the system response is "
                    f"'anger': {result_dict['anger']}, "
                    f"'disgust': {result_dict['disgust']}, "
                    f"'fear': {result_dict['fear']}, "
                    f"'joy': {result_dict['joy']}, "
                    f"'sadness': {result_dict['sadness']}. "
                    f"The dominant emotion is {result_dict['dominant_emotion']}."
                )
        else:
            result = "Invalid text! Please try again!"
            
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Run the Flask development server.
    # Host: 0.0.0.0 (accessible externally)
    # Port: 5000
    # Debug mode: True
    app.run(host='0.0.0.0', port=5000, debug=True)
