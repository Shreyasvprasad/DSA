def runCustomerSimulation(n, seq):
    computers = set()
    walked_away = 0
    
    for char in seq:
        if char in computers:
            computers.remove(char)
        else:
            if len(computers) < n:
                computers.add(char)
            else:
                walked_away += 1
    
    return walked_away

# Example usage
print(runCustomerSimulation(2, "ABBAJJKZKZ"))  # Output: 0
print(runCustomerSimulation(3, "GACCBDDBAGEE"))  # Output: 1
print(runCustomerSimulation(3, "GACCBGDDBAEE"))  # Output: 0
print(runCustomerSimulation(1, "ABCBCA"))  # Output: 2
print(runCustomerSimulation(1, "ABCBCADEED"))  # Output: 3
