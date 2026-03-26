from waitress import serve
from flask import Flask, send_file, abort
import os, sys

app = Flask(__name__)

# This looks for a file at tiles/z/x/y.png
@app.route('/<string:map_name>/<int:z>/<int:x>/<int:y>.png')
def serve_tile(map_name, z, x, y):
    tile_path = f'tiles/{map_name}/{z}/{x}/{y}.png'
    
    if os.path.exists(tile_path):
        return send_file(tile_path, mimetype='image/png')
    else:
        # Returns a 404 if the specific tile doesn't exist
        abort(404)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"Usage: python {sys.argv[0]} [port]")
        sys.exit(1)

    if len(sys.argv) > 2 and 'dev' in sys.argv:
        app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
    else:
        print(f"Starting server on port {sys.argv[1]}...")
        serve(app, host='0.0.0.0', port=int(sys.argv[1]))