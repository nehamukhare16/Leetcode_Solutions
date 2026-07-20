class Solution:
    def shiftGrid(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols

        # If k is larger than the number of elements,
        # shifting by total elements brings the grid back to the same state.
        k = k % total

        result = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # Convert (row, col) to a 1D index
                current_index = row * cols + col

                # Calculate the new index after shifting
                new_index = (current_index + k) % total

                # Convert the new 1D index back to (row, col)
                new_row = new_index // cols
                new_col = new_index % cols

                # Place the element in its new position
                result[new_row][new_col] = grid[row][col]

        return result