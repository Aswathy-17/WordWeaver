from flask import Flask, render_template, request, jsonify
from modules.content_generator import generate_content
from modules.text_summarizer import summarize_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate_page():
    return render_template('generate.html')

@app.route('/summarize')
def summarize_page():
    return render_template('summarize.html')

@app.route('/api/generate', methods=['POST'])
def api_generate():
    topic = request.json.get('topic')
    return generate_content(topic)

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    text = request.json.get('text')
    return summarize_text(text)

if __name__ == '__main__':
    app.run(debug=True)
