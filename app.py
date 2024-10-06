from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista para almacenar la cola de reproducción
video_queue = []

@app.route('/')
def index():
    return render_template('index.html')

# Endpoint para agregar una URL a la cola
@app.route('/add_video', methods=['POST'])
def add_video():
    video_url = request.json.get('url')
    if video_url:
        video_queue.append(video_url)
        return jsonify({'message': 'Video added successfully!', 'queue': video_queue})
    return jsonify({'message': 'Invalid URL'}), 400

# Endpoint para obtener la cola de videos
@app.route('/get_queue', methods=['GET'])
def get_queue():
    return jsonify(video_queue)

# Endpoint para remover el primer video de la cola
@app.route('/remove_first_video', methods=['POST'])
def remove_first_video():
    if video_queue:
        video_queue.pop(0)
    return jsonify(video_queue)

if __name__ == '__main__':
    app.run(debug=True)