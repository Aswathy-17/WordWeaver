from flask import Flask, request, jsonify
from content_generation import generate_content
from summarization import summarize_content

app = Flask(__name__)

@app.route("/generate_content", methods=["POST"])
def generate_content_route():
    data = request.json
    query = data.get("query")
    generated_content = generate_content(query)
    return jsonify({"content": generated_content})

@app.route("/summarize", methods=["POST"])
def summarize_content_route():
    data = request.json
    content = data.get("content")
    summary = summarize_content(content)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
