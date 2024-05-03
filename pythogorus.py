def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer():
                triplets.append((a, b, int(c)))
    return triplets

# Example usage
limit = int(input("Enter the limit: "))
triplets = generate_pythagorean_triplets(limit)
print("Pythagorean triplets within the limit:", triplets)
        