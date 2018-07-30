import time 

def gaussian_sum(number):
    return number * (number + 1) / 2 

	#return gaussian_sum(end) - gaussian_sum(start) + start
					

def simple_minded_sum(number):
    sum = 0
    for i in range(number+1):
       sum += i
    return sum 

def add_zero(number):
    return number + 0

#### time the difference between the gaussian_sum and simple_minded_sum for number = [10, 100, 10000, 900000]

a_list = [100000, 300000, 600000, 900000]
for var in a_list:
	print(var)
	start = time.time()
	gaussian_sum(var)
	end = time.time()
	g_time = end - start
	start = time.time()
        simple_minded_sum(var)
        end = time.time()
        simple_minded_sum_time = end - start
	print(var, g_time, simple_minded_sum_time

