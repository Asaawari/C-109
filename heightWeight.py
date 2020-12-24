import pandas as pd 
import csv
import statistics

data = pd.read_csv("height-weight.csv")

height_list = data["Height(Inches)"].to_list()
weight_list = data["Weight(Pounds)"].to_list()

heightMean = statistics.mean(height_list)
weightMean = statistics.mean(weight_list)

heightMedian = statistics.median(height_list)
weightMedian = statistics.median(weight_list)

heightMode = statistics.mode(height_list)
weightMode = statistics.mode(weight_list)

print("Mean, median and mode of height is ", heightMean,heightMedian,heightMode)
print("Mean, median and mode of weight is ", weightMean,weightMedian,weightMode)

stdDevHeight = statistics.stdev(height_list)

first_std_dev_start_height, first_std_dev_end_height = heightMean-stdDevHeight, heightMean+stdDevHeight
second_std_dev_start_height, second_std_dev_end_height = heightMean-(2*stdDevHeight), heightMean+(2*stdDevHeight)
third_std_dev_start_height, third_std_dev_end_height = heightMean-(3*stdDevHeight), heightMean+(3*stdDevHeight)

list_of_data_within_first_std_dev_height = [result for result in height_list if result>first_std_dev_start_height and result<first_std_dev_end_height]
list_of_data_within_second_std_dev_height = [result for result in height_list if result>second_std_dev_start_height and result<second_std_dev_end_height]
list_of_data_within_third_std_dev_height = [result for result in height_list if result>third_std_dev_start_height and result<third_std_dev_end_height]

print("Standard Deviation of this data is", stdDevHeight)
print("{}% of data lies in First Standard Deviation".format(len(list_of_data_within_first_std_dev_height)*100.0/len(height_list)))
print("{}% of data lies in Second Standard Deviation".format(len(list_of_data_within_second_std_dev_height)*100.0/len(height_list)))
print("{}% of data lies in Third Standard Deviation".format(len(list_of_data_within_third_std_dev_height)*100.0/len(height_list)))

stdDevWeight = statistics.stdev(weight_list)

first_std_dev_start_weight, first_std_dev_end_weight = weightMean-stdDevWeight, weightMean+stdDevWeight
second_std_dev_start_weight, second_std_dev_end_weight = weightMean-(2*stdDevWeight), weightMean+(2*stdDevWeight)
third_std_dev_start_weight, third_std_dev_end_weight = weightMean-(3*stdDevWeight), weightMean+(3*stdDevWeight)

list_of_data_within_first_std_dev_weight = [result for result in weight_list if result>first_std_dev_start_weight and result<first_std_dev_end_weight]
list_of_data_within_second_std_dev_weight = [result for result in weight_list if result>second_std_dev_start_weight and result<second_std_dev_end_weight]
list_of_data_within_third_std_dev_weight = [result for result in weight_list if result>third_std_dev_start_weight and result<third_std_dev_end_weight]

print("Standard Deviation of this data is", stdDevWeight)
print("{}% of data lies in First Standard Deviation".format(len(list_of_data_within_first_std_dev_weight)*100.0/len(weight_list)))
print("{}% of data lies in Second Standard Deviation".format(len(list_of_data_within_second_std_dev_weight)*100.0/len(weight_list)))
print("{}% of data lies in Third Standard Deviation".format(len(list_of_data_within_third_std_dev_weight)*100.0/len(weight_list)))