# MIT Map Proxy

I made this project because I could not find an easy way to use a custom image as my map in MIT App Inventor. This project allows you to generate tiles from an image, which are then served on an endpoint in a standard XYZ tile format compatible with libraries like Leaflet.js or OpenLayers.  

## How It Works

The project consists of two main Python scripts:

### 1. Tile Generation (`generate.py`)

This script takes a source image (e.g., `map.png`) and generates a directory of map tiles.

-   It creates multiple zoom levels.
-   For each zoom level, it resizes the source image to fit within a square canvas, preserving the aspect ratio and centering it on a transparent background.
-   It then slices this canvas into 256x256 pixel tiles.
-   To save space, it only saves tiles that contain image data (i.e., are not completely transparent).

### 2. Tile Server (`app.py`)

This is a lightweight Flask web application that serves the generated tiles.

-   It exposes a single URL endpoint: `/<z>/<x>/<y>.png`.
-   When a request is received, it looks for the corresponding tile in the `tiles` directory.
-   If the tile exists, it's served as a PNG image.
-   If the tile does not exist (either because it was outside the map bounds or was completely transparent), it returns a `404 Not Found` error.

## Usage

1.  **Place your map image:**
    Put your source map image in the root of the project directory and name it `map.png`.

2.  **Generate the tiles:**
    Run the `generate.py` script. You can modify the `max_zoom` level at the bottom of the script.
    ```bash
    python generate.py
    ```
    This will create a `tiles` directory with the generated tile images structured as `tiles/{z}/{x}/{y}.png`.

3.  **Run the server:**
    Start the Flask application.
    ```bash
    python app.py 5000
    ```
    The server will start on `http://0.0.0.0:5000`.

4.  **Access the tiles:**
    You can now access your map tiles from any application or browser at `http://localhost:5000/{z}/{x}/{y}.png`. For example: `http://localhost:5000/3/4/3.png`.

    For use with `MIT App Inventor` you will need to either host this app on a VPS, Vercel (or similar), or self-host with port forwarding.

    Once setup you can simply enter `http(s)://hostname:port/{z}/{x}/{y}.png` into the advanced options of the map and you image will load. 


