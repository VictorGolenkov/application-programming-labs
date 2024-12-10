import csv
import os


from icrawler.builtin import GoogleImageCrawler

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
