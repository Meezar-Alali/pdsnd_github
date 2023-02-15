# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 03:13:22 2023

@author: Meezar.Alali
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
City_input=['chicago','new york city','washington']
Month_input=['all','janury','february','march','april','may','june']
Day_input=['All', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['all','january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city,month,day=None,None,None
    try:
        print('Hello! Let\'s explore some US bikeshare data!')
               # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
           
        city=input("Enter the City name 'chicago' 'new york city' 'washington': \n").lower()
                       
        while city not in City_input:
            city=input("Enter the Exact City name 'chicago' 'new york city' 'washington': \n").lower()
          
                
            
                

            # get user input for month (all, january, february, ... , june)
           
        month=input("In which month you want to filter enter: 'all','january','february',....,'june':  ").lower()
        while month not in Month_input:
           
            month=input("In which month you want to filter enter: 'all','january','february',....,'june':  ").lower()
                  
                

               
                
            # get user input for day of week (all, monday, tuesday, ... sunday)

        day=input(" which day of week you want to filter enter: 'all','monday'tuesday',....,sunday: ").title()
        while day not in Day_input:
            day=input("Enter correct day name spelling or 'all': ").title()
        print('-'*40)
    except Exception as e:
        print("Exception occurred: {}".format(e))    
                
          
    return city,month,day

def load_data(city,month,day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=None
    #read csv file 
    try:
        df = pd.read_csv(CITY_DATA[city])
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
        # extract start hour to be used in other functions like time_state
        df['hour']=df['Start Time'].dt.hour
        if month != 'all':
            print()
            # use the index of the months list to get the corresponding int
            month = months.index(month)
            # filter by month to create the new dataframe
            df = df[df['month']==month]
         # filter by day of week if applicable
        if day != 'All':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week']==day.title()]
    except Exception as ex:
        print("Exception occurred: {}".format(ex))
        
    return df

def time_stats(df):
    try:
        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # display the most common month
        name_of_month =months[df['month'].mode()[0]]
        
        print("Most trips were happened in the month : {}".format(name_of_month))
        # display the most common day of week
      
        print("Most trips were happened in day : {}".format(df['day_of_week'].mode()[0]))

        # display the most common start hour
        print("Most trips started at hour : {}".format(df['hour'].mode()[0]))

       
    except Exception as ex:
            print("Exception occurred: {}".format(ex))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    try:
        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # display most commonly used start station
        
        print("Most commonly trips started from station: {}".format(df['Start Station'].mode()[0]))


        # display most commonly used end station
        print("Most trips ended at station: {}".format(df['End Station'].mode()[0]))


        # display most frequent combination of start station and end station trip
        df['start to end']=df['Start Station']+" "+df['End Station']
        print("Most frequent combination trips of start station and end station: {}".format(df['start to end'].mode()[0]))
        

        
    except Exception as ex:
        print("Exception occurred: {}".format(ex))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    Travel_day,Travel_hour,Travel_minute,Travel_second=0,0,0,0
    
    """Displays statistics on the total and average trip duration."""
    try:
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # display total travel time
        Travel_day=(np.sum(df['Trip Duration'])//(24*3600))
        Travel_hour=(np.sum(df['Trip Duration'])-(Travel_day*24*3600))//3600
        Travel_minute=(np.sum(df['Trip Duration'])-(Travel_day*24*3600)-(Travel_hour*3600))//60
        Travel_second=np.sum(df['Trip Duration'])-(Travel_day*24*3600)-(Travel_hour*3600)-(Travel_minute*60)
        print("Total travle time is {} days, {} hours , {} minutes ,{} seconds".format(Travel_day,Travel_hour,Travel_minute,Travel_second))
        
    except Exception as e:
        print("Exception occurred: {}".format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
              

    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        print("\nAnalysis users by type:")
        if 'User Type' in df.columns:
            df['User Type'].fillna(method='bfill',inplace=True)
            user_stat = df.groupby(['User Type'])['User Type'].count()
            print(user_stat)
            
         
        else:
            print('The data set does not contain any users type!!')
         
        

    

    # Display counts of gender
        print("Analysis users by gender :")
        if 'Gender' in df.columns:
            #Clean data set by filing missing data 
            df['Gender'].fillna(method='bfill',inplace=True)
            user_stat = df.groupby(['Gender'])['Gender'].count()
            print(user_stat)
            
       
        else:
            print('The data set does not contain any gender type!!')
       


    # Display earliest, most recent, and most common year of birth
        print("\nAnalysis users by birth year:")
        if 'Birth Year' in df.columns:
            #Clean data set by filing missing data 
            df['Birth Year'].fillna(method='bfill',inplace=True)
            
            earliest=int(np.min(df['Birth Year']))
            most_recent=int(np.max(df['Birth Year']))
            most_common=int(df['Birth Year'].mode()[0])
            print("The eldest user was borened in :{}\nThe youngest user borned in {},\nMostly users were born in {}".format(earliest,most_recent,most_common))
        else:
            print('The data set does not contain any Birth date!!')
            
        # Display counts of user types,
        
        print("\nAnalysis users by type:")
        if 'User Type' in df.columns:
            df['User Type'].fillna(method='bfill',inplace=True)
            user_stat = df.groupby(['User Type'])['User Type'].count()
            print(user_stat)
        else:
            print('Your dataset does not contain users type!!')
            
            
    except Exception as e:
        print("Exception occurred: {}".format(e))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_bikeshare=input('would you like to view first 5 rows of the data set? Type: yes or No : ').lower()
            if view_bikeshare=='yes':
                raw_index=0
                while True:
                    print(df.iloc[raw_index:raw_index+5]) 
                    raw_index+=5
                    view_bikeshare=input('would you like to view the first 5 rows of the bike share data set?').lower()
                    if view_bikeshare=='no':
                        break
            if view_bikeshare=='no':
                break
            
            else:
                break
            
  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
                


    

  




        
    