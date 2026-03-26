from waitress import serve
from flask import Flask, send_file, abort
import os

app = Flask(__name__)

# This looks for a file at tiles/z/x/y.png
@app.route('/<int:z>/<int:x>/<int:y>.png')
def serve_tile(z, x, y):
    tile_path = f'tiles/{z}/{x}/{y}.png'
    
    if os.path.exists(tile_path):
        return send_file(tile_path, mimetype='image/png')
    else:
        # Returns a 404 if the specific tile doesn't exist
        abort(404)
if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=9999)
#	serve(app, host='0.0.0.0', port=9999)
