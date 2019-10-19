import argparse
import os
from PIL import Image


def resize_images(input_directory, convert_rgb, final_size, output_directory):

    """
    Funcion que permite tratar y dar un tamaño especifico a las imagenes
    a traves de una estrategia,dando como retroalimentacion un mensaje
    cada 10000 imagenes convertidas
    """
    try:
        files = os.listdir(input_directory)
        print(files)
        count = 0
        for item in files:
            path = os.path.join(input_directory, item)
            if os.path.isfile(path):
                try:
                    image = Image.open(path)
                    if convert_rgb != 0:
                        image = image.convert("RGB")

                    try:
                        #image_array = image_array / 255.
                        # Pillow
                        image = image.resize((int(final_size), int(final_size)), Image.ANTIALIAS)
                        image.save(os.path.join(output_directory, item), 'PNG', quality=100)
                    except Exception as e:
                        print(e)

                    if count % 10000 == 0:
                        print("Iteracion {}".format(count))
                except Exception as e:
                    print(e)
            else:
                print(f'{path} Is not a file')

        print("La tarea fallo con exito")
    except Exception as e:
        print(f'We have a problem: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resize square images from directory')
    parser.add_argument('input', metavar='input dir', type=str,
                        help='directory where are placed the images')
    parser.add_argument('output', metavar='output dir', type=str,
                        help='directory where are going to place the images')
    parser.add_argument('size', metavar='new size', type=str,
                        help='the new size will be like: nxn')
    parser.add_argument('rgb', metavar='convert RGB', type=int,
                        help='0=false n=true')

    args = parser.parse_args()
    input_dir = args.input
    output_dir = args.output
    size = args.size
    rgb = args.rgb
    print(input_dir, output_dir, size, rgb)

    resize_images(input_directory=input_dir, convert_rgb=rgb, final_size=size, output_directory=output_dir)
