import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks the user to select a city and returns the filename for that city's bike share data.
    Args:
    none.
    Returns:
        (str) city - name of the city to analyze
    """
    
    person = input("Please tell us who you are: ")
    print("Hello there, {}!".format(person.title()))
    print('Let\'s explore some US bikeshare data!')
   
    # ask user to choose a city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York, or'
                   ' Washington?\n').lower().title()
    while(True):
        if city == 'chicago':
            return 'chicago.csv'
        elif city == 'new york':
            return 'new_york_city.csv'
        elif city == 'washington':
            return 'washington.csv'
            break
        else:
            print("\nI'm sorry, I do not recognize that city. Let's try again.")
            return get_city()
        
def get_month():
    """
    Asks the user to select a month of the year (all, january, february, ....june) 
    Args:
    none.
    Returns:
         (str) month - name of the month to analyze
    """
    #ask user to choose a month (january, february...june)
    month = input('Which month would you like to filter by? january, february, march, april, may, june or all?\n').lower()
    
    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter valid month\n').lower()
            return get_month()
        
def get_day():        
    """
    Asks the user to select a day of the week (all, monday, tuesday, ... sunday)
    Args:
    none.
    Returns:
        (str) day - name of the day to analyze
    """
    #ask user to choose a day of the week (monday, tuesday...sunday)
    day = input('Please choose a day ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n').lower()
    
    while(True):
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Please enter Correct day: ').lower()
            return get_day()
             #lower is used to get input in any format


    print('-'*40)

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
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # to_datetime is used to convert date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #finding index of month.
        month = months.index(month) + 1      

        df = df[df['Start Time'].dt.month == month]

    #look at data by day.
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print only 5 rows.
    print(df.head())
    return df


def time_stats(df, month, day):
    """Calculating statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # show us the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # show us the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))

    # show us the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Calculating statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # show us most commonly used start station
    most_common_start_station = st.mode(df['Start Station'])
    print('\nMost common start station is {}\n'.format(most_common_start_station))

    # show us most commonly used end station
    most_common_end_station = st.mode(df['End Station'])
    print('\nMost common end station is {}\n'.format(most_common_end_station))

    # show us most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Calculating statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calculate total travel time
    total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # calculate mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time2 = mean_travel_time
    day2 = time2 // (24 * 3600)
    time2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print('\nMean travel time is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Calculating statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate counts of user types
    no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers are {}\n'.format(int(no_of_subscribers)))
    print('\nNumber of customers are {}\n'.format(int(no_of_customers)))
   
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nCalculating your requested statistic...")
        start_time = time.time()

    # Calculate counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))


    # Calculate earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = st.mode(df['Birth Year'])
        print('\n Oldest Birth Year is {}\n Youngest Birth Year is {}\n Most popular Birth Year is {}\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def stats():
    """
    Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    """
    # Filter by city (Chicago, New York, Washington)
    city = get_mycity()
    city_df = pd.read_csv(city)   


    # Give the user the option to restart?
def restart():
    """
    Restarts the program based on the user's input
    Args:
        none.
    Returns:
    """
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'. (If you say no it will end the program and it will exit.)\n')
    if restart.lower() == 'yes' or restart.lower() == 'y':
            stats()
    elif restart.lower() == 'no' or restart.lower() == 'n':
            return
    else:
     print("\nI'm not sure if you wanted to restart or not. Let's try again.")
            return restart()



if __name__ == "__main__":
        stats()