import math
def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    cur_instances = instances
    i = 0

    while i < len(averageUtil):
        if averageUtil[i] < 25 and cur_instances > 1:
            cur_instances = math.ceil(cur_instances / 2)
            i+=11
            continue
        elif averageUtil[i] > 60 and cur_instances *2 <= 2*math.pow(10,8):
            cur_instances *= 2
            i+=11
            continue
        i+=1
    return cur_instances