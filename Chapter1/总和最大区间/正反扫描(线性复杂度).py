from numpy import array


array1 = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]
array2 = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -62.2, 44.2, 5.4, -7.8, 1.1, -4.9]

def find_max_subarray_v1(a):
    max_sum = max(a)
    length = len(a)
    if (length < 2):
        return a
    elif max_sum <= 0:
        return max_sum
    else:
        # right side
        for i in range(length):
            right_side = i
            right_sum = a[i]
            right_array = [a[i]]
            if a[i] <= 0:
                continue
            else:
                for j in range(i+1, length):
                    sum_hat = sum(a[i: j])
                    if sum_hat > right_sum:
                        right_sum = sum_hat
                        right_side = j
                        right_array = a[i: j]
            break
        print(right_sum, right_side, right_array)
                        
        # left side
        for i in range(length-1, -1, -1):
            left_side = i
            left_sum = a[i]
            left_array = [a[i]]
            if a[i] <= 0:
                continue
            else:
                for j in range(i-1, -1, -1):
                    sum_hat = sum(a[j: i+1])
                    if sum_hat > left_sum:
                        left_sum = sum_hat
                        left_side = j
                        left_array = a[j: i+1]
            break
        print(left_sum, left_side, left_array)
        
        if left_side == right_side:
            return left_array
        else:
            return a[left_side: right_side]

result = find_max_subarray_v1(array1)
print(result)

def find_max_subarray_v2(a):
    max_sum = max(a)
    length = len(a)
    if (length < 2):
        return a
    elif max_sum <= 0:
        return max_sum
    else:
        # right side
        for i in range(length):
            max = [a[i]]
            max_sum = a[i]
            if a[i] <= 0:
                continue
            else:
                for j in range(i+1, length):
                    if sum(a[i: j+1]) > 0:
                        continue
                    else:
                        max_hat = find_max_subarray_v1(a[i: j])
                        max_hat_sum = sum(max_hat)
                        if max_hat_sum > max_sum:
                            max = max_hat
                            max_sum = max_hat_sum
                        

                        

                
            break
        print(right_sum, right_side, right_array)
                        
        # left side
        for i in range(length-1, -1, -1):
            left_side = i
            left_sum = a[i]
            left_array = [a[i]]
            if a[i] <= 0:
                continue
            else:
            break
        print(left_sum, left_side, left_array)
        
        if left_side == right_side:
            return left_array
        else:
            return a[left_side: right_side]
    


            
                    



