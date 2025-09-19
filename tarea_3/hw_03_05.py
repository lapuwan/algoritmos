


def operations(numbers):
    results = []        # T(n) = 1
    
    for number in numbers:      # T(n) = n
        count = 0       # T(n) = 1
        while number >= 1:      # T(n) = log_2(n)
            number /= 2     # T(n) = 1
            count += 1      # T(n) = 1
        results.append(count)       # T(n) = 1
    
    return results      # T(n) = 1
