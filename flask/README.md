# Flask + HTMX Demo

A minimal Flask web server demonstrating HTMX functionality with a "Hello World" page and dynamic user loading.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository
2. Navigate to the `flask` directory
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

1. Start the Flask development server:
```bash
python app.py
```
2. Open your browser and visit `http://localhost:5000`

## Features

- Static "Hello World" page
- HTMX integration via unpkg CDN
- Dynamic user loading from JSONPlaceholder API
- Server-side rendered HTML fragments

## Project Structure

```
flask/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── templates/         
    ├── index.html     # Main page template
    └── users.html     # User list template fragment
```
