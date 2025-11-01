from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Simple HTML template for testing
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Emotion Detector</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; }
        button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; }
        .result { margin-top: 20px; padding: 10px; background-color: #f0f0f0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Emotion Detector</h1>
        <form action="/detect" method="post">
            <input type="text" name="text" placeholder="Enter text to analyze emotions..." required>
            <button type="submit">Detect Emotion</button>
        </form>
        {% if result %}
        <div class="result">
            <h3>Result:</h3>
            <p><strong>Text:</strong> {{ result.text }}</p>
            <p><strong>Emotion:</strong> {{ result.emotion }}</p>
            <p><strong>Confidence:</strong> {{ result.confidence }}%</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/detect', methods=['POST'])
def detect_emotion():
    text = request.form.get('text', '')
    
    # Placeholder emotion detection logic
    # TODO: Replace with actual emotion detection model
    emotion, confidence = analyze_emotion(text)
    
    result = {
        'text': text,
        'emotion': emotion,
        'confidence': confidence
    }
    
    return render_template_string(HTML_TEMPLATE, result=result)

@app.route('/api/detect', methods=['POST'])
def api_detect_emotion():
    """API endpoint for emotion detection"""
    data = request.get_json()
    text = data.get('text', '')
    
    emotion, confidence = analyze_emotion(text)
    
    return jsonify({
        'text': text,
        'emotion': emotion,
        'confidence': confidence
    })

def analyze_emotion(text):
    """
    Placeholder function for emotion analysis
    TODO: Implement actual emotion detection using ML model
    """
    # Simple rule-based emotion detection for demo
    text_lower = text.lower()
    
    if any(word in text_lower for word in ['happy', 'joy', 'excited', 'great', 'awesome']):
        return 'happy', 85
    elif any(word in text_lower for word in ['sad', 'depressed', 'terrible', 'awful']):
        return 'sad', 78
    elif any(word in text_lower for word in ['angry', 'mad', 'furious', 'hate']):
        return 'angry', 82
    elif any(word in text_lower for word in ['afraid', 'scared', 'fear', 'terrified']):
        return 'fear', 75
    elif any(word in text_lower for word in ['surprised', 'wow', 'amazing', 'shocked']):
        return 'surprise', 70
    else:
        return 'neutral', 60

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
