"""
Fibonacci Sequence Generator
----------------------------
This script provides a clean implementation of the Fibonacci series 
for use in algorithm analysis and project management tools.
"""

def generate_fibonacci(limit):
    """
    Generates a Fibonacci sequence up to a specified number of terms.
    
    Args:
        limit (int): How many numbers to generate.
        
    Returns:
        list: A list containing the Fibonacci sequence.
    """
    # Validation: Ensure the input is a positive integer
    if limit <= 0:
        return []
    
    # Initialize the sequence with the first two terms
    sequence = [0, 1]
    
    # Loop to calculate the next terms based on the sum of previous two
    while len(sequence) < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
        
    # Return only the requested number of elements
    return sequence[:limit]

if __name__ == "__main__":
    # Example usage for a real-world scenario (e.g., Agile Story Points)
    terms = 10
    fib_list = generate_fibonacci(terms)
    
    print(f"Fibonacci Sequence ({terms} terms):")
    print(fib_list)
