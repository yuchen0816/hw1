# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108000133.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
data = list(filter(lambda item: item['TEMP'] != '-99.000' and  item['TEMP'] != '-999.000', data))
ans = []

data1 = []
target_data1 = list(filter(lambda item: item['station_id'] == 'C0A880', data))
for row in target_data1:
   data1.append(row['TEMP'])
ans.append(['C0A880', max(data1)])

data2 = []
target_data2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
for row in target_data2:
   data2.append(row['TEMP'])
ans.append(['C0F9A0', max(data2)])

data3 = []
target_data3 = list(filter(lambda item: item['station_id'] == 'C0G640', data))
for row in target_data3:
   data3.append(row['TEMP'])
ans.append(['C0G640', max(data3)])

data4 = []
target_data4 = list(filter(lambda item: item['station_id'] == 'C0R190', data))
for row in target_data4:
   data4.append(row['TEMP'])
ans.append(['C0R190', max(data4)])

data5 = []
target_data5 = list(filter(lambda item: item['station_id'] == 'C0X260', data))
for row in target_data5:
   data5.append(row['TEMP'])
ans.append(['C0X260', max(data5)])

# Retrive ten data points from the beginning.
#target_data = data[:]

#=======================================

# Part. 4
#=======================================
# Print result
print(ans)
#========================================