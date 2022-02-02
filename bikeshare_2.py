import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What city would you like to query?\nYour options are:\
            \nChicago\nNew York City\nWashington\nPlease type your answer below\n").lower()
        if city in CITY_DATA:
            break
        else:   
            print("That's not an option or may have been misspelled.\nMake sure to type city names exactly as they appear!")

    # get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June', \
        'July', '', 'August', 'September', 'October', 'November', 'December'] 
    while True:
        month = input("If you would like to query a specific month enter the name below, otherwise press return to leave blank\nThe data are for January-June\n").title()
        if month in months:
            break
        else:   
            print("That's not an option or may have been misspelled.\n")
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', '']
    while True:
        day  = input("If you would like to query a specific weekday enter the name below otherwise press return to leave blank\n").title()
        if day in days:
            break
        else:   
            print("That's not an option or may have been misspelled.\n")



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    start_time = time.time()
    print('Loading data...')
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.strftime("%B")
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['hour'] = df['Start Time'].dt.strftime("%H")
    # filter by month if applicable
    if month != '':
        # use the index of the months list to get the corresponding int
        #
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        

    # filter by day of week if applicable
    if day != '':
        # days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', '']
        # day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week'] == day]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    return df


def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel.
    If data is filtered by day and/or month, these data will be ommitted from results.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == '':
        print('The most common month was: ', df['month'].mode()[0])
   
    # display the most common day of week
    if day == '':
        print('The most common day of the week was: ', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('The most common start hour was: ', df['hour'].mode()[0] + ':00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station was: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most common end station was: ', df['End Station'].mode()[0])

    # determine if trips are 'one way' or 'round trips'
    for index in df.index:
        if df['Start Station'][index] == df['End Station'][index]:
            df.at[index, 'Trip Type'] = 'round trip'
        else:
            df.at[index, 'Trip Type'] = 'one way'
        
    # display most frequent combination of start station and end station trip
    df['Station Combos'] = df['Start Station'] + ' & ' + df['End Station']
    print('The most common station for a round trip was: ', df['Start Station'][df['Trip Type'] == 'round trip'].mode()[0])
    print('The most common one way trip was between: ', df['Station Combos'][df['Trip Type'] == 'one way'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(('Users spent {} hours riding in total.').format(int(df['Trip Duration'].sum()/3600)))

    # display mean travel time
    print(('Users spent an average of {} minutes riding per trip.').format(int(df['Trip Duration'].mean()/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Breakdown of users by type:')
    for x in df['User Type'].value_counts().index:
        print(x + 's:', df['User Type'].value_counts()[x])

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Breakdown of users by gender:')
        for x in df['Gender'].value_counts().index:
            print(x + 's:', df['Gender'].value_counts()[x])

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The oldest users were born in: ', int(df['Birth Year'].min()))
        print('The youngest users were born in: ', int(df['Birth Year'].max()))
        print('The average user was born in: ', int(df['Birth Year'].mean()))
        print('The most users were born in: ', int(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
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
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
