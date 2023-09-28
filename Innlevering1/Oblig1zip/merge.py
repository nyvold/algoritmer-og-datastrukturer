from countswaps import CountSwaps


class merge:
    #hjelpermetode for mergesort
    def merge_arrays(A1, A2, A):
        i = 0
        j = 0
        while i < len(A1) and j < len(A2):
        # her en plass ville jeg telt swaps
            if A1[i] <= A2[j]:
                A[i + j] = A1[i]
                i = i + 1
            else:
                A[i + j] = A2[j]
                j = j + 1
        while i < len(A1):
            A[i + j] = A1[i]
            i = i + 1
        while j < len(A2):
            A[i + j] = A2[j]
            j = j + 1
        return A
    
    def sort(A):
        if len(A) <= 1:#basistilfelle
            return A
        i = len(A) // 2
        A1 = merge.sort(A[:i])
        A2 = merge.sort(A[i:])
        return merge.merge_arrays(A1, A2, A)#rekursivt kall
    
    def __str__(self):
        return "Algoritme: merge"

# def main():
#     arr = [8, 9, 6, 7, 4, 5, 2, 3, 10, 1] 

#     assert merge.sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print("merge test ok")


# main()