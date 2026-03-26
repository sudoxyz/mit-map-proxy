import os, sys
from PIL import Image


def generate_tiles(image_path, map_name, max_zoom):
    map_name = f"tiles/{map_name}"
    original_img = Image.open(image_path).convert("RGBA")
    tile_size = 256

    for z in range(max_zoom + 1):
        num_tiles = 2**z
        level_pixel_size = num_tiles * tile_size
        
        # Create a transparent square canvas for this zoom level
        canvas = Image.new("RGBA", (level_pixel_size, level_pixel_size), (0, 0, 0, 0))
        
        # Resize original image to fit within the canvas while keeping aspect ratio
        img_ratio = original_img.width / original_img.height
        if img_ratio > 1:
            # Wider than tall
            new_w = level_pixel_size
            new_h = int(level_pixel_size / img_ratio)
        else:
            # Taller than wide
            new_h = level_pixel_size
            new_w = int(level_pixel_size * img_ratio)
            
        resized_img = original_img.resize((new_w, new_h), Image.LANCZOS)
        
        # Paste the resized image into the center of the transparent canvas
        offset_x = (level_pixel_size - new_w) // 2
        offset_y = (level_pixel_size - new_h) // 2
        canvas.paste(resized_img, (offset_x, offset_y))
        
        # Slice the canvas into tiles
        for x in range(num_tiles):
            for y in range(num_tiles):
                left = x * tile_size
                top = y * tile_size
                right = left + tile_size
                bottom = top + tile_size
                
                tile = canvas.crop((left, top, right, bottom))
                
                # Only save if the tile isn't completely empty/transparent
                if tile.getbbox(): 
                    save_path = os.path.join(map_name, str(z), str(x))
                    os.makedirs(save_path, exist_ok=True)
                    tile.save(os.path.join(save_path, f"{y}.png"))
                    print(f"Saved: {map_name}/{z}/{x}/{y}.png")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} <image.png> <map_name> <max_zoom>")
        sys.exit(1)

    generate_tiles(sys.argv[1], sys.argv[2], int(sys.argv[3]))
