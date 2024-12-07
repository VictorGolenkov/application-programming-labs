import os
import csv
import argparse

from icrawler.builtin import GoogleImageCrawler

import Iterator

def parser_for_program() -> tuple[str, str, str]:
    """
    Parses the search keyword, the name of the directory
    where the downloaded images will be saved and the name of the annotation.

    :return: A list containing the keyword, the name of the directory and the name of the annotation
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help='keyword')
    parser.add_argument('save_file', type=str, help='safe_dir')
    parser.add_argument('annotation_file', type=str, help='annotation_file')
    args = parser.parse_args()
    return args.keyword, args.save_file, args.annotation_file

def crawler(keyword: str, max_number: int, save_dir: str) -> None:
    """
    Downloads images based on a given keyword.
    :param keyword: The keyword by which images are downloaded
    :param max_number: Maximum number of images
    :param save_dir: The folder where the files will be saved
    :return: None
    """
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': save_dir})
    filters = dict(
        size='large',
        license='noncommercial,modify')
    google_crawler.crawl(keyword=keyword, filters=filters, max_num=max_number)

def create_annotation(save_dir: str, annotation_path: str) -> None:
    """
    Creates an annotation in a .csv file for images
    :param save_dir: The path to the directory where the images are saved
    :param annotation_path: The name of the annotation file
    :return: None
    """
    pictures = os.listdir(save_dir)
    with open(annotation_path,
              mode="w",
              newline="",
              encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute path", "Relative path"])
        for picture in pictures:
            abs_path = os.path.abspath(os.path.join(save_dir, picture))
            rel_path = os.path.join(save_dir, picture)
            writer.writerow([abs_path, rel_path])

def main():
    keyword, save_dir, annotation_file = parser_for_program()
    crawler(keyword, 100, save_dir)
    create_annotation(save_dir,annotation_file)
    it = iter(Iterator.IteratorForImages(annotation_file))

    for image in it:
        print("Очередное значение:", image)

if __name__ == "__main__":
     main()