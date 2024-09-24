# Tagus image script 

### input file
create txt file with rgb values... cannot upload the file to the git because of its size

### traversing the matrix

    [[1,1,1], [2,2,2], [3,3,3]],

    [[4,4,4], [5,5,5], [6,6,6]],

    [[7,7,7], [8,8,8], [9,9,9]]

**diagonal_traverse:**
the algoritm should traserse the matrix in this order: 

`[1,1,1], [2,2,2], [4,4,4], [3,3,3], [5,5,5], [7,7,7], [6,6,6], [8,8,8], [9,9,9]`

**diagonal_traverse_other_way:**
the algoritm should traserse the matrix in this order: 

`
[1, 1, 1]
[4, 4, 4]
[2, 2, 2]
[7, 7, 7]
[5, 5, 5]
[3, 3, 3]
[8, 8, 8]
[6, 6, 6]
[9, 9, 9]
`