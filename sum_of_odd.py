my_list = [1, 2, 3, 4, 5]

def addition(lst):
  return sum(num for num in lst if num % 2 != 0)

print (addition(my_list))