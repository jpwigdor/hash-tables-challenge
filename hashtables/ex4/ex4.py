def has_negatives(a):
    has_negatives_num = {}

    for num in a:
        has_negatives_num[num] = -num

    result = []

    for num in has_negatives_num.keys():
        if num > 0 and has_negatives_num[num] in has_negatives_num:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
