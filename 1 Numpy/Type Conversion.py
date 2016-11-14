import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr.dtype)

print(hex(id(arr)))
print(hex(id(float_arr)))  # not same

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(hex(id(arr)))
print(arr.dtype)

arr = arr.astype(np.int32)
print(arr)
print(hex(id(arr)))  # address is same, means the previous one is replaced and no memory loss
print(arr.dtype)

string_arr = np.array(arr, dtype=np.str)  # ['3' '-1' '-2' '0' '12' '10']
print(string_arr)

string_arr = np.array(arr, dtype=np.string_)  # [b'3' b'-1' b'-2' b'0' b'12' b'10']
print(string_arr)

numeric_str = np.array(string_arr, dtype=np.int32)
print(numeric_str)
