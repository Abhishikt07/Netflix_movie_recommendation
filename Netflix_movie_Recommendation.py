import re
import ast
import pickle
 
import numpy as np
import pandas as pd 
import streamlit as st 

import nltk 
from nltk.stem.porter import PorterStemmer 
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings('ignore')

movies = pd.read_csv(r"D:\VS code\Netflix_movie_recommend\tmdb_5000_movies.csv")
credit = pd.read_csv(r"D:\VS code\Netflix_movie_recommend\tmdb_5000_credits.csv")

print(movies.head())
print(credit.head())

print(movies.shape)
print(credit.shape)

#Merging the two data frame 
movies = movies.merge(credit, on ='title')
print(movies.shape)
print(movies.columns)

#choosing relevent features : movie_id,title, overview, genres, keyword,cast,crew
df = movies[['id','title','overview','genres','keywords','cast','crew']]
print(df.head(2))
print(df.shape)

#Final goal - movie_id, name, tags
#Start transforming 1 by 1 feature
#Genres
def fetch_genres(text):
    l = []
    for i in ast.literal_eval(text):
        l.append(i['name'])

    return l
print(fetch_genres(df['genres'][1]))
df['genres'] = df['genres'].apply(fetch_genres)
print(df['genres'])

#Keywords
def fetch_keywords(text):
    l = []
    for i in ast.literal_eval(text):
        l.append(i['name'])

    return l
print(fetch_keywords(df['keywords'][1]))
df['keywords'] = df['keywords'].apply(fetch_keywords) 
print(df['keywords'])

#Cast
def fetch_cast (text):
    l = []
    counter = 0
    for i in ast.literal_eval (text):
        if counter != 3:
            l.append(i['name'])
            counter += 1
        else:
            break
    return l 
     
print(fetch_cast(df['cast'][1]))
df['cast'] = df['cast'].apply(fetch_cast)
print(df)

#Crew
def fetch_director (text):
    l = []
    for i in ast. literal_eval(text):   
        if i['job'] == 'Director': 
            l.append(i['name'])
    return l

print(fetch_director(df['crew'][3]))
df['crew'] = df['crew'].apply(fetch_director)
print(df)

#Overview
print(df.isnull().sum())
print(df.shape)
df.dropna(inplace = True)
print(df.shape)
print(df.isnull().sum())

df['overview'] = df['overview'].apply(lambda x : x.split())
print(df['overview'])

#Adding all related terms in one single term called "Tag"
df['tags'] = df['overview']+df['genres']+df['keywords']+df['cast']+df['crew']
data = df[['id', 'title', 'tags']]
print(data)


# print('I am a boy'.replace(' ', ''))
data['tags'] =  data['tags'].apply(lambda x: [i.replace(' ', '')for i in x])
print(data['tags'][0])

data['tags'] =  data['tags'].apply(lambda x:" ".join(x))
print(data['tags'][0])

#Text preprocess function
ps = PorterStemmer()
def preprocess_text(text):
    new_text = []
    for i in text.split():
        lower = i.lower()
        new_text.append(ps.stem(lower))
    
    return " ".join(new_text)
    
# print(preprocess_text(data['tags'][0]))
data['tags'] = data['tags'].apply(preprocess_text)
print(data)

#BOW (Bag of Words)
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(data['tags']).toarray()
print(vectors)
for i in cv.get_feature_names_out():
    print(i)

similarity = cosine_similarity(vectors)
print(similarity[0])
print(sorted(enumerate(similarity[0]), reverse=True, key= lambda x: x[1])[1:6])
print(data.iloc[1214])

#Final Function 
def recommend(movie):
    movie_index = data[data['title'] == movie].index[0]
    distance =  similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key= lambda x: x[1])[1:6]
    
    for i in movie_list:
        print(data.iloc[i[0]].title)

recommend('Iron Man')

#Pickle Module
pickle.dump(data.to_dict(), open ('movies_dict.pkl', mode='wb'))
pickle.dump(similarity, open ('similarity.pkl', mode='wb'))
