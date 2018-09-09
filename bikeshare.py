import time
import pandas as pd
import numpy as np
import calendar

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

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
    flag=True
    while flag:
      print('\n Select City : \n 1.chicago \n 2.New York \n 3.washington \n')
      city=input('Please enter city from above options :')
      if city=='1' or city.lower()=="chicago":
         print('\n Selected city : Chicago')
         city='chicago.csv'
         flag=False
      elif city=='2' or city.lower()=="new york":
         print('\n Selected city : New york')
         city='new_york_city.csv'
         flag=False
      elif city=='3' or city.lower()=="washington":
         print('\n Selected city : washington')
         city='washington.csv'
         flag=False
      else:
         print('\n Invalid City. Try again')


    # get user input for month (all, january, february, ... , june)
    flag=True
    while flag:
      month = input('\n Select month : \n All  \n January,\n February,\n March,\n April,\n May,\n June \n Please Enter month from above options:')
      month = month.lower()
      if month == "all":
         flag=False
      elif month in MONTHS:
         month=MONTHS.index(month)+1
         flag=False
      else:
         print('\nInvalid month. Try again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    flag=True
    while flag:
      day = input('\n Select day : \n All  \n Monday \n Tuesday \n Wednesday \n Thursday \n Friday \n Saturday \n Sunday \n  Please enter day from above options:')
      if day.lower() == "all":
         flag=False
      elif day.lower() == "monday":
         day='Monday'
         flag=False
      elif day.lower() == "tuesday":
         day='Tuesday'
         flag=False
      elif day.lower() == "wednesday":
         day='Wednesday'
         flag=False
      elif day.lower() == "thursday":
         day='Thursday'
         flag=False
      elif day.lower() == "friday":
         day='Friday'
         flag=False
      elif day.lower() == "saturday":
         day='Saturday'
         flag=False
      elif day.lower() == "sunday":
         day='Sunday'
         flag=False
      else:
         print('\nInvalid day. Try again')

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
    df=pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df_month = df.groupby('month')['Start Time'].count()
    print('\nMost common Month : ',MONTHS[df_month.sort_values(ascending=False).index[0]-1])

    # display the most common day of week
    df_day = df.groupby('day_of_week')['Start Time'].count()
    print('\nMost common Day of week : ',df_day.sort_values(ascending=False).index[0])


    # display the most common start hour

    print('\nMost Common Start Hour :', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    df_start_station = df.groupby('Start Station')['Start Time'].count()
    print('\n Common STart Station',df_start_station.sort_values(ascending=False).index[0])

    # display most commonly used end station
    df_end_station = df.groupby('End Station')['Start Time'].count()
    print('\n Common End Station',df_end_station.sort_values(ascending=False).index[0])

    # display most frequent combination of start station and end station trip
    df_trip = df.groupby(['Start Station','End Station'])['Start Time'].count()
    print('\n Common Trip',df_trip.sort_values(ascending=False).index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    print('Total Travel Time ',df['Trip Duration'].sum())

    # display mean travel time
    print('Mean Travel Time',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Types : \n',df.groupby('User Type')['User Type'].count())

    # Display counts of gender
    print('Gender  : \n',df.groupby('Gender')['Gender'].count())

    # Display earliest, most recent, and most common year of birth
    print('Earliest birth Year',df['Birth Year'].min())
    print('Recent birth Year',df['Birth Year'].max())
    df_birth_year=df.groupby('Birth Year')['Birth Year'].count()
    print('Common Birth Year',df_birth_year.sort_values(ascending=False).index[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_filtered_data(df,line_no):
    """Displays Filtered data on bikeshare users."""
    while True:
        view_data = input('\n Would you like to display 5 lines of Filtered data? Enter Yes or No :')
        count=df['Start Time'].count()
        if view_data.lower() == 'yes' or view_data.lower() == 'y':
            if count <= line_no:
                print('\n Finished Printing all rows in Filtered Data')
                break
            else:
                print(df.iloc[line_no:line_no+5])
                line_no += 5
        elif view_data.lower() == 'no' or view_data.lower() == 'n':
            break
        else:
            print('\n Invalid Option. Try again')
            return print_filtered_data(df, line_no)
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != "washington.csv":
            user_stats(df)
        else :
            print('Gender and BirthYear details are not available for Washington')
        print('\n Number of Rows in Filtered Data',df['Start Time'].count())
        print_filtered_data(df,0)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
