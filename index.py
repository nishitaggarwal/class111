import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()




mean_of_population = statistics.mean(data)
print("Mean Of the Population is:-" ,mean_of_population)

standard_dev = statistics.stdev(data)
print("standard Deviation for population is:-",standard_dev)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        rand_ix = random.randint(0,len(data)-1)
        value = data[rand_ix]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_dev = statistics.stdev(mean_list)
print("standard deviation:- ",std_dev)

mean = statistics.mean(mean_list)
print("Mean of Sampling Distribution:",mean)





first_std_dev_start,first_std_dev_end = mean-std_dev,mean + std_dev
second_std_dev_start,second_std_dev_end = mean- (2 * std_dev),mean + (2 * std_dev)
third_std_dev_start,third_std_dev_end = mean- (3 * std_dev),mean + (3 * std_dev)

print("First Standard Deviation:-",first_std_dev_start,first_std_dev_end)

print("Second Standard Deviation:-",second_std_dev_start,second_std_dev_end)

print("Third Standard Deviation:-",third_std_dev_start,third_std_dev_end)



fig  = ff.create_distplot(
    [mean_list],
    ["student Marks "],
    show_hist = False
    )
fig.add_trace(go.Scatter(
    x = [mean,mean], 
    y = [0,0.20],
    mode = "lines",
    name = "MEAN"
    ))
fig.add_trace(go.Scatter(
    x = [first_std_dev_start,first_std_dev_start], 
    y = [0,0.15],
    mode = "lines",
    name = "First Standard Deviation Start"
    ))
fig.add_trace(go.Scatter(
    x = [first_std_dev_end,first_std_dev_end], 
    y = [0,0.15],
    mode = "lines",
    name = "First Standard Deviation End"
    ))
fig.add_trace(go.Scatter(
    x = [second_std_dev_start,second_std_dev_start], 
    y = [0,0.15],
    mode = "lines",
    name = "Second Standard Deviation Start"
    ))
fig.add_trace(go.Scatter(
    x = [second_std_dev_end,second_std_dev_end], 
    y = [0,0.15],
    mode = "lines",
    name = "Second Standard Deviation End"
    ))
fig.add_trace(go.Scatter(
    x = [third_std_dev_start,third_std_dev_start], 
    y = [0,0.15],
    mode = "lines",
    name = "Third Standard Deviation Start"
    ))
fig.add_trace(go.Scatter(
    x = [third_std_dev_end,third_std_dev_end], 
    y = [0,0.15],
    mode = "lines",
    name = "Third Standard Deviation End"
    ))
fig.show()



df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()


mean_of_sample1 = statistics.mean(data)
print("Mean Of the sample 1 is:- " ,mean_of_sample1)


fig  = ff.create_distplot(
    [mean_list],
    ["student Marks "],
    show_hist = False
    )
fig.add_trace(go.Scatter(
    x = [mean,mean], 
    y = [0,0.20],
    mode = "lines",
    name = "MEAN"
    ))
fig.add_trace(go.Scatter(
    x = [mean_of_sample1,mean_of_sample1], 
    y = [0,0.20],
    mode = "lines",
    name = "Mean of sample1"
    ))
fig.add_trace(go.Scatter(
    x = [first_std_dev_end,first_std_dev_end], 
    y = [0,0.15],
    mode = "lines",
    name = "First Standard Deviation End"
    ))
fig.show()

mean_of_sample2 = statistics.mean(data)
print("Mean Of the sample 2 is:- " ,mean_of_sample2)


mean_of_sample3 = statistics.mean(data)
print("Mean Of the sample 3 is:- " ,mean_of_sample3)

mean = statistics.mean(data)
print(mean)

zScore1 = (mean_of_sample1-mean)/std_dev
print("zscore is:-",zScore1)

zScore2 = (mean_of_sample2-mean)/std_dev
print("zscore is:-",zScore2)

zScore3 = (mean_of_sample3-mean)/std_dev
print("zscore is:-",zScore3)