# WordWeaver

WordWeaver is a Flask-based web application that provides two main features:
1. Content Generation: Generate detailed articles based on any topic
2. Text Summarization: Summarize long pieces of text into concise versions

## Features

- AI-powered content generation using OpenAI's GPT-3.5
- Text summarization with smart sentence analysis
- Modern and responsive user interface
- Real-time processing

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd wordweaver
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the interface to:
   - Generate content by entering a topic
   - Summarize text by pasting it into the text area

## Project Structure

```
wordweaver/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── static/
│   └── css/
│       └── style.css  # CSS styles
└── templates/
    └── index.html     # Main HTML template
```

## Note

Make sure to keep your OpenAI API key secure and never commit it to version control. 