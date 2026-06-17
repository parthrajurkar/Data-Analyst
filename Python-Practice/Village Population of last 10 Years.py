# The Current population of a village is 10000.The Population of the Village is increasing
# at the rate of 10% per year.You have to write a program to find out the population at
# the end of each of the last 10 years


curr_pop=10000

for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop=curr_pop/1.1