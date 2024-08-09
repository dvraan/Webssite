from flask import Flask, render_template, request, jsonify, url_for, redirect
import json

app = Flask(__name__)

# Load queries from JSON file
with open('queries.json', 'r') as file:
    queries = json.load(file)['queries']

# Helper function to find a query by title
def find_query_by_title(title):
    for index, query in enumerate(queries):
        if query['title'] == title:
            return query, index
    return None, -1

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the DAX page
@app.route('/dax')
def dax():
    dax_functions = [query['title'] for query in queries if 'DAX' in query['title']]
    return render_template('dax.html', functions=dax_functions, title="DAX")

# Route for the SQL page
@app.route('/sql')
def sql():
    sql_functions = [query['title'] for query in queries if 'SQL' in query['title']]
    return render_template('sql.html', functions=sql_functions, title="SQL")

# Route for the Pandas page
@app.route('/pandas')
def pandas():
    pandas_functions = [query['title'] for query in queries if 'Pandas' in query['title']]
    return render_template('pandas.html', functions=pandas_functions, title="Pandas")

# Route for the query examples
@app.route('/query')
def query():
    query_title = request.args.get('query', "")
    query, query_index = find_query_by_title(query_title)
    if query is None:
        return "Query not found", 404

    prev_query = queries[query_index - 1]['title'] if query_index > 0 else None
    next_query = queries[query_index + 1]['title'] if query_index < len(queries) - 1 else None

    return render_template(
        'query.html', 
        query=query, 
        prev_query=prev_query, 
        next_query=next_query
    )

@app.route('/queries')
def get_queries():
    return jsonify(queries)

if __name__ == '__main__':
    app.run(debug=True)
