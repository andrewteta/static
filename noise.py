import random
import numpy as np
# import matplotlib.pyplot as plt
import plotly.express as px
import time
import os
from PIL import Image


def gen_noise(img: np.ndarray):
    X = np.shape(img)[0]
    Y = np.shape(img)[1]
    for y in range(Y):
        for x in range(X):
            bright = random.randint(0, 255)
            img[x][y] = [bright, bright, bright]


def gen_frame(mx):
    # fig = px.imshow(mx)
    fig = Image.fromarray(mx)
    # fig.show()
    return fig


def main():

    X = 400
    Y = 500
    img = np.zeros((X, Y, 3), dtype=np.uint8)

    if not os.path.exists('./images'):
        os.mkdir('images')

    gen_noise(img)

    # plt.ion()
    # fig = plt.figure()
    # ax = plt.imshow(img)
    # plt.show(block=False)

    gif = []
    n_frames = 10
    for i in range(n_frames):
        # plt.pause(0.01)
        gen_noise(img)
        # ax.set_data(img)
        # fig.canvas.flush_events()
        fig = gen_frame(img)
        # fig.write_image(f'images/img{i}.png')
        gif.append(fig)
    gif[0].save('./videos/static.gif', save_all=True,
                optimize=True, append_images=gif[1:n_frames], loop=0)


if __name__ == "__main__":
    main()
