"""
Extracts metadata from video files and stores it in machine-readable form for the purpose of checking quality inconsistencies in a video archive.

TODO: store metadata in database? optional? would enable more functionalities

Author: hemmer
Date: 2023-02-23
Version: 0.1
"""

import os  # for folder crawling
import pathlib  # for getting file path and extension
import pprint  # for human-readable printing

import ffmpeg_extensions

pretty = pprint.PrettyPrinter(indent=4)

# load from ffmpeg_extensions class
file_formats = list()

archive_path = str()
archive_files = list()
archive_metadata = list()


def main():
    folder = get_folder()

    # get extensions
    ffmpeg_extensions.use_local_extensions()
    formats = ffmpeg_extensions.load_extensions()

    get_files(folder, formats)
    read_metadata(archive_files, archive_metadata)

    pretty.pprint(archive_metadata)


def get_folder():
    """
    Gets directory path from user.

    :return: Path as string.
    """

    path = input("Please input path to video archive: ")

    while not pathlib.Path(path).is_dir():
        print(path)
        path = input("Please input valid path: ")

    return path


def get_files(folder, supported_formats):
    """
    Gets filepaths from all supported video files in a folder and its subfolders.

    :param folder:
    :param supported_formats:
    :return:
    """
    for root, subdir, files in os.walk(folder):
        for file in files:
            file_path = pathlib.PurePath(file)
            extension = file_path.suffix[1:]  # slicing to remove leading dot

            if extension in supported_formats:
                archive_files.append(file_path)


def read_metadata(files, metadata_collection):
    """
    TODO: implement ffmpeg probing
    Gets metadata from a given list of files via ffmpeg.probe and stores it in a given list.
    
    :param files: List with paths of video files (eg: 'e:/archive/films/forest_gump.mkv')
    :param metadata_collection:
    :return:
    """
    for file in files:
        metadata = "TODO"
        metadata_collection.append(metadata)


if __name__ == '__main__':
    main()
