def solution(operations):
    answer = []
    l = []
    for op in operations:
        oper, num = op.split(' ')
        num = int(num)
        if oper == 'I':
            l.append(num)
        elif oper == 'D' and num == 1:
            if len(l) == 0:
                continue
            l.remove(max(l))
        else:
            if len(l) == 0:
                continue
            l.remove(min(l))
    if len(l) == 0:
        answer = [0, 0]
    else:
        answer = [max(l), min(l)]
    return answer