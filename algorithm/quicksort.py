def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = []
    right = []
    pivots = []
    for el in array:
        if pivot > el:
            left.append(el)
        elif pivot < el:
            right.append(el)
        else:
            pivots.append(el)
    result_left = quickSort(left)
    result_right = quickSort(right)

    result = result_left + pivots + result_right

    return result 

def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()
