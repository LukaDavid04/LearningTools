import math

def median_finding_algorithm(DB1, DB2, n):
    p1 = p2 = n // 2  # Initialize query pointers to the middle of each database

    for i in range(2, int(math.log2(n)) + 1):
        m1 = query_database(DB1, p1)  # Query the median of DB1
        m2 = query_database(DB2, p2)  # Query the median of DB2

        if m1 > m2:
            # Next time, query the median of the upper half of DB1 and the lower half of DB2
            p1 -= n // (2 ** i)
            p2 += n // (2 ** i)
        else:
            # Next time, query the median of the lower half of DB1 and the upper half of DB2
            p1 += n // (2 ** i)
            p2 -= n // (2 ** i)

    # After the loop, return the minimum of m1 and m2
    m1 = query_database(DB1, p1)  # Query the median of DB1
    m2 = query_database(DB2, p2)
    
    if m1 > m2:
        # Next time, query the median of the upper half of DB1 and the lower half of DB2
        return max(m1, m2)
    else:
        # Next time, query the median of the lower half of DB1 and the upper half of DB2
        return max(m1, m2)

def median_finding_algorithm2(DB1, DB2, n):
    p1 = p2 = n // 2  # Initialize query pointers to the middle of each database

    for i in range(2, int(math.log2(n)) + 1):
        m1 = query_database(DB1, p1)  # Query the median of DB1
        m2 = query_database(DB2, p2)  # Query the median of DB2

        if m1 > m2:
            # Next time, query the median of the upper half of DB1 and the lower half of DB2
            DB1.remove(DB1.index[p1:])    
            DB2.remove(DB2.index[:p2])
        else:
            # Next time, query the median of the lower half of DB1 and the upper half of DB2
            for j in range(i + 1, n):
                DB1.remove(DB1.index[p1])
                DB2.remove(DB2.index[p2])

    # After the loop, return the minimum of m1 and m2
    return min(m1, m2)


def query_database(database, k):
    # Assuming 'database' is a list, you would return the kth smallest element
    # (Note: Python uses 0-based indexing, so adjust the index accordingly)
    return sorted(database)[k]

# Example usage:
DB1 = [3, 8, 4, 6, 14]  # Replace with your actual database
DB2 = [5, 2, 7, 9, 10]  # Replace with your actual database

DB1.sort()
DB2.sort()

result = median_finding_algorithm(DB1, DB2, 5)
print("Median:", result)
