# 🖼️ Batch Atkinson Dithering

This script applies **Atkinson dithering** to all images in a folder and saves them as sequentially numbered PNGs (`image_0001.png`, `image_0002.png`, etc.).

---

## ✨ Features

- **Atkinson Dithering**: Classic retro dithering algorithm.  
- **Batch Processing**: Processes every supported image in the input folder.  
- **Sequential Output**: Outputs files as `image_0001.png`, `image_0002.png`, etc.  
- **Custom Width**: Resizes images to a given width while keeping aspect ratio.  
- **Simple Setup**: Just drop images in the input folder and run the script.  

---

## 📋 Requirements

You need Python installed, along with these libraries:

- [Pillow](https://pypi.org/project/pillow/)  
- [NumPy](https://pypi.org/project/numpy/)  
- [tqdm](https://pypi.org/project/tqdm/)  

Install dependencies with:


```

```bash
pip install pillow numpy tqdm
```

<h3> ✨ Set Parameters in the Script

```bash
set_input_folder = "input"        # Folder with source images
set_width = 1024                  # Resize width (keeps aspect ratio)
set_output_directory = "output"   # Folder for results
