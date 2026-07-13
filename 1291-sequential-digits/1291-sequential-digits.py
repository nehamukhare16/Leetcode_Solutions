class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # String containing digits in increasing order.
        digits = "123456789"

        # Store valid sequential numbers
        result = []

        # Try every possible length
        for length in range(2, 10):

            # Slide window of size 'length'
            # across the digits string
            for start in range(10 - length):

                # Extract the sequential substring
                number = int(digits[start:start + length])

                # Keep only numbers inside the given range
                if low <= number <= high:
                    result.append(number)

        return result


        