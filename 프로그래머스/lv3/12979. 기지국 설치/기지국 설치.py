def solution(n, stations, w):
    answer = 0
    
    for st in stations:
        if stations[0] == st:
            no = st - 1 - w
            answer += no // (2 * w + 1)
            bf = st + w
            print(st, "first")
            if no % (2 * w + 1) != 0:
                answer += 1
                print(answer)
        else:
            no = st - 1 - bf - w
            answer += no // (2 * w + 1)
            print(answer)
            bf = st + w
            print(st, "sec")
            if no % (2 * w + 1) != 0:
                answer += 1
    if stations[-1] != n:
        af = stations[-1] + w
        if n - af > 0:
            answer += (n - af) // (2 * w + 1)
            print(answer)
            if (n - af) % (2 * w + 1) != 0:
                answer += 1
                print(answer)
    
    
    
    
    
    
    
    
#     apt = [0] * n
#     s = 0
    
#     for st in stations:
#         if stations[-1] == st:
#             if n - st + w <= n:
#                 answer += (st - w - s) // (2 * w + 1)
#                 if (st - w - s) % (2 * w + 1) != 0:
#                     answer += 1
#         answer += (st - w - s) // (2 * w + 1)
#         if (st - w - s) % (2 * w + 1) != 0:
#             answer += 1
#         s = st + w
        
#     for st in stations:
#         idx = st - 1
#         apt[idx] = 1
#         for i in range(1, w + 1):
#             if idx - i >= 0:
#                 apt[idx - i] = 1
#             if idx + i <= len(apt) - 1:
#                 apt[idx + i] = 1
    
#     index = 0
#     l = [0] * n
#     for i in apt:
#         if i == 0:
#             l[index] += 1
#         if i == 1:
#             index += 1
#     net = 2 * w + 1
#     for j in l:
#         if j != 0:
#             answer += j // net
#             if j % net != 0:
#                 answer += 1
    
    return answer