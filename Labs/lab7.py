import numpy as np

# # Printing matrices using NumPy:

# # Convert a list of lists into an array:
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# M = np.array(M_listoflists)
# # Now print it:
# print(M)




# #Compute M*x for matrix M and vector x by using
# #dot. To do that, we need to obtain arrays
# #M and x
# M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
# x = np.array([75,10,-11])
# b = np.matmul(M,x)        

# print(M)
# #[[ 1 -2  3]
# # [ 3 10  1]
# # [ 1  5  3]]

# # To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist() 

# print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]


# Problem 1
def print_matrix(M_lol):
    x = np.array(M_lol)
    print(x)

# Problem 2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

# Problem 3
def get_row_to_swap(M, start_i):
    min = get_lead_ind(M[start_i])
    row = start_i
    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < min:
            min = get_lead_ind(M[i])
            row = i
    return row

# Problem 4
def add_row_coefs(r1, c1, r2, c2):
    for i in range(len(r1)):
        r1[i] *= c1
    for i in range(len(r2)):
        r2[i] *= c2
    r = [0]*max(len(r1),len(r2))
    for i in range(len(r)):
        r[i] += r1[i] + r2[i]
    return r

# Problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    x = M[row_to_sub][best_lead_ind]
    for i in range(row_to_sub+1, len(M)):
        c = (M[i][best_lead_ind]/x)
        for k in range(len(M[0])):
            M[i][k] -= c*M[row_to_sub][k]
    return M

# Problem 6
def forward_step(M):
    for i in range(len(M)): # i is row number
        # first row with nonzero
        print("Now looking at row", i)
        r_swap = get_row_to_swap(M,i)
        print("Swapping rows",i, "and", r_swap, "so that entry 0 in the current row is non-zero")

        for k in range(len(M[i])): # k is column of row
            temp = M[i][k]
            M[i][k] = M[r_swap][k]
            M[r_swap][k] = temp

        print("The matrix is currently:")
        print_matrix(M)

        elim_col = len(M[0])
        for k in range(i,len(M)):
            temp = get_lead_ind(M[k])
            # print("temp",temp)
            # print("elim_col",elim_col)
            if temp < elim_col:
                elim_col = temp
        print("Adding row", i, "to rows below it to eliminate coefficients in column", elim_col)
        print("The matrix is currently:")
        print_matrix(M)
        
        # adding multiples to lower rows
        # for k in range(i + 1,len(M)): # k is rows from row after i to last row in M
        #     # print(M)
        M = eliminate(M, i, elim_col)

    return M

def backward_step(M):
    for row_to_sub in range(len(M)-1,-1,-1):
        best_lead_ind = get_lead_ind(M[row_to_sub])
        for i in range(row_to_sub - 1, -1, -1):
            x = M[row_to_sub][best_lead_ind]
            c = (M[i][best_lead_ind]/x)
            for k in range(len(M[0])):
                M[i][k] -= c*M[row_to_sub][k]
        print_matrix(M)
    for row in range(len(M)):
        row_lead_ind = get_lead_ind(M[row])
        x = M[row][row_lead_ind]
        for col in range(len(M[row])):
            M[row][col] /= x
        print_matrix(M)
    return M

# Problem 8
def solve(M,b):

    x = []

    for i in range(b):
        x.append(0)

    for row in range(M):
        M[row].append(b[row])
    
    M = forward_step(M)
    M = backward_step(M)

    print_matrix(M)



    return x

if __name__ == "__main__":
    M = [[  1.,  -2.,   3.,  22.],
[3.,10.,1., 314.],
 [  1.,   5.,   3.,  92.]]
    M = np.array(M)
    print_matrix(M)
    # print(get_row_to_swap(M,1))
    # print(add_row_coefs([1,2,3],2,[2,3,4],3))
    # print(eliminate(M, 1,2))
    # solve(M, )