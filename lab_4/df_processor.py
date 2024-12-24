import cv2
import matplotlib.pyplot as plt
import pandas as pd

def create_df(annotation: str) -> pd.DataFrame:
    """
        Reads the annotation file and creates a DataFrame.
        :param annotation: Path to the annotation file.
        :return: DataFrame containing image paths.
        """
    try:
        df = pd.read_csv(annotation)
        df.columns = ["absolute_path", "relative_path"]
    except Exception:
        raise Exception("The annotation could not be read!")

    return df

def add_info_to_df(df: pd.DataFrame) -> None:
    """
    Adds columns for image dimensions (height, width, depth) to the DataFrame.
    :param df: DataFrame containing image paths.
    :return: Updated DataFrame with height, width, and depth columns.
    """
    try:
        heights, widths, channels = [], [], []
        for path in df["relative_path"]:
                img = cv2.imread(path)
                if img is not None:
                    heights.append(img.shape[0])
                    widths.append(img.shape[1])
                    channels.append(img.shape[2])
                else:
                    heights.append(None)
                    widths.append(None)
                    channels.append(None)
        df["height"] = heights
        df["width"] = widths
        df["channels"] = channels
    except Exception:
        raise Exception("The images have not been opened!"
                    " It is impossible to determine"
                    " their characteristics!")

def calc_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates statistical information for image dimensions.
    :param df: DataFrame containing image dimensions.
    :return: Statistical summary of the DataFrame.
    """
    try:
        return df[["height", "width", "channels"]].describe()
    except Exception:
        raise Exception("It is impossible to calculate statistical data!")

def filter_for_df(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Filters the DataFrame to include only images within specified size limits.
    :param df: DataFrame containing image dimensions.
    :param max_height: Maximum allowed image height.
    :param max_width: Maximum allowed image width.
    :return: Filtered DataFrame.
    """
    try:
        return df[(df["height"] <= max_height) & (df["width"] <= max_width)]
    except Exception:
        raise Exception("It is impossible to filter DataFrame!")

def add_area(df: pd.DataFrame) -> None:
    """
    Adds a new column 'Area' to the DataFrame, representing the image area.
    :param df: DataFrame containing image dimensions.
    :return: Updated DataFrame with the 'Area' column.
    """
    try:
        df["area"] = df["height"] * df["width"]
    except Exception:
        raise Exception("It is impossible to add a new column!"
                        " Perhaps the DataFrame does not exist!")

def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sorts the DataFrame in ascending order by the 'Area' column.
    :param df: DataFrame containing the 'Area' column.
    :return: Sorted DataFrame.
    """
    try:
        return df.sort_values(by='area')
    except Exception:
        raise Exception("The DataFrame cannot be sorted!"
                        " Perhaps the DataFrame does not exist!")

def plot_hist(df: pd.DataFrame) -> None:
    """
    Plots a histogram of image areas.
    :param df: DataFrame containing the 'Area' column.
    :return: None
    """
    try:
        df["area"].plot(kind="hist",
                        ylabel="Frequency",
                        xlabel="Area (pixels)",
                        title="Distribution of image areas",
                        grid=True
                        )
        plt.show()
    except Exception:
        raise Exception("The histogram cannot be displayed!"
                        " Perhaps the DataFrame does not exist!")

