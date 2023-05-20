data = ['ab133', 'bb4', 'xy111', 'pq10']

for v in sorted(data, key=lambda v: int(v[2:])):
    print(v)
