import numpy as np

a = np.array([1,2,3,4,5])
print("1d:\n",a)
print(f"shape={a.shape},ndim={a.ndim},size={a.size},dtype={a.dtype}")
newtype = a.astype(float)
print(f"After type change: shape={newtype.shape},ndim={newtype.ndim},size={newtype.size},dtype={newtype.dtype}")

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("2d:\n",b)
print(f"shape={b.shape},ndim={b.ndim},size={b.size},dtype={b.dtype}")

c = np.array([[[1,2,3],
               [4,5,6],
               [7,8,9]],
               [[10,11,12],
                [13,14,15],
                [16,17,18]],
                [[19,20,21],
                 [22,23,24],
                 [25,26,27]]])
print("3d:\n",c)
print(f"shape={c.shape},ndim={c.ndim},size={c.size},dtype={c.dtype}")

zero = np.zeros((3,4),dtype=int)
print("zero:\n",zero)

ones = np.ones((2,3), dtype=int)
print("ones:\n",ones)

full = np.full((3,4), 7, dtype=int)
print("full:\n",full)

empty = np.empty((2,3))
print("empty:\n",empty)

identity = np.eye(3, dtype=int)
print("identity:\n",identity)

arrange = np.arange(0,10,2)
print("arrange:\n",arrange)

linspace = np.linspace(0,1,5)
print("linspace:\n",linspace)


print("a+2:\n",a+2)
mul = np.dot(b,np.array([[2],[3],[4]]))
print("mul:\n",mul)
print("sqrt:\n",np.sqrt(a))

print("a[0]:\n",a[0])
print("b[:,1]:\n",b[:,1])

random = np.random.random((2,3))
print("randon:\n", random)
normal = np.random.normal(size=(3,3))
print("normal:\n", normal)
randint = np.random.randint(1,10,(2,3))
print("randint:\n", randint)


d = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

one_element = d[0,0]
print("one_element:\n",one_element)

row_element = d[0,:]
print("row_element:\n",row_element)

column_element = d[:,1]
print("column_element:\n",column_element)

element1 = d[0:2,1:3]
print('"[0:2,1:3]":\n',element1)

e = np.array([1,2,3,4,5])

element2 = e[1:4]
print('"[1:4]":\n', element2)

col_newaxis = e[:,np.newaxis]
print("column newaxis:\n",col_newaxis)

row_axis = e[np.newaxis,:]
print("row newaxis:\n",row_axis)


f = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

reshape = f.reshape((1,9))
print("reshape:\n",reshape)

reshaped = reshape.reshape((3,3))
print("reshaped:\n",reshaped)

g = np.array([[1,2,3],
              [4,5,6]])

h = np.array([[7,8,9],
              [10,11,12]])

concatinate0 = np.concatenate((g,h), axis=0)
print("concatinate 0:\n",concatinate0)

vstack = np.vstack((g,h))
print("vstack:\n",vstack)

concatinate1 = np.concatenate((g,h), axis=1)
print("concatinate 1:\n",concatinate1)

hstack = np.hstack((g,h))
print("hstack:\n",hstack)


i = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

split0 = np.split(i,3,axis=0)
print("split 0:\n",split0)

split1 = np.split(i,2,axis=1)
print("split 1:\n",split1)

array_split0 = np.array_split(i,2,axis=0)
print("array_split 0:\n",array_split0)

array_split1 = np.array_split(i,3,axis=1)
print("array_split 1:\n",array_split1)

j = np.array([[1,2,3],
              [4,5,6]])

k = np.array([[7,8,9],
              [10,11,12]])

stack0 = np.stack((j,k),axis=0)
print("stack 0:\n",stack0)

stack1 = np.stack((j,k),axis=1)
print("stack 1:\n", stack1)


l = np.array([1,2,3])

m = np.array([4,5,6])

n = np.array([7,8,9])

o = np.array([[1,2,3],
              [4,5,6]])

p = np.array([1,2,3,4,5])

q = np.array([0,np.pi/2,np.pi])

add = np.add(l,m)
print("add:\n",add)

multiply = np.multiply(l,n)
print("multiply:\n",multiply)

multiply2 = o*2
print("multiply times 2:\n",multiply2)

sum = np.sum(p)
print("sum:\n",sum)

mean = np.mean(p)
print("mean:\n",mean)

sin = np.sin(q)
print("sin:\n",sin)

exponent = np.exp(q)
print("exponent:\n",exponent)

r = np.array([1,2,3])

s = np.array([4,5,6])

array_plus = r+s
print("array + array:\n",array_plus)

array_multiply = r*s
print("array * array:\n",array_multiply)

t = np.array([1,2,3,4,5,6,7,8,9])

max_function = np.max(t)
print("max:\n",max_function)

min_function = np.min(t)
print("min:\n",min_function)

sum_function = np.sum(t)
print("sum:\n",sum_function)

mean_function = np.mean(t)
print("mean:\n",mean_function)

std_function = np.std(t)
print("std:\n",std_function)


