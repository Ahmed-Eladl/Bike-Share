import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("choose a city from (chicago , new york city , washington): ").lower()
        if city not in CITY_DATA:
            print("invalid choice , please choose a correct city name ")

        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            'please choose a month from january ,february, march,april,may,june or choose "all" to show all months :').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months and month != 'all':
            print("invalid month , please choose a month from january to june or all")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please choose a day of the week(saturday ,sunday ,monday ,tuesday ,wednesday ,thursday ,friday) , or choose "all" to display all days :').lower()
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if day not in days and day != 'all':
            print("invalid day , please enter a valid day or all ")
        else:
            break

    print('-' * 40)

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
      return:
           df

    """

    # make dataframe like PRACTICE 1

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # separate month and day from start time to new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #  like PRACTICE 3

    # filter by month  if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  # use index to get corresponding int

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("the most common month: ",
          calendar.month_name[most_common_month])  # used calendar to get month name from month number

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("the most common day is :", most_common_day)

    # TO DO: display the most common start hour
    # separate hour from the start time column and put in the new column
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("the most common start hour :", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("the most start station is :", most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print("the most end station is :", most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + 'to' + df['End Station']).mode()[0]
    print("the most frequent combination of Start and End station:", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time :', total_travel_time, 'seconds, or', total_travel_time / 3600, 'hour',
          int(total_travel_time / 86400), 'days')

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('average travel time is :', avg_time, 'seconds, or ', avg_time / 3600, 'hour', int(avg_time / 86400), 'days')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user type: \n', df['User Type'].value_counts())

    # TO DO: Display counts of gender

    # washington has not gender in the data set ,so we made if statement to avoid the error
    if 'Gender' in df:
        print('\n counts of gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth

    # washington has not Birth Year in the data set,so we made if statement to avoid the error
    if 'Birth Year' in df:
        earliest_b_year = int(df['Birth Year'].min())
        print('\n Earliest year of birth:\n', earliest_b_year)
        recent_b_year = int(df['Birth Year'].max())
        print('\n most recent year of birth:\n', recent_b_year)
        common_b_year = int(df['Birth Year'].mode()[0])
        print('\n most common year of birth:\n', common_b_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
 #ask user if he wants to show the raw_data for  first 5 rows

def display_raw(df):
     raw_data = input('would you like to show the first 5 rows data (yes or no): \n ').lower()

     if raw_data == 'yes':
         counter = 0
         while True:
             print(df.iloc[counter:counter + 5])
             counter += 5
             question = input("do you want to show  next 5 rows? (yes or no)").lower()
             if question != 'yes':
                 break










def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
