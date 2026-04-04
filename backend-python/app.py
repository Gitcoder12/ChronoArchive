from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data structures for demonstration purposes
countries = []
timelines = []
artifacts = []
museums = []
research_gaps = []

# Endpoints for the API

@app.route('/api/countries', methods=['GET'])
def get_countries():
    return jsonify(countries), 200

@app.route('/api/timelines', methods=['GET'])
def get_timelines():
    return jsonify(timelines), 200

@app.route('/api/artifacts', methods=['GET'])
def get_artifacts():
    return jsonify(artifacts), 200

@app.route('/api/museums', methods=['GET'])
def get_museums():
    return jsonify(museums), 200

@app.route('/api/research-gaps', methods=['GET'])
def get_research_gaps():
    return jsonify(research_gaps), 200

if __name__ == '__main__':
    app.run(debug=True)