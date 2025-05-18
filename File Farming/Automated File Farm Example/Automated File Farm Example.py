import os
import time
import random
import string

class FileFarm:
    def __init__(self, filename, interval=5, iterations=10):
        """
        Initializes the FileFarm with a file and automation settings.
        
        :param filename: The name of the file to create and grow.
        :param interval: Time interval (in seconds) between automatic content additions.
        :param iterations: Number of times content will be added automatically.
        """
        self.filename = filename
        self.interval = interval
        self.iterations = iterations
        self.create_seed_file()

    def create_seed_file(self):
        """Creates an empty seed text file."""
        with open(self.filename, 'w') as file:
            file.write("Seed file created. Ready to grow...\n")
        print(f"Seed file '{self.filename}' created!")

    def generate_content(self):
        """Generates random content to simulate file growth."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(50))

    def add_content(self, content):
        """Adds content to the text file and simulates growth."""
        with open(self.filename, 'a') as file:
            file.write(content + "\n")
        print(f"Content added to '{self.filename}'.")

    def view_file_content(self):
        """Displays the current content of the file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                content = file.read()
            print(f"\nCurrent content of '{self.filename}':\n")
            print(content)
        else:
            print(f"File '{self.filename}' does not exist.")

    def file_size(self):
        """Returns the size of the file in bytes."""
        size = os.path.getsize(self.filename)
        print(f"The file size of '{self.filename}' is {size} bytes.")
        return size

    def grow_file_automatically(self):
        """Automatically grows the file by adding content at regular intervals."""
        print(f"Starting automatic file growth... Adding content every {self.interval} seconds.")
        for i in range(self.iterations):
            content = self.generate_content()
            self.add_content(content)
            self.file_size()  # Check the size of the file after each addition
            time.sleep(self.interval)
        print(f"File growth completed after {self.iterations} iterations.")

# Example of usage
if __name__ == "__main__":
    # Step 1: Create the automated FileFarm instance
    # Here we set a 3-second interval between updates and run it for 5 iterations
    farm = FileFarm("automated_file_farm.txt", interval=3, iterations=5)

    # Step 2: Start automatic growth
    farm.grow_file_automatically()

    # Step 3: View final file content
    farm.view_file_content()
