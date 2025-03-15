import numpy as np
from PIL import Image


image = Image.open("birds.jpg")
image_array = np.array(image)

flipped_image = np.flipud(np.fliplr(image_array))

noise = np.random.randint(-50, 51, image_array.shape, dtype=np.int16) 
noisy_image = np.clip(image_array.astype(np.int16) + noise, 0, 255).astype(np.uint8)

brightened_image = np.clip(image_array + 40, 0, 255).astype(np.uint8)


h, w, _ = image_array.shape
start_x, start_y = w // 2 - 50, h // 2 - 50
masked_image = image_array.copy()
masked_image[start_y:start_y+100, start_x:start_x+100] = [0, 0, 0] 

Image.fromarray(flipped_image).save("flipped_birds.jpg")
Image.fromarray(noisy_image).save("noisy_birds.jpg")
Image.fromarray(brightened_image).save("brightened_birds.jpg")
Image.fromarray(masked_image).save("masked_birds.jpg")

print("Image processing complete. Check the saved files.")
