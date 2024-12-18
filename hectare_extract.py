import csv

# File paths for the CSV file
# initialise the file location
file1_path = "first_list.csv"  # Replace with your actual path
file2_path = "second_list.csv"  # Replace with your actual path
output_file_path = "matched_results.csv"  # Output file path

# Read the first CSV into a list of BVNs
with open(file1_path, mode='r') as file1:
    reader = csv.DictReader(file1)
    first_list = [row['BVN'] for row in reader]

# Read the second CSV into a dictionary with BVN as the key and SIZE as the value
with open(file2_path, mode='r') as file2:
    reader = csv.DictReader(file2)  # Now looking for "BVN" directly
    second_list = {row['BVN']: row['SIZE'] for row in reader}

# Prepare matched results
matched_results = []
for bvn in first_list:
    if bvn in second_list:
        matched_results.append({'BVN': bvn, 'SIZE': second_list[bvn]})

# Write the matched results to a new CSV
with open(output_file_path, mode='w', newline='') as output_file:
    fieldnames = ['BVN', 'SIZE']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(matched_results)

print(f"Matched results have been written to {output_file_path}")