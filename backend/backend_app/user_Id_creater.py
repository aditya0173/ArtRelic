import os

class UserIDGenerator:
    def __init__(self, start=1, storage_file="user_id_counter.txt"):
        self.storage_file = storage_file
        self.current_id = self._load_last_id() if os.path.exists(storage_file) else start

    def _load_last_id(self):
        """Load the last used ID from the file."""
        with open(self.storage_file, "r") as file:
            return int(file.read().strip(), 16)

    def _save_current_id(self):
        """Save the current ID to the file."""
        with open(self.storage_file, "w") as file:
            file.write(hex(self.current_id)[2:])

    def generate_user_id(self):
        """Generate the next user ID as a hexadecimal number."""
        user_id = f"{self.current_id:04x}"  # Ensures 4-character hex format (e.g., 0001, 0002, etc.)
        self.current_id += 1
        self._save_current_id()
        return user_id

# Example Usage
if __name__ == "__main__":
    generator = UserIDGenerator()
    print(generator.generate_user_id())  # Output: 0001
    print(generator.generate_user_id())  # Output: 0002
