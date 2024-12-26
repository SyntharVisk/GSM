import feedparser
import requests
import json
import os
from flask import jsonify, render_template, Blueprint, current_app

main_bp = Blueprint('main', __name__)

# Load API key from config.json
def load_config():
    try:
        # Get the absolute path of the config.json file in the project root
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..', 'config.json')
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            return config.get('RAWG_API_KEY')
    except FileNotFoundError:
        current_app.logger.error("config.json file not found!")
        return None
    except json.JSONDecodeError:
        current_app.logger.error("Error decoding config.json file!")
        return None

RAWG_API_KEY = load_config()

# Home route to render the main page
@main_bp.route('/')
def home():
    return render_template('index.html')

# Route to fetch the popular games using RAWG API
@main_bp.route('/popular-games')
def latest_games():
    if not RAWG_API_KEY:
        return jsonify({'error': 'API key not found in configuration'}), 500
    try:
        url = f"https://api.rawg.io/api/games?key={RAWG_API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP issues
        games_data = response.json()

        games = [
            {
                'name': game.get('name', 'Unknown'),
                'released': game.get('released', 'Unknown'),
                'background_image': game.get('background_image', None)
            } for game in games_data.get('results', [])
        ]
        return jsonify({'games': games})

    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Error fetching games from RAWG API: {e}")
        return jsonify({'error': 'Unable to fetch games'}), 500

# Route to fetch RSS feed for gaming news
@main_bp.route('/rss-feed')
def rss_feed():
    try:
        feed_url = 'https://www.pcgamer.com/rss/'
        feed = feedparser.parse(feed_url)

        if feed.bozo:
            raise ValueError(f"Error parsing RSS feed: {feed.bozo_exception}")

        items = [
            {'title': entry.title, 'link': entry.link}
            for entry in feed.entries[:10]  # Limit to 10 items
        ]
        return jsonify({'items': items})

    except Exception as e:
        current_app.logger.error(f"Error fetching RSS feed: {e}")
        return jsonify({'error': 'Unable to fetch news'}), 500
