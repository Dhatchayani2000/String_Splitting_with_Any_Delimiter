import re

class StringSplitter:
    def __init__(self):
        self.delimiter = None

    def set_delimiter(self, delimiter):
        self.delimiter = delimiter

    def split_string(self, input_string):
        if self.delimiter is None:
            raise ValueError("Delimiter not set. Please use set_delimiter() method first.")

        delimiter_pattern = re.escape(self.delimiter)
        fields = re.split(delimiter_pattern, input_string)
        return fields

given_input = 'stigwith Delimiter; 1234:split12'
splitter = StringSplitter()
delimiter = input("Enter the delimiter: ")
splitter.set_delimiter(delimiter)
output = splitter.split_string(given_input)
print(output)
