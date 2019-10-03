def count_positives_sum_negatives(arr):
    positive = []
    negative = 0
    if len(arr) == 0:
        return []
    else:
        for i in arr:
            if i > 0:
                positive.append(i)
            elif i < 0:
                negative = negative + i
        return [len(positive),negative]



print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

