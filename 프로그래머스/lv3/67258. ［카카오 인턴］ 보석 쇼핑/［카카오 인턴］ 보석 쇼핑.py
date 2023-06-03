def solution(gems):
    answer = []
    jewelry = set(gems)
    num_jewelry = len(jewelry)
    
    if len(jewelry) == 1:
        return [1, 1]
    
    start, end = 0, 0
    jewelry_counts = {}
    shortest_length = float('inf')
    
    while end < len(gems):
        if gems[end] not in jewelry_counts:
            jewelry_counts[gems[end]] = 1
        else:
            jewelry_counts[gems[end]] += 1
        
        end += 1
        
        if len(jewelry_counts) == num_jewelry:
            while start < end:
                if jewelry_counts[gems[start]] > 1:
                    jewelry_counts[gems[start]] -= 1
                    start += 1
                elif shortest_length > end - start:
                    shortest_length = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break
    
    return answer
