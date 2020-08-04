import pyexr
import numpy as np

if __name__ == '__main__':

    shift_coords = [[1, 0], [0, 1]]

    path = "path/to/some/image.exr"
    img = pyexr.read(path)

    height = img.shape[0]
    width = img.shape[1]

    r = pyexr.read(path, "R")
    g = pyexr.read(path, "G")
    b = pyexr.read(path, "B")
    a = pyexr.read(path, "A")


    for coords in shift_coords:

        new_r = np.zeros((height, width, 1))
        new_g = np.zeros((height, width, 1))
        new_b = np.zeros((height, width, 1))
        # new_a = np.zeros((height, width, 1))

        print(width, height)

        for h in range(height):
            for w in range(width):
                target_w = w+coords[0]
                target_h = h+coords[1]
                if target_w < width and target_w >= 0 and target_h < height and target_h >= 0:
                    new_r[h][w] = r[target_h, target_w] - r[h][w]
                    new_g[h][w] = g[target_h, target_w] - g[h][w]
                    new_b[h][w] = b[target_h, target_w] - b[h][w]
                    # new_a[h][w] = a[target_h, target_w] - a[h][w]

        color = np.concatenate((new_r, new_g, new_b, a), axis=2)

        pyexr.write("out_"+str(coords[0])+"_"+str(coords[1])+".exr", color)
