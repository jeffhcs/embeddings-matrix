from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from knn import KNN
from embed import embed_single
import os
from matrix import get_plot

app = Flask(__name__)
CORS(app)

knn = KNN()

print('Ready!')

@app.route('/')
def hello():
    return "<h1>Jeff Huang"

@app.route('/playground', defaults={'path': ''})
@app.route('/<path:path>')
def serve_public(path):
    if path != "" and os.path.exists(os.path.join("dist", path)):
        return send_from_directory('dist', path)
    else:
        return send_from_directory('dist', 'index.html')



@app.route('/playground/search')
def search_knn():
    text = request.args.get('text').strip()
    embedding = embed_single(text)

    k = 10

    weighted_nn = knn.find_nearest_neighbors(embedding, True, k)
    unweighted_nn = knn.find_nearest_neighbors(embedding, False, k)

    output = {
        'weighted': weighted_nn,
        'unweighted': unweighted_nn
    }

    return jsonify(output)


@app.route('/playground/heatmap.png')
def heatmap_png():
    texts_raw = request.args.get('texts')
    texts = [text.strip() for text in texts_raw.split('\n')]

    model = request.args.get('model')
    metric = request.args.get('metric')

    output = get_plot(texts, metric, model)
    
    return send_file(output, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
