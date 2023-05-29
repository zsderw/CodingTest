def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        if A[i] < B[i]:
            answer += 1
        else:
            for j in range(i + 1, len(A)):
                if A[i] < B[j]:
                    answer += 1
                    t = B[j]
                    B[j] = B[i]
                    B[i] = t
                    break
    return answer