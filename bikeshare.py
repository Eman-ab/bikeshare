# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:03:57 2020

@author: Mohamed-115
"""

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
cities=['new york city','chicago','washington']
#infinite loop
while True:
    city=input("Enter a city: ")
    city=city.lower()
    #condition in the middle
    if city in cities:
        break
    print("That is not a city.")
       # get user input for month (all, january, february, ... , june)
months=['january','february','march','april','may','june']
#infinite loop
while True:
    month=input("Enter a month: ")
    month=month.lower()
    #condition in the middle
    if month in months:
        break
    print("That is not a month")
    # get user input for day of week (all, monday, tuesday, ... sunday)
days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
#infinite loop
while True:
    day=input("Enter a day: ")
    day=day.lower()
    #condition in the middle
    if day in days:
        break
    print("That is not a day")
def load_data():
  city,month,day=load_data()
  return city, month, day
print(city)
print(month)
print(day)
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
df=pd.read_csv(CITY_DATA[city])
print(df)
    #convert 'start time' to datetime object
df['Start Time']=pd.to_datetime(df['Start Time'])
print(df)
#extract month and day from Start Time
df['month'] = df['Start Time'].dt.month
df['day'] = df['Start Time'].dt.day
df['hour'] = df['Start Time'].dt.hour
#filter based on month then on day 
if month !='all':
#use the index of the months list to get the corresponding int
 months=['january','february','march','april','may','june']
 month = months.index(month) + 1
#filter by month to create the new dataframe 
df=df.loc[df['month']==month]
#filter by day name if applicable
if day !='all':
#use the index of the days list to get the corresponding int
 days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
 day = days.index(day) + 1
#filter by day name to create the new dataframe
 df = df.loc[df['day']==day]   


  
 def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()

# TO DO: display the most common month
common_month= df['Start Time'].dt.month_name().mode()[0]
print('Common month is :{}'.format(common_month))

    # TO DO: display the most common day of week
common_day=df['Start Time'].dt.day_name().mode()[0]
print('Common day is:{}'.format(common_day))
    # TO DO: display the most common start hour
common_hour=df['Start Time'].dt.hour.mode()[0]
print('Common hour is:{}'.format(common_hour))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        (df) df - pandas DataFrame containing city data filtered by month and day if applicable
    """

print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()
most_common_start_station=df['Start Station']+"|"+df['End Station']
start_time=time.time()
most_common_start_station=df['Start Station'].mode()[0]
most_common_end_station=df['End Station'].mode()[0]
# TO DO: display most commonly used start station
print('The most common Start Station is:{}'.format(most_common_start_station))
 # TO DO: display most commonly used end station
print('The most common End Station is:{}'.format(most_common_end_station))
# TO DO: display most frequent combination of start station and end station trip
df['Frequent Trip']=df['Start Station']+'to'+df['End Station']
common_trip=df['Frequent Trip'].mode()[0]
print('Most common trip:{}'.format(common_trip))
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        df - pandas DataFrame containing city data filtered by monh and day if applicable
    """
    print('\nCalculating Trip Duration...\n')
start_time = time.time()
 # TO DO: display total travel time
total_travel_time=df['Trip Duration'].sum() 
print('Total travel time:',total_travel_time,'seconds')
 # TO DO: display mean travel time
mean_travel_time=df['Trip Duration'].mean()
print('Average travel time:',mean_travel_time,'seconds')
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
def user_stats(df):
    """
    Displays statistics on bikeshare users.
    Args:
        df - pandas DataFrame containing city data filtered by month and day if applicable 
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
user_types=df['User Type'].value_counts()
print("Count of user type:\n{0}\n{1}\n{0}\n".format('_'*20,user_types.to_string()))
 # TO DO: Display counts of gender
#check for gender coloumn is missing ,other wise print counts of gender
if 'Gender' in df:
 user_genders=df['Gender'].value_counts()
print("Count of gender:\n{0}\n{1}\n{0}\n".format('_'*20,user_genders.to_string()))
# TO DO: Display earliest, most recent, and most common year of birth
if 'Birth Year' in df:
 birth_year=df['Birth Year']
earliest_year_of_birth=int(birth_year.min())
mostrecent_year_of_birth=int(birth_year.max())
common_year_of_birth=int(birth_year.mode()[0])
#year data was collected to calculate age
data_collection_year=2017
print("Earliest year of birth: {} ( eldest user was {} )".format(earliest_year_of_birth,data_collection_year-earliest_year_of_birth))
print("Most recent year of birth: {} (youngest user was {} )".format(mostrecent_year_of_birth,data_collection_year-mostrecent_year_of_birth))
print("Most common year of birth: {} (most common age {} )".format(common_year_of_birth,data_collection_year-common_year_of_birth))
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
def show_raw_data(df):
    """ 
     Display raw data in batch of 5 upon user request.
      Args:
          df - pandas DataFrame containing city data filtered
          """ 
row=0
reviewanswer = input('\nWould you like to see sample raw data ?(y)es or anything else for no.\n')
while reviewanswer.lower() == 'yes'or reviewanswer.lower() == 'y':
 df=df.iloc[row:row+5]
#check if end of data is reached,if so ,exit the loop
if df.empty:
 print('no more data to display!')
      
def main():
    """
    Takes into account all the functions and run them in orderself.
    """
    while True:
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
