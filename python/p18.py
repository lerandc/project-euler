"""
Luis RD
April 11, 2020

------------------------------------------------

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle in problem18.txt
"""
import time

def generateTriangle(height):
    """
    generate an integer sequenced triangle of arbitrary height
    """
    triangle = []
    count = 1
    for i in range(0,height):
        triangle.append([])
        for j in range(0,i+1):
            triangle[i].append(count)
            count += 1

    return triangle

def triangleSequence(height):
    """
    Get sequence of maximally sized recursive triangles
    """
    N = 3
    sequence = [3]
    while(2*N < height):
        N += N-1
        sequence.append(N)
    return sequence

def getNewTriangle(triangle,s_idx,j):
    """
    Pruning operation
    """
    new_triangle = []
    for i in range(s_idx,len(triangle)):
        new_triangle.append([])
        for jj in range(j,j+i-s_idx+1):
            new_triangle[i-s_idx].append(triangle[i][jj])

    return new_triangle

def recursiveTriSum(triangle,sequence):
    """
    Implementation of rough algorithm to subdivide the triangle into pieces
    and track maximum sum of regions, updating the bottom row

    Triangle input is list of lists, where top row is 1 element,
    and Nth row is N elements
    """
    if len(triangle) == 3: #end of recursion, only 4 paths to evaluate
        mid = [i+triangle[0][0] for i in triangle[1]]
        bot = triangle[2]
        vals = [mid[0]+bot[0],mid[0]+bot[1],mid[1]+bot[1],mid[1]+bot[2]]
        return max(vals)

    #if not smallest recursion element, find biggest recursive triangle
    seq_hold = [i for i in sequence if i < len(triangle)]
    if len(seq_hold) == 0:
        if len(triangle) == 2:
            return max(triangle[1])+triangle[0][0]
        print("Exiting.")
        exit()
    prune = max(seq_hold)

    s_idx = len(triangle)-prune
    for j in range(0,s_idx+1):
        new_triangle = getNewTriangle(triangle,s_idx,j)
        triangle[s_idx][j] = recursiveTriSum(new_triangle,sequence)

    del triangle[s_idx+1:]
    
    #want to collapse all the way to three high triangle
    return recursiveTriSum(triangle,sequence)

def readTriangle(filepath):
    """
    Read triangle from text file into list of lists
    """
    triangle = []
    with open(filepath) as file:
        line = file.readline()
        while(len(line) > 0):
            line = line.strip('\n')
            line = line.split(' ')
            line = [int(s) for s in line]
            triangle.append(line)
            line = file.readline()
            
    return triangle

def main():
    tic = time.perf_counter()
    triangle = readTriangle("p067_triangle.txt")
    sequence = triangleSequence(len(triangle))
    print(recursiveTriSum(triangle,sequence))

    # for i in range(3,51):
    #     triangle = generateTriangle(i)
    #     sequence = triangleSequence(len(triangle))
    #     print(recursiveTriSum(triangle,sequence))
    toc = time.perf_counter()
    print("Recursive algorithm finished in: ", toc-tic, " seconds")

if __name__ == '__main__':
    main()