### Explore US Bikeshare Data

### Summary
  In this project, Python code is used to import US bike share data of given cities(Chicago,New York,Washington) and answer questions (usage by city,gender,age,station etc) about given dataset by using computing descriptive statistics.

### Prerequisite
  * Python

### Example Configuration

```   sh
$ python bikeshare.py
Hello! Let's explore some US bikeshare data!

 Select City :
 1.chicago
 2.New York
 3.washington

Please enter city from above options :chicago

 Selected city : Chicago

 Select month :
 All  
 January,
 February,
 March,
 April,
 May,
 June
 Please Enter month from above options:All

 Select day :
 All  
 Monday
 Tuesday
 Wednesday
 Thursday
 Friday
 Saturday
 Sunday
  Please enter day from above options:Monday
----------------------------------------

Calculating The Most Frequent Times of Travel...


Most common Month :  june

Most common Day of week :  Monday

Most Common Start Hour : 17

This took 0.007082939147949219 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...


 Common STart Station Streeter Dr & Grand Ave

 Common End Station Streeter Dr & Grand Ave

 Common Trip ('Lake Shore Dr & Monroe St', 'Streeter Dr & Grand Ave')

This took 0.02377796173095703 seconds.
----------------------------------------

Calculating Trip Duration...

Total Travel Time  39945856
Mean Travel Time 890.039348499365

This took 0.0007648468017578125 seconds.
----------------------------------------

Calculating User Stats...

User Types :  User Type
Customer       7565
Subscriber    37316
Name: User Type, dtype: int64
Gender  :  Gender
Female     8689
Male      28646
Name: Gender, dtype: int64
Earliest birth Year 1899.0
Recent birth Year 2016.0
Common Birth Year 1989.0

This took 0.014342069625854492 seconds.
----------------------------------------

 Number of Rows in Filtered Data 44881

 Would you like to display 5 lines of Filtered data? Enter Yes or No :No

Would you like to restart? Enter yes or no.
no
$

```

### Built with
   * Python 3, NumPy, and pandas installed using Anaconda
   * Atom
   * Terminal(Mac)
