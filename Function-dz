#1
def my_sum(arr: list[float | int]) -> float | int:
    a=0
    for i in arr:
        a+=i
    return a

#2
def my_avg(arr: list[float | int]) -> float | int:
    d=0
    a=0
    for i in arr:
        a+=i
        d+=1
    if d==0:
        return 0
    return a/d

#3
def my_min(arr: list[float | int]) -> float | int:
    if not arr:
        return None
    minn = arr[0]
    for i in arr:
        if i < minn:
            minn = i
    return minn


#4
def my_max(arr: list[float | int]) -> float | int:
    if not arr:
        return None
    maxx = arr[0]
    for i in arr:
        if i > maxx:
            maxx = i
    return maxx

#5
def my_max_filter(arr: list[float | int], num: float | int) -> list[float | int]:
    result = []
    for i in arr:
        if i > num:
            result.append(i)
    return result


