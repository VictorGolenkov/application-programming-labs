import argparse
import os
import csv
import argparse

from icrawler.builtin import BingImageCrawler

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

    :param keyword:
    :param max_number:
    :param save_dir:
    :return: None
    """
    google_crawler = BingImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': save_dir})
    filters = dict(
        license='noncommercial,modify')
    google_crawler.crawl(keyword=keyword, filters=filters, max_num=max_number)

def create_annotation(save_dir: str, annotation_path: str):
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

class IteratorForImages:
    def __init__(self, limit, annotation_dir):
        self.no_of_elements = limit
        self.counter = 0
        self.annotation_file = annotation_file

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter = self.counter + 1
            return self
        else:
            raise StopIteration

def main():
    a = parser_for_program()
    crawler(a[0], 200, a[1])
    create_annotation(a[1],a[2])


if __name__ == "__main__":
     main()