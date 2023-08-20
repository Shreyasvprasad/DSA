def find_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    result = []

    def dfs(x, y, index, path):
        if index == len(word):
            result.append(path)
            return

        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != word[index]:
            return

        original_char = grid[x][y]
        grid[x][y] = "#"  # Mark the cell as visited

        for dx, dy in directions:
            dfs(x + dx, y + dy, index + 1, path + [(x, y)])

        grid[x][y] = original_char  # Backtrack

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                dfs(i, j, 0, [])

    return result

# Example usage
grid = [
    ['a', 'b', 'c', 'd'],
    ['a', 'r', 'a', 's'],
    ['a', 'c', 'o', 't']
]
word = "car"
result = find_word_in_grid(grid, word)
print("Occurrences of the word:", result)