u = np.array([[1,2,3],
              [4,5,6]])

sum0 = np.sum(u, axis=0)
print("sum 0:\n",sum0)

sum1 = np.sum(u, axis=1)
print("sum 1:\n",sum1)

max0 = np.max(u,axis=0)
print("max 0:\n", max0)

max1 = np.max(u,axis=1)
print("max 1:\n",max1)

mean0 = np.mean(u,axis=0)
print("mean 0:\n",mean0)

mean1 = np.mean(u,axis=1)
print("mean 1:\n",mean1)


v = np.array([1,2,3])

w = np.array([[4,5,6],
              [7,8,9]])

add_broadcast_number = v+2
print("add broadcast number:\n",add_broadcast_number)

add_broadcast_array = v+w
print("add broadcast array:\n",add_broadcast_array)


x = np.array([[1],
              [2],
              [3]])

y = np.array([4,5,6])

add_broadcast_array1 = x+y
print("add_broadcast_array1:\n",add_broadcast_array1)


array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

equal_elements = array1 == array2
print("Equal Elements:\n", equal_elements)

not_equal_elements = array1 != array2
print("Not Equal Elements:\n", not_equal_elements)

greater_than_elements = array1 > array2
print("Greater Than Elements:\n", greater_than_elements)

less_than_elements = array1 < array2
print("Less Than Elements:\n", less_than_elements)

greater_equal_elements = array1 >= array2
print("Greater Than or Equal Elements:\n", greater_equal_elements)

less_equal_elements = array1 <= array2
print("Less Than or Equal Elements:\n", less_equal_elements)


arr = np.array([True, True, False, True])

all_true = arr.all()
print("All True:\n", all_true)

any_true = arr.any()
print("Any True:\n", any_true)

count_true = arr.sum()
print("Count of True values:\n", count_true)


aa = np.array([[1, 2, 3], [4, 5, 6]])
scalar_value = 3

comparison_result = aa > scalar_value
print("Element-wise comparison with broadcasting (aa > 3):\n", comparison_result)


arr1 = np.array([True, True, False, False])
arr2 = np.array([True, False, True, False])

result_and = arr1 & arr2
print("Bitwise AND:\n", result_and)

result_or = arr1 | arr2
print("Bitwise OR:\n", result_or)

result_not = ~arr1
print("Bitwise NOT:\n", result_not)


arr3 = np.array([1, 2, 3, 4, 5])

print("Boolean mask:\n", arr3 > 3)
print("Masked Elements:\n", arr3[arr3 > 3])


print("Fancy Indexing")
arr = np.array([10, 20, 30, 40, 50])

indices = np.array([1, 3, 4])
result = arr[indices]
print(result)

condition = arr > 30
result = arr[condition]
print(result)

arr1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
row_indices = np.array([0, 1, 2])
col_indices = np.array([1, 2, 0])

result = arr1[row_indices, col_indices]
print(result)

arr[[1, 3, 4]] = 999
print(arr)

condition = arr > 30
arr[condition] = 999
print(arr)

arr1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
row_indices = np.array([0, 1, 2])
col_indices = np.array([1, 2, 0])
arr1[row_indices, col_indices] = 999
print(arr1)


arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Normal indexing and slicing:")
print(arr[1, 2])
print(arr[:, 1:3])

rows = np.array([0, 2])
cols = np.array([1, 3])
print("\nFancy indexing:")
print(arr[rows, cols])

print("\nCombine techniques:")
arr[0, 1:3] = 999
arr[:, [0, 2]] = 0
print(arr)


arr_2d = np.array([[3, 2, 1],
                   [6, 5, 4],
                   [9, 8, 7]])

sorted_arr_along_last_axis = np.sort(arr_2d)
print("Sorted along last axis:")
print(sorted_arr_along_last_axis)

sorted_arr_along_first_axis = np.sort(arr_2d, axis=0)
print("\nSorted along first axis:")
print(sorted_arr_along_first_axis)


print("argsort")
arr = np.array([3, 1, 2, 4, 5])
sorted_indices = np.argsort(arr)
sorted_arr = arr[sorted_indices]
print(sorted_indices)

print(sorted_arr)


arrs = np.array([1, 2, 2, 3, 4, 4, 5, 1, 5, 6])

unique_elements = np.unique(arrs)
print("Unique Elements:\n", unique_elements)

unique_elements, indices = np.unique(arrs, return_index=True)
print("Indices:\n", indices)

unique_elements, inverse_indices = np.unique(arrs, return_inverse=True)
print("Inverse Indices:\n", inverse_indices)

unique_elements, counts = np.unique(arrs, return_counts=True)
print("Counts:\n", counts)

arrw = np.array([1, 2, 3, 4, 5])
condition = arr > 3
result = np.where(condition, arrw, 0)
print("where:\n",result)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

resultm = np.matmul(A, B)
print("matmul:\n",resultm)
resulta = A @ B
print("@:\n",resulta)

A_inv = np.linalg.inv(A)
print("Matrix inverse:\n",A_inv)
