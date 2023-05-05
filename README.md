# LVM to H5 Converter

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## Overview

The LVM to H5 Converter is a Python-based tool designed to process and convert data from .lvm files to .h5 files. The tool reads .lvm files, extracts the data, and writes the data to .h5 files. This project aims to help users manage, process, and store large datasets more efficiently by converting data from the .lvm format, which is commonly used in LabVIEW applications, to the .h5 format, which is widely used in scientific computing for its performance and flexibility.

## Features

### Data Processing and Conversion
- Reads and processes .lvm files containing data in a tabular format
- Preserves headers in the final pandas dataframe
- Handles large .lvm files by reading and writing data in chunks
- Converts .lvm files to .h5 files, preserving the original data structure
- Automatically detects existing .h5 files and skips them to avoid duplicating work

### User Interface
- Provides a simple command-line interface for specifying input and output folders
- Displays a progress bar to track the conversion status
- Offers functions for converting single .lvm files to .h5 files for debugging and individual file processing
- Allows users to read .h5 files into pandas DataFrames for further data manipulation

## Installation

1. Clone the repository to your local machine:
```
git clone https://github.com/josmarcristello/LVMtoH5
```

2. Change into the project directory:
```
cd LVMtoH5
```
3. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```
4. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Place your .lvm files in an input folder of your choice.

2. Create an output folder where the converted .h5 files will be stored.

3. Run the main script with the input and output folder paths:

```python
from lvm_to_h5 import convert_lvm_to_h5

input_folder = "path/to/input/folder"
output_folder = "path/to/output/folder"

convert_lvm_to_h5(input_folder, output_folder)
```

4. The converted .h5 files will be stored in the output folder.

5. To read the .h5 files into pandas DataFrames, you can use the `read_h5_to_dataframe` function:

```python
from lvm_to_h5 import read_h5_to_dataframe

h5_file = "path/to/output/file.h5"
df = read_h5_to_dataframe(h5_file)
print(df.head())
```

## Contributing

We welcome contributions to improve this project. Please submit a pull request with your proposed changes, and ensure your code follows the project's style guidelines and best practices.

## License

This project is licensed under the MIT License. Please see the `LICENSE` file for more information.