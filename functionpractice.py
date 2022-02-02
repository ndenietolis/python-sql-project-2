import pandas as pd
import time
import numpy as np

# df = pd.read_csv('new_york_city.csv')
# df = pd.read_csv('washington.csv')
df = pd.read_csv('chicago.csv')
# df['Start Time'] = pd.to_datetime(df['Start Time'])
# df['month'] = df['Start Time'].dt.strftime("%B")
# df['day_of_week'] = df['Start Time'].dt.strftime("%A")
# df['hour'] = df['Start Time'].dt.strftime("%H")
# print(df['hour'].head() + ":00")
#df['Station Combos'] = 'Start: ' + df['Start Station'] + ' | ' + 'End: ' + df['End Station']
#  
# df['Station Combos'] = 'Start: ' + df['Start Station'] + ' & ' + 'End: ' + df['End Station']
# for index in df.index:
#     if df['Start Station'][index] == df['End Station'][index]:
#         df.at[index, 'Trip Type'] = 'round trip'
#     else:
#         df.at[index, 'Trip Type'] = 'one way'
# print(df['Start Station'][df['Trip Type'] == 'round trip'].mode()[0])
# print(df['Station Combos'][df['Trip Type'] == 'one way'].mode()[0])
# print(('Users spent an average of {} minutes riding per trip.').format(int(df['Trip Duration'].mean()/60)))
# if 'Gender' in df.columns:
#     print(df['Gender'].value_counts())
# else:
#     print('n/a')
# print(df['User Type'].value_counts())
# print(df['User Type'].value_counts().index[1])
# print(df['User Type'].value_counts()[df['User Type'].value_counts().index[1]])
# for x in df['User Type'].value_counts().index:
#    print(x + 's', df['User Type'].value_counts()[x])
# if 'Birth Year' in df.columns:
#     print('The oldest users were born in: ', int(df['Birth Year'].max()))
#     print('The youngest users were born in: ', int(df['Birth Year'].min()))
#     print('The average user was born in: ', int(df['Birth Year'].mean()))
#     print('The majority of users were born in: ', int(df['Birth Year'].mode()))
raw_dat = input('Would you like to see the raw data? Type yes or no\n').lower()
index_counter = 0
while True:
    if raw_dat == 'yes':
        print(df[index_counter:index_counter + 5])
        index_counter += 5
        while True:
            raw_dat = input('Would you like to see five more rows? Type yes or no\n')
            if raw_dat == 'no' or raw_dat == 'yes':
                break
            elif raw_dat != 'yes':
                print('Oops, that\'s not an option. Please type yes or no\n')
    if raw_dat == 'no':
        break
        