def find_min_max(numbers):
    """
    Find the minimum and maximum values in a list using inner functions.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        tuple: Minimum and maximum values in the list.
    """

    def find_min():
        """Find the minimum value in the list."""
        return min(numbers) if numbers else None

    def find_max():
        """Find the maximum value in the list."""
        return max(numbers) if numbers else None

    return find_min(), find_max()


if __name__ == '__main__':
    result = find_min_max([1, 2, 3, 4, 5])
    print(result)  # Sollte (1, 5) zurückgeben
