def binary(n):
    arr = []
    while (True):
        if n == 1 or n == 0:
            arr.append(n)
            break
        arr.append(n % 2)
        n = n // 2
    arr.reverse()
    
    return arr

def checkCnt(n):
    n = n - 1
    t = 2
    while(True):
        if (n < 0):
            return 0 # 포화트리 불만족
        if (n == 0):
            return 1 # 포화트리 만족
        n = n - t
        t = t * 2

def check(arr):
    global c
    if len(arr) < 3 or len(arr) % 2 == 0:
        return
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2 + 1:]
    m = (len(arr) // 2) // 2
    if ((left[m] == 1) or (right[m] == 1)) and arr[len(arr) // 2] == 0:
        c = c + 1 # c가 0보다 크면 안됨
        return
    check(left)
    check(right)
    
def solution(numbers):
    answer = [0 for i in range(len(numbers))]
    
    for i in range(len(numbers)):
        # 이진수 변환
        numbers[i] = binary(numbers[i])
        # 최초로 나온 1이 중심일 때까지 앞에다가 0붙여주기(이진수의 길이는 짝수면 안되고, 루트노드는 0이면 안되고, 이진수 길이가 포화노드 만족해야하고, 부모노드가 0인데 자식노드가 1이면 안됨
        lenBin = len(numbers[i])
        k = 0
        while True:
            global c
            c = 0
            check(numbers[i])
            if checkCnt(len(numbers[i])) == 1 and c == 0 and numbers[i][len(numbers[i]) // 2] == 1:
                answer[i] = 1
                break
            if k == lenBin - 1:
                break
            k = k + 1
            numbers[i].insert(0, 0)
    return answer
