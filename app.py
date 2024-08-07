from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load queries from JSON file
with open('queries.json', 'r') as file:
    queries = json.load(file)['queries']

@app.route('/')
def index():
    # Get the query index from the URL parameter (default to 0)
    query_index = int(request.args.get('query', 0))
    # Ensure the index is within range
    if query_index < 0 or query_index >= len(queries):
        query_index = 0

    query = queries[query_index]
    return render_template('index.html', query=query, query_index=query_index, total_queries=len(queries))

@app.route('/queries')
def get_queries():
    return jsonify(queries)

if __name__ == '__main__':
    app.run(debug=True)
