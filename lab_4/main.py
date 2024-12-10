import argparse
import os

import df_processor

def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments to retrieve the path to the annotation file.
    :return: Parsed arguments containing the annotation file path.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation_path",
                        type=str,
                        help="Path to the annotation"
                        )

    args = parser.parse_args()

    if not os.path.exists(args.annotation_path):
        raise Exception("The annotation file was not found!")

    return args


def main():
    try:
        args = parse_arguments()
        annotation_file = args.annotation_path

        df = df_processor.create_df(annotation_file)
        print(df)

        df = df_processor.add_info_to_df(df)

        print("Statistical information:")
        print(df_processor.calc_stats(df), end="\n\n")

        max_height, max_width = 1000, 1000
        filtered_df = df_processor.filter_for_df(df, max_height, max_width)
        print("Filtered data:")
        print(filtered_df, end="\n\n")

        df = df_processor.add_area(df)
        df = df_processor.sort_by_area(df)
        print("Sorted data:")
        print(df, end="\n\n")

        df_processor.plot_hist(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()