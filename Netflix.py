import sys
import os
import json
from math import sqrt

def process_movie (r, rating_list, w,MyAnswerCache, average_movie_ratings, customer_averages) :
	"""
	This method does all the main work.  It runs through the entire input file, looking
	for a : line, which will be the movie_id.  It then prints this out, and sets current_movie.
	If it encounters a movie_id, it first looks up the id in the AnswerCache, then creates
	a guess rating based off the average customer rating - a hard-coded value which is the 
	average of ALL movie ratings, then subtracts off the average for the current movie.
	return the rating_list which is our created list and the real_ratings list.
	"""
	assert len(rating_list) == 0
	current_movie = 0
	real_ratings = []
	for l in r:
		if ':' in l : #Movie 
			id_list = l.split('\n')
			w.write(id_list[0]+'\n')
			current_movie = l.split(':')
			current_movie = current_movie[0]
		else :
			cust_id = int(l)
			real_rating = MyAnswerCache[str(current_movie)][str(cust_id)]
			real_ratings.append(real_rating)
			cust_rating = customer_averages[l.strip()]
			cust_rating = cust_rating - (3.604289964420661 - average_movie_ratings[str(current_movie)])
			rating_list.append(eval("%0.1f" % cust_rating))
			w.write("%0.1f" % cust_rating + '\n')
	return rating_list,real_ratings

def read_input(r,w,MyAnswerCache, average_movie_ratings, customer_averages) :
	"""
	This method receives the cache files and calls process_movie to get ratings
	and then calls rmse to get the RMSE value for our ratings.  It then prints the 
	RMSE, rounded to 4 decimal digits to the writer.
	r is the reader (stdin)
	w is the writer (stdout)
	MyAnswerCache = Dictionary of actual answers from training data
	average_movie_ratings = Dictionary with key:movie_id and value: Average rating from population
	customer_averages = Dictionary with key:customer_id and value: Average of all customer's ratings
	"""
	rating_list = []
	rating_list, real_ratings= process_movie(r, rating_list, w,MyAnswerCache, average_movie_ratings, customer_averages)
	my_rmse = rmse_map_zip_sum(real_ratings,rating_list)
	w.write("RMSE: ")
	w.write("%0.4f" % my_rmse + '\n')
	return rating_list

def sqre_diff_2(x):
	"""
	Small function that computers difference and squares it.  Used with map.
	return integer
	"""
	return (x[0] - x[1]) ** 2
 
def rmse_map_zip_sum(a, p):
	"""
	Calculates the RMSE value for the real_ratings versus the actual_ratings
	a is a list for the real ratings.
	p is a list of our calcualted ratings.
	return the un-truncated float result.
	"""
	return sqrt((sum(map(sqre_diff_2, zip(a,p))))/len(a))

def netflix_solve(r, w) : 
	"""
	Opens the three cache files and calls read_input with the dictionary files.
	r is the reader (stdin)
	w is the writer (stdout)
	"""
	customer_averages = [] #Average reviews per customer
	with open("/u/mukund/netflix-tests/bryan-customer_cache.json") as f :
		customer_averages = json.load(f)
	average_movie_ratings = [] #This one has average ratings for all movies
	with open("/u/mukund/netflix-tests/rbrooks-movie_average_rating.json", "r") as f:
		average_movie_ratings = json.load(f)
	MyAnswerCache = [] #Contains actual answers to pull from
	with open("/u/mukund/netflix-tests/frankc-answer_cache.json", 'r') as f:
		MyAnswerCache = json.load(f)
	assert len(customer_averages) > 0
	assert len(average_movie_ratings) > 0
	assert len(MyAnswerCache) > 0
	read_input(r,w,MyAnswerCache, average_movie_ratings, customer_averages)