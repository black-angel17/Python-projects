import os

# Directory path containing the files
directory = r'C:\Users\ADMIN\Downloads\CISCO Ideathon 23\CISCO Ideathon 23\CISCO Ideathon 23\CISCO Ideathon 2022\Preliminary Round Quiz'
count =0
# Loop through each file in the directory
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        # Get the current file path
        current_path = os.path.join(directory, filename)
        count = count +1
        # Generate the new file name
        new_filename = str(count) + ".jpeg"

        # Get the new file path
        new_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(current_path, new_path)

        print(f"Renamed {filename} to {new_filename}")
