import argparse
import grpc
import pathlib
import image_visualization_service_pb2 as vis
import image_visualization_service_pb2_grpc as vis_grpc
import time


def parse_args():
    parser = argparse.ArgumentParser(
        description='Test for Web Visualization Service '
                    'for the Tag My Outfit Pipeline')
    parser.add_argument(
        '--target',
        default='localhost:8061',
        help='Location where the server to test is listening')
    parser.add_argument(
        '--delay',
        type=int,
        default=1,
        help='Delay between images in seconds')
    parser.add_argument(
        'images',
        help='Path to the images folder to use or to a single image')
    return parser.parse_args()


def images_paths_generator(images):
    if images.is_file():
        return images,
    return filter(
        lambda x: x.is_file() and x.suffix in {'.jpg', '.png'},
        images.iterdir())


def send_image(stub, img_path):
    with open(img_path, 'rb') as fp:
        image_bytes = fp.read()
    request = vis.Image(data=image_bytes)
    stub.Visualize(request)


def send_images(channel, images_dir, delay):
    stub = vis_grpc.ImageVisualizationServiceStub(channel)
    path = pathlib.Path(images_dir)
    for img_path in images_paths_generator(path):
        send_image(stub, img_path)
        time.sleep(delay)


def main():
    args = parse_args()
    target = args.target
    images = args.images
    delay = args.delay
    with grpc.insecure_channel(target) as channel:
        send_images(channel, images, delay)


if __name__ == '__main__':
    main()
