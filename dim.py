from PIL import Image
import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image path')
    parser.add_argument('image', metavar='input dir', type=str,
                        help='relative path to the image')
    im = Image.open(parser.parse_args().image)
    np_im = np.array(im)
    print(np_im.shape)