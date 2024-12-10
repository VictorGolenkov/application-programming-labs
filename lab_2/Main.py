import argparse

import Crawler
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

def main():
    try:
        keyword, save_dir, annotation_file = parser_for_program()
        Crawler.crawler(keyword, 100, save_dir)
        Crawler.create_annotation(save_dir, annotation_file)
        it = iter(Iterator.IteratorForImages(annotation_file))

        for image in it:
            print("Очередное значение:", image)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
