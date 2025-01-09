async function generateContent() {
    const query = document.getElementById('query').value;
    const response = await fetch('http://localhost:5000/generate_content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    });
    const data = await response.json();
    document.getElementById('generatedContent').innerText = data.content;
}

async function summarizeContent() {
    const content = document.getElementById('contentToSummarize').value;
    const response = await fetch('http://localhost:5000/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: content })
    });
    const data = await response.json();
    document.getElementById('summarizedContent').innerText = data.summary;
}
