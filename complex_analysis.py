"""
Test file for inline PR review functionality.
This file contains various code patterns to test HarperBot's analysis.
"""

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total


def find_duplicate(numbers):
    """Find the first duplicate in a list."""
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None


def process_data(data):
    """Process data with some intentional issues."""
    # Missing validation
    if data is None:
        return None
    
    # Inefficient string concatenation
    result = ""
    for item in data:
        result = result + str(item) + ","
    
    # Unnecessary else after return
    if len(result) > 0:
        return result[:-1]
    else:
        return ""


class DataProcessor:
    """A class to process data."""
    
    def __init__(self):
        self.data = []
    
    def add_item(self, item):
        """Add an item to the data list."""
        self.data.append(item)
    
    def get_summary(self):
        """Get a summary of the data."""
        if not self.data:
            return "No data"
        
        summary = "Items: "
        for i, item in enumerate(self.data):
            summary += f"{i}: {item}, "
        
        return summary[:-2]  # Remove trailing comma and space


# Main execution
if __name__ == "__main__":
    # Test the functions
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum: {calculate_sum(numbers)}")
    print(f"Duplicate: {find_duplicate([1, 2, 3, 2, 4])}")
    
    processor = DataProcessor()
    processor.add_item("Apple")
    processor.add_item("Banana")
    print(f"Summary: {processor.get_summary()}")
