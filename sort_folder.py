import argparse
from pathlib import Path
from shutil import copyfile, unpack_archive
from threading import Thread
import logging


parser = argparse.ArgumentParser(description='App for sorting folder')
parser.add_argument('-s', '--source', required=True)
parser.add_argument('-o', '--output', default='sorted_folder')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')

folders = []


def grabs_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)

def sort_folder(path: Path):
    for element in path.iterdir():
        if element.is_file():
            extension = element.suffix
            if extension == '.jpeg' or extension == '.png' or extension == '.jpg' or extension == '.sng':
                new_path = output_folder / 'images'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / element.name)
            elif extension == extension == '.avi' or extension == '.mp4' or extension == '.mov' or extension == '.mkv':
                new_path = output_folder / 'video'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / element.name)
            elif extension == '.DOC' or extension == '.docx' or extension == '.txt' or extension == '.pdf' or extension == '.xlsx' or extension == '.pptx':
                new_path = output_folder / 'documents'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / element.name)
            elif extension == '.MP3' or extension == '.ogg' or extension == '.wav' or extension == '.amr':
                new_path = output_folder / 'audio'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / element.name)
            elif extension == extension == '.zip' or extension == '.gz' or extension == '.tar':
                new_path = output_folder / 'archives' / element.name
                unpack_archive(element, new_path)
            else:
                new_path = output_folder / 'others'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / element.name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    base_folder = Path(source)
    output_folder = Path(output)

    folders.append(base_folder)
    grabs_folder(base_folder)

    threads = []
    for folder in folders:
        th = Thread(target=sort_folder, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print('Success!')