from countswaps import CountSwaps

class insertion:

    def sort(A):
        for i in range(len(A)):
            j = i
            while j > 0 and A[j-1] > A[j]:
                A.swap(j-1, j)
                j -= 1
        return A