def solution(sequence):
    answer = 0
    lenS = len(sequence)
    seq = [ sequence[i] if i % 2 == 0 else -1 * sequence[i] for i in range(lenS) ]
    seq2 = [ sequence[i] if i % 2 != 0 else -1 * sequence[i] for i in range(lenS) ]
    
    
    if seq[0] < 0:
        seq[0] = 0
    for i in range(1, len(seq)):
        if seq[i - 1] + seq[i] >= 0:
            seq[i] += seq[i - 1]
        else:
            seq[i] = 0
    if seq2[0] < 0:
        seq2[0] = 0
    for i in range(1, len(seq2)):
        if seq2[i - 1] + seq2[i] >= 0:
            seq2[i] += seq2[i - 1]
        else:
            seq2[i] = 0
                
    answer = max(max(seq), max(seq2))
    return answer