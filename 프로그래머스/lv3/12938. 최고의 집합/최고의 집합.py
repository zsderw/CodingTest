def solution(n, s):
    answer = []
    l = []
    if s < n:
        return [-1]
    else:
        answer = [s // n] * n
        print(answer)
        for i in range(s % n):
            answer[len(answer) - i - 1] += 1
        
    return answer