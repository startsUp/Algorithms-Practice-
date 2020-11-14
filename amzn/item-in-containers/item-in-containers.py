def calculate(s, starts, ends):
    result = []
    mem = []
    count = 0
    for char in s:
        if char == '|':
            mem.append(count)
            count += 1
        else:
            mem.append("*")

    #print(mem)
    for i in range(len(starts)):
        start = starts[i]-1
        end = ends[i]-1

        while start < end and start < len(s) and mem[start] == "*":
            start += 1
        while start < end and end >= 0 and mem[end] == "*":
            end -= 1

        if start >= len(s) or end < 0:
            result.append(0)
        else:
            try:
                result.append((end - start) - (mem[end] - mem[start]))
            except TypeError:
                result.append(0)
    return result
