from PIL import Image
from tqdm import tqdm
import numpy as np
import os

# ==== CONFIG ====
set_input_folder = "input"        # Folder containing images
set_width = 512                   # Target width
set_output_directory = "output"   # Output folder
# =================

# Read and convert image to grayscale
def read_and_convert_image(image_path):
    image = Image.open(image_path)
    return image.convert('L')

# Scale image while keeping aspect ratio
def scale_image(image, base_width=600):
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    return image.resize((base_width, h_size), Image.Resampling.NEAREST)

# Atkinson Dithering algorithm implementation
def atkinson_dithering(image):
    img_array = np.array(image, dtype=np.float32)
    height, width = img_array.shape

    # Atkinson diffusion offsets (dx, dy)
    offsets = [(1,0), (2,0), (-1,1), (0,1), (1,1), (0,2)]

    for y in range(height):
        for x in range(width):
            old_pixel = img_array[y, x]
            new_pixel = 255 if old_pixel > 127 else 0
            img_array[y, x] = new_pixel
            error = (old_pixel - new_pixel) / 8.0

            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    img_array[ny, nx] += error

    return Image.fromarray(np.uint8(np.clip(img_array, 0, 255)), 'L')


# Save as PNG with sequential name
def save_to_png(image, index):
    os.makedirs(set_output_directory, exist_ok=True)
    filename = f"image_{index:04d}.png"  # e.g., image_0001.png
    output_path = os.path.join(set_output_directory, filename)
    image.save(output_path, "PNG")
    print(f"[✔] Saved: {output_path}")

# Process one image
def process_image(image_path, index, base_width):
    image = read_and_convert_image(image_path)
    scaled = scale_image(image, base_width)
    dithered = atkinson_dithering(scaled)
    save_to_png(dithered, index)

# Main loop — process all images in folder
def process_folder(input_folder, base_width):
    supported_exts = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_exts)]
    files.sort()  # ensure consistent order

    if not files:
        print("❌ No images found in input folder.")
        return

    for idx, f in enumerate(files, start=1):
        process_image(os.path.join(input_folder, f), idx, base_width)

# ==== RUN ====
process_folder(set_input_folder, set_width)
