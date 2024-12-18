import os


def process_numbers(input_csv, output_folder, max_per_file=200):
    """
    Processes a CSV of numbers, ensuring only numeric strings with 11 characters
    and starting with '2' are included. Splits the output into multiple files.

    Args:
        input_csv (str): Path to the input CSV file.
        output_folder (str): Directory to save the output files.
        max_per_file (int): Maximum number of valid numbers per output file.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read and process numbers from the input CSV
    with open(input_csv, 'r') as file:
        numbers = set()  # Use a set to ensure uniqueness
        for line in file:
            for num in line.split(","):  # Split CSV-style rows
                cleaned_num = num.strip()  # Remove whitespace
                # Ensure numeric, 11 characters, and begins with '2'
                if cleaned_num.isdigit() and len(cleaned_num) == 11 and cleaned_num.startswith("2"):
                    numbers.add(cleaned_num)

    # Convert the set back to a sorted list
    numbers = sorted(numbers)

    # Split numbers into chunks and write to multiple files
    file_count = 1
    for i in range(0, len(numbers), max_per_file):
        chunk = numbers[i:i + max_per_file]
        output_file = os.path.join(output_folder, f'numbers_part_{file_count}.csv')
        with open(output_file, 'w') as out_file:
            out_file.write("BVN\n")  # Add header
            for number in chunk:
                out_file.write(f"{number},\n")  # Write each number with a trailing comma
        file_count += 1

    print(f"Processing complete. Files saved in: {output_folder}")


# Example usage
input_csv = "input_numbers.csv"  # Replace with your input CSV file path
output_folder = "output_files"  # Replace with your desired output folder path
process_numbers(input_csv, output_folder)
