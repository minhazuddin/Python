def median(values):
    if len(values) % 2 == 0:
      median = ((values[(int(len(values) / 2)) - 1] + values[(int(len(values) / 2))]) / 2)
    else:
      median = values[(int(len(values) / 2))]
    return median


a = median([1, 6, 4, 3, 5, 6, 7, 8, 9, 10])
print(a)