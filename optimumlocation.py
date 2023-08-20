import math

def find_point_on_line_with_min_distance(points, a, b, c):
    n = len(points)
    
    # Calculate the centroid of the points
    x_sum = sum(point[0] for point in points)
    y_sum = sum(point[1] for point in points)
    x_centroid = x_sum / n
    y_centroid = y_sum / n
    
    # Calculate the perpendicular distance from centroid to the line
    distance = abs(a * x_centroid + b * y_centroid + c) / math.sqrt(a**2 + b**2)
    
    return x_centroid, y_centroid

# Example usage
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
a = 2
b = -3
c = 5
x_centroid, y_centroid = find_point_on_line_with_min_distance(points, a, b, c)
print("Point on the line with minimum distance:", (x_centroid, y_centroid))
