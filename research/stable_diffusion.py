import time
import keras_cv
import keras
import matplotlib.pyplot as plt
import numpy as np

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

print("the model is ready")
prompt = "A university with a golden flower"
images = model.text_to_image(prompt, batch_size=1)
print("images are created. plotting...")
images.dump(prompt.replace(" ", "_"))
images = np.load(prompt.replace(" ", "_"), allow_pickle=True)

def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")

plot_images(images)
plt.show()

