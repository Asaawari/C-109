import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics 

dice_result = []
count = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
stdDev = statistics.stdev(dice_result)

first_std_dev_start,  first_std_dev_end = mean-stdDev, mean+stdDev
second_std_dev_start,  second_std_dev_end = mean-(2*stdDev), mean+(2*stdDev)
third_std_dev_start,  third_std_dev_end = mean-(3*stdDev), mean+(3*stdDev)

list_of_data_within_first_std_dev = [result for result in dice_result if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_second_std_dev = [result for result in dice_result if result>second_std_dev_start and result<second_std_dev_end]
list_of_data_within_third_std_dev = [result for result in dice_result if result>third_std_dev_start and result<third_std_dev_end]

print(mean,median,mode)
print("Standard Deviation of this data is", stdDev)
print("{}% of data lies in First Standard Deviation".format(len(list_of_data_within_first_std_dev)*100.0/len(dice_result)))
print("{}% of data lies in Second Standard Deviation".format(len(list_of_data_within_second_std_dev)*100.0/len(dice_result)))
print("{}% of data lies in Third Standard Deviation".format(len(list_of_data_within_third_std_dev)*100.0/len(dice_result)))

fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()