import itertools

def compute_unfairness(lst):
    output = 0
    for index in range(len(lst)):
        for index2 in range(index+1,len(lst)):
            output += abs(lst[index]-lst[index2])
    return output

def output(input_list):
    LU = 0
    a = input_list[2:]
    values = []
    for i in xrange(1,input_list[0]+1):
        values.append(list(itertools.combinations(a,i)))

    for item in values[input_list[1]-1:]:
        for lst in item:
            unfairness = compute_unfairness(lst)
            if not LU:
                LU = unfairness
            elif LU > unfairness:
                LU = unfairness

    return LU

print output([10, 4, 1, 2, 3, 4, 10, 20, 30, 40, 100, 200])
