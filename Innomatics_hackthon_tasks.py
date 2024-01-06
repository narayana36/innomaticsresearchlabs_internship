#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv


# In[4]:


My_str_1


# In[3]:


Foo


# In[5]:


Abc = 100,000,000


# In[6]:


A,b,c = 100,200,300


# In[7]:


A b c = 100 200 300


# In[8]:


A_b_c = 100,000,000


# In[9]:


tup = (1, 2, 3)


# In[10]:


tup = (1)


# In[11]:


tup = [1, 2, 3]


# In[13]:


import pandas as pd


# In[65]:


movies=pd.read_csv(r"C:\Users\pagad\Downloads\movie_data\movies.csv")
movies.shape


# In[66]:


movies


# In[16]:


ratings=pd.read_csv(r"C:\Users\pagad\Downloads\movie_data\ratings.csv")
ratings.shape


# In[167]:


tags=pd.read_csv(r"C:\Users\pagad\Downloads\movie_data\tags.csv")
tags.shape


# In[236]:


links=pd.read_csv(r"C:\Users\pagad\Downloads\movie_data\links.csv")
links.shape


# In[18]:


ratings


# In[19]:


ratings['userId'].nunique()


# In[190]:


df1=pd.concat([movies,ratings,tags])
df1


# In[179]:


df = pd.concat([movies, ratings],axis=1)
df


# In[180]:


max_rating = df['rating'].max()
max_rating


# In[181]:


max_rating_row = df.loc[df['rating'] == max_rating]
max_rating_row


# In[182]:


print('Maximum number rating:', max_rating)
print('Row with the maximum number rating:', max_rating_row)


# In[183]:


max_rating = df['rating'].max()
max_rating


# In[185]:


terminator_df = df[df['title'] == 'Terminator 2: Judgment Day (1991)']

# Calculate the average user rating
average_rating = terminator_df['rating'].mean()
average_rating


# In[186]:


terminator_df = df[df['title'] == 'Jumanji (1995)']

# Calculate the average user rating
average_rating = terminator_df['rating'].mean()
average_rating


# In[187]:


terminator_df = df[df['title'] == 'Shawshank Redemption, The (1994)']

# Calculate the average user rating
average_rating = terminator_df['rating'].mean()
average_rating


# In[188]:


terminator_df = df[df['title'] == 'Godfather, The (1972)']

# Calculate the average user rating
average_rating = terminator_df['rating'].mean()
average_rating


# In[189]:


terminator_df = df[df['title'] == 'Wolf of Wall Street, The (2013)']

# Calculate the average user rating
average_rating = terminator_df['rating'].mean()
average_rating


# In[127]:


terminator_df = df[df['title'] == 'Terminator 2: Judgment Day (1991)']

# Calculate the average user rating
average_rating = terminator_df['rating'].mean()
average_rating


# In[116]:


df[df['title']=='Fight Club (1999)']['rating'].mean()


# In[235]:


df[df['genres']=='Sci-Fi']['rating'].head()


# In[108]:


import matplotlib.pyplot as plt


# In[111]:


fight_club_df = df[df['title'] == 'Fight Club (1999)']

# Plotting the data distribution
plt.figure(figsize=(8, 6))
plt.hist(fight_club_df['rating'])
plt.title('User Ratings Distribution for Fight Club (1999)')
plt.xlabel('User Ratings')
plt.ylabel('Frequency')
#plt.grid(True)
plt.show()


# In[158]:


ratings_grouped = pd.DataFrame(df)


# In[201]:


# Group by movieId and apply aggregation functions
ratings_grouped = df1.groupby('movieId').agg({'rating': ['count', 'mean']}).reset_index()

# Rename the columns for better readability
ratings_grouped.columns = ['movieId', 'rating_count', 'rating_mean']

print(ratings_grouped)


# In[244]:


# Assuming ratings_grouped is your grouped dataframe with rating counts
# Sort the dataframe by rating_count in descending order
top_movies = ratings_grouped.sort_values(by='rating_count', ascending=False).head(5)

# Assuming movies_df is your dataframe created from "movies.csv"
# Merge with movies_df to get movie titles
result_df = pd.merge(top_movies, movies, on='movieId', how='inner')

# Select the relevant columns
selected_movies = result_df[['title', 'rating_count', 'rating_mean']]

print(selected_movies)


# In[242]:


# Assuming result_df is your dataframe with top movies, ratings, and genres
# Assuming 'genres' column contains information about movie genres
# Assuming you want to filter Sci-Fi movies
sci_fi_movies = result_df[result_df['genres'].str.contains('Sci-Fi')]

# Sort Sci-Fi movies by rating_count in descending order
sorted_sci_fi_movies = sci_fi_movies.sort_values(by='rating_count', ascending=False)

# Select the third most popular Sci-Fi movie
third_most_popular_sci_fi = sorted_sci_fi_movies.iloc[2]

print(third_most_popular_sci_fi['title'])


# In[243]:


top_most_popular_sci_fi = sorted_sci_fi_movies.iloc[2]
print(top_most_popular_sci_fi)


# In[193]:


ratings_grouped = df1.groupby('movieId')['rating'].agg(['count', 'mean']).reset_index()

print(ratings_grouped)


# In[237]:


filtered_movies = result_df[result_df['rating_count'] > 50]

print(filtered_movies)


# In[246]:


# Assuming result_df is your dataframe with top movies and ratings
filtered_movies = result_df[result_df['rating_count'] > 50]

print(filtered_movies)


# In[ ]:




