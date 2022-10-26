from PIL import Image

image_file = Image.open(r".\colorida.jpg")

image_file = image_file.convert('L')

image_file.save(r".\preta-e-branca.jpg")