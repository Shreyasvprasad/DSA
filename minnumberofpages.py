def is_possible(books, n, m, min_pages):
    students = 1
    pages_allocated = 0
    
    for i in range(n):
        if books[i] > min_pages:
            return False
        
        if pages_allocated + books[i] > min_pages:
            students += 1
            pages_allocated = books[i]
            if students > m:
                return False
        else:
            pages_allocated += books[i]
    
    return True

def allocate_books(books, n, m):
    if n < m:
        return -1
    
    total_pages = sum(books)
    low = max(books)
    high = total_pages
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(books, n, m, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result

# Example usage
n = int(input("Enter the number of books: "))
books = list(map(int, input().split()))
m = int(input("Enter the number of students: "))
result = allocate_books(books, n, m)
print("Minimum number of pages allocated:", result)
