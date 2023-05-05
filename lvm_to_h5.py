import os
import pandas as pd
import glob
from tqdm import tqdm

def convert_single_lvm_to_h5(input_file, output_file):
    """
    Convert a single .lvm file to a .h5 file by reading the .lvm file, processing the data,
    and writing the processed data to a .h5 file. This function handles conversion for one file
    at a time and is useful for debugging and processing individual files.

    Parameters
    ----------
    input_file : str
        Path to the .lvm file to be converted.
    output_file : str
        Path to the .h5 file where the converted data will be stored.

    Returns
    -------
    None

    Example
    -------
    input_file = "path/to/input/file.lvm"
    output_file = "path/to/output/file.h5"
    convert_single_lvm_to_h5(input_file, output_file)
    """
    try:
        # Read the .lvm file contents into a Pandas DataFrame with the 'low_memory=False' option
        df = pd.read_csv(input_file, delimiter="\t", skiprows=22, low_memory=False)

        # Convert object columns to appropriate types
        for col in df.columns:
            if df[col].dtype == 'O':
                try:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                except ValueError:
                    print(f"Cannot convert column {col} to numeric type, skipping...")

        # Write the DataFrame to the .h5 file with column headers
        with pd.HDFStore(output_file) as store:
            store.put("data", df, format="table")

        print(f"Successfully converted {input_file} to {output_file}")

    except Exception as e:
        print(f"An error occurred while converting {input_file} to {output_file}: {e}")
        
        
def convert_lvm_to_h5(input_folder, output_folder, chunksize=100000):
    """
    Convert .lvm files in a given input folder to .h5 files and store them in an output folder.
    The function reads the .lvm files in chunks to avoid memory issues and writes each chunk
    to the corresponding .h5 file.

    Parameters
    ----------
    input_folder : str
        Path to the folder containing the .lvm files to be converted.
    output_folder : str
        Path to the folder where the converted .h5 files will be stored.
    chunksize : int, optional
        Number of rows to read and write at a time (default is 50000).

    Returns
    -------
    None

    Example
    -------
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"
    convert_lvm_to_h5(input_folder, output_folder)
    """
    if not os.path.exists(input_folder):
        print(f"Input folder {input_folder} does not exist.")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all .lvm files in the input folder
    lvm_files = glob.glob(os.path.join(input_folder, "*.lvm"))

    if not lvm_files:
        print("No .lvm files found in the input folder.")
        return

    # Iterate through each .lvm file, read its contents and write to a .h5 file
    for lvm_file in tqdm(lvm_files, desc="Converting .lvm to .h5", unit="files"):
        # Create a .h5 file with the same name in the output folder
        h5_file = os.path.join(output_folder, os.path.splitext(os.path.basename(lvm_file))[0] + ".h5")

        # Check if the .h5 file already exists, skip it and print a message if it does
        if os.path.exists(h5_file):
            print(f"Skipping conversion: {h5_file} already exists.")
            continue

        # Read the .lvm file contents in chunks
        first_chunk = True
        for chunk in pd.read_csv(lvm_file, delimiter="\t", skiprows=22, low_memory=False, chunksize=chunksize):
            # Convert object columns to appropriate types
            for col in chunk.columns:
                if chunk[col].dtype == 'O':
                    try:
                        chunk[col] = pd.to_numeric(chunk[col], errors='coerce')
                    except ValueError:
                        print(f"Cannot convert column {col} to numeric type, skipping...")

            # Write the chunk to the .h5 file with column headers
            with pd.HDFStore(h5_file) as store:
                if first_chunk:
                    store.put("data", chunk, format="table")
                    first_chunk = False
                else:
                    store.append("data", chunk, format="table")
