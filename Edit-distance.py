#######################################
# Edit-distance
#######################################

def initialize_distance_matrix(str1, str2):
    """
    Initializes the distance matrix based on the lengths of the two strings.
    The first row and first column are filled with incremental values.
    """
    m, n = len(str1), len(str2)
    D = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

    # Filling the first row and column
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j
    
    return D

def compute_edit_distance(D, str1, str2):
    """
    Fills in the distance matrix based on the edit distance algorithm.
    Computes the minimum operations required to convert str1 to str2.
    """
    m, n = len(str1), len(str2)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                diff = 0
            else:
                diff = 1
            D[i][j] = min([
                D[i - 1][j] + 1,  # Delete from str1
                D[i][j - 1] + 1,  # Insert into str1
                D[i - 1][j - 1] + diff  # Replace
            ])
    
    return D

def reconstruct_operations(D, str1, str2):
    """
    Reconstructs the sequence of operations (insert, delete, replace)
    that transforms str1 into str2 based on the filled distance matrix D.
    """
    i, j = len(str1), len(str2)
    operations = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and (str1[i - 1] == str2[j - 1] or D[i][j] == D[i - 1][j - 1] + 1):
            if str1[i - 1] != str2[j - 1]:
                operations.append(f"Replace {str1[i - 1]} with {str2[j - 1]}")
            i -= 1
            j -= 1
        elif i > 0 and D[i][j] == D[i - 1][j] + 1:
            operations.append(f"Delete {str1[i - 1]}")
            i -= 1
        else:
            operations.append(f"Insert {str2[j - 1]}")
            j -= 1

    operations.reverse()  # Reverse the operations to show them in the correct order
    return operations

def editDistance(str1, str2, showSolution=False):
    """
    Computes the edit distance between two strings and returns both
    the distance and the operations required to convert str1 into str2.
    """
    # Step 1: Initialize the distance matrix
    D = initialize_distance_matrix(str1, str2)

    # Step 2: Compute the edit distance by filling the matrix
    D = compute_edit_distance(D, str1, str2)
    if not showSolution:
        print(f"Edit distance = {D[len(str1)][len(str2)]}")
        return
    # Step 3: Reconstruct the sequence of operations
    operations = reconstruct_operations(D, str1, str2)

    # Output the results
    print(f"Edit distance = {D[len(str1)][len(str2)]}")
    print("Operations:")
    for op in operations:
        print(op)

    
editDistance("ponedeljek", "petek", showSolution=True)
