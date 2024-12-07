import csv

class IteratorForImages:
    """
     A class for creating an iterator based on downloaded images.
    """
    def __init__(self, annotation_file:str) -> None:
        """
        Initializes the fields of the iterator
        :param annotation_file: The name of the .csv file with the annotation
        """
        self.annotation_file = annotation_file
        self.images = self.get_images()
        self.limit = len(self.images)
        self.counter = 0


    def get_images(self) -> list:
        """
        Reads the relative path to each downloaded
        image from the annotation file.
        :return: List of relative paths of downloaded images
        """
        with open(self.annotation_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            return [row[1] for row in reader]

    def __iter__(self) -> 'IteratorForImages':
        """
        Returns the ImageIterator object.
        :return: The ImageIterator object
        """
        return self

    def __next__(self) -> str:
        """
        Returns the next element from the iterator.
        :raises StopIteration: Notifies that the iterator is exhausted
        :return: The next element from the iterator
        """
        if self.counter < self.limit:
            self.counter = self.counter + 1
            return self.images[self.counter - 1]
        else:
            raise StopIteration