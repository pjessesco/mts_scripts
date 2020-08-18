import pyexr
import numpy as np
import os
import glob

if __name__ == '__main__':

    path = "path/to/directory"

    exr_list = glob.glob(os.path.join(path,"mts2_*.exr"))

    exr_list.sort()

    assert(len(exr_list)%3 == 0)

    base_color_path = exr_list[0]
    base_color_square_path = exr_list[1]

    # may have 0 because of numerical issue
    base_r = pyexr.read(base_color_path, "R")
    base_g = pyexr.read(base_color_path, "G")
    base_b = pyexr.read(base_color_path, "B")

    base_var_r = pyexr.read(base_color_square_path, "R") - np.square(base_r)
    base_var_g = pyexr.read(base_color_square_path, "G") - np.square(base_g)
    base_var_b = pyexr.read(base_color_square_path, "B") - np.square(base_b)
    a = pyexr.read(base_color_path, "A")

    base_var_avg = (base_var_r+base_var_g+base_var_b)/3
    var_base = np.concatenate((base_var_avg, base_var_avg, base_var_avg, a), axis=2)
    pyexr.write(os.path.join(path, "variance_0.exr"), var_base)

    for i in range(3, len(exr_list), 3):

        print("Perform " + str(i//3) + "th offset path")

        color_path = exr_list[i]
        color_square_path = exr_list[i+1]
        color_base_multiply_path = exr_list[i + 2]

        offset_r = pyexr.read(color_path, "R")
        offset_g = pyexr.read(color_path, "G")
        offset_b = pyexr.read(color_path, "B")

        var_r = pyexr.read(color_square_path, "R") - np.square(offset_r)
        var_g = pyexr.read(color_square_path, "G") - np.square(offset_g)
        var_b = pyexr.read(color_square_path, "B") - np.square(offset_b)

        # assert (np.all(var_r >= 0))
        # assert (np.all(var_g >= 0))
        # assert (np.all(var_b >= 0))
        a = pyexr.read(color_path, "A")

        corr_numerator_r = pyexr.read(color_base_multiply_path, "R") - base_r * offset_r
        corr_numerator_g = pyexr.read(color_base_multiply_path, "G") - base_g * offset_g
        corr_numerator_b = pyexr.read(color_base_multiply_path, "B") - base_b * offset_b

        corr_denominator_r = np.sqrt(base_var_r) * np.sqrt(var_r)
        corr_denominator_g = np.sqrt(base_var_g) * np.sqrt(var_g)
        corr_denominator_b = np.sqrt(base_var_b) * np.sqrt(var_b)

        corr_r = corr_numerator_r / corr_denominator_r
        corr_g = corr_numerator_g / corr_denominator_g
        corr_b = corr_numerator_b / corr_denominator_b

        var_avg = (var_r + var_g + var_b) / 3
        corr_avg = (corr_r + corr_g + corr_b) / 3

        var = np.concatenate((var_avg, var_avg, var_avg, a), axis=2)
        corr = np.concatenate((corr_avg, corr_avg, corr_avg, a), axis=2)

        pyexr.write(os.path.join(path, "variance_"+str(i//3)+".exr"), var)
        pyexr.write(os.path.join(path, "correlation_" + str(i // 3) + ".exr"), corr)
