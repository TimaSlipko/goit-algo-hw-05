def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    i = 0
    upper = None

    while left <= right:
        i += 1
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return i, mid_val

        if mid_val < target:
            left = mid + 1
        else:
            upper = mid_val
            right = mid - 1

    return i, upper

def main():
    arr = [0.5, 1.2, 2.3, 3.7, 5.0, 8.4]
    print(binary_search(arr, 3.0))
    print(binary_search(arr, 0.5))

if __name__ == '__main__':
    main()