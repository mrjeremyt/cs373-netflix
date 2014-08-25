#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
import json

from Netflix import process_movie, read_input , netflix_solve, rmse_map_zip_sum, sqre_diff_2

# -----------
# TestCollatz
# -----------
customer_averages = []
with open("/u/mukund/netflix-tests/bryan-customer_cache.json") as f :
	customer_averages = json.load(f)
average_movie_ratings = []
with open("/u/mukund/netflix-tests/rbrooks-movie_average_rating.json", "r") as f:
	average_movie_ratings = json.load(f)
MyAnswerCache = []
with open("/u/mukund/netflix-tests/frankc-answer_cache.json", 'r') as f:
	MyAnswerCache = json.load(f)

class TestNetflix (TestCase) :
	global customer_averages, average_movie_ratings, MyAnswerCache
    # ----
    # rmse
    # ----

	def test_rmse_1 (self) :
		a = [4, 5, 6]
		b = [4, 5, 6]
		c = rmse_map_zip_sum(a,b)
		self.assertEqual(c,0)

	def test_rmse_2 (self) : 
		a = [5, 5, 5]
		b = [6, 6, 6]
		c = rmse_map_zip_sum(a,b)
		self.assertEqual(c,1)

	def test_rmse_3 (self) :
		a = [5, 10]
		b = [10, 15]
		c = rmse_map_zip_sum(a,b)
		self.assertEqual(c,5)

	def test_rmse_4 (self) :
		a = [5]
		b = [5]
		c = rmse_map_zip_sum(a,b)
		self.assertEqual(c,0)

	def test_rmse_5 (self) :
		a = [5.0]
		b = [5.0]
		c = rmse_map_zip_sum(a,b)
		self.assertEqual(c,0)	

    # ----
    # square_diff
    # ----

	def test_sqdiff_1 (self) :
		a = [4,2]
		b = sqre_diff_2(a)
		self.assertEqual(b,4)

	def test_sqdiff_2 (self) :
		a = [1,1]
		b = sqre_diff_2(a)
		self.assertEqual(b,0)

	def test_sqdiff_3 (self) :
		a = [5,7]
		b = sqre_diff_2(a)
		self.assertEqual(b,4)	

	# ----
    # process_movie
    # ----

	def test_process_1 (self) : 	
		rating_list = []
		real_ratings = []
		r = StringIO("1:\n30878\n2647871\n1283744")
		w = StringIO()
		rating_list, real_ratings = process_movie(r,rating_list,w,MyAnswerCache, average_movie_ratings, customer_averages)
		self.assertEqual(rating_list, [3.8,3.4,3.7])

	def test_process_2 (self) :  	
		rating_list = []
		real_ratings = []
		r = StringIO("1:\n30878\n")
		w = StringIO()
		rating_list, real_ratings = process_movie(r,rating_list,w,MyAnswerCache, average_movie_ratings, customer_averages)
		self.assertEqual(rating_list, [3.8])

	def test_process_3 (self) :   	
		rating_list = []
		real_ratings = []
		r = StringIO("10015:\n2405069\n2378764\n")
		w = StringIO()
		rating_list, real_ratings = process_movie(r,rating_list,w,MyAnswerCache, average_movie_ratings, customer_averages)
		self.assertEqual(rating_list, [3.7,4.2])

	def test_process_4 (self) :  	
		rating_list = []
		real_ratings = []
		r = StringIO("10012:\n2445069\n1483604\n")
		w = StringIO()
		rating_list, real_ratings = process_movie(r,rating_list,w,MyAnswerCache, average_movie_ratings, customer_averages)
		self.assertEqual(rating_list, [3.1,4.0])

	# ----
    # read_input
    # ----

	def test_input_1 (self) :
		r = StringIO("10:\n1531863\n")
		w = StringIO()
		read_input(r,w,MyAnswerCache,average_movie_ratings,customer_averages)
		self.assertEqual(w.getvalue(), "10:\n2.7\nRMSE: 0.3000\n")

	def test_input_2 (self) :
		r = StringIO("10:\n1531863\n")
		w = StringIO()
		c = read_input(r,w,MyAnswerCache,average_movie_ratings,customer_averages)
		self.assertEqual(c, [2.7])

	def test_input_3 (self) :
		r = StringIO("10012:\n2445069\n1483604\n")
		w = StringIO()
		read_input(r,w,MyAnswerCache,average_movie_ratings,customer_averages)
		self.assertEqual(w.getvalue(), "10012:\n3.1\n4.0\nRMSE: 0.0707\n")

	def test_input_4 (self) :
		r = StringIO("10012:\n2445069\n1483604\n")
		w = StringIO()
		c = read_input(r,w,MyAnswerCache,average_movie_ratings,customer_averages)
		self.assertEqual(c, [3.1,4.0])

	def test_input_5 (self) :    	
		r = StringIO("1:\n30878\n")
		w = StringIO()
		c = read_input(r, w, MyAnswerCache, average_movie_ratings, customer_averages)
		self.assertEqual(c, [3.8])

	def test_input_6 (self) :   	
		r = StringIO("1:\n30878\n")
		w = StringIO()
		read_input(r, w, MyAnswerCache, average_movie_ratings, customer_averages)
		self.assertEqual(w.getvalue(), "1:\n3.8\nRMSE: 0.2000\n")


	# ----
    # netflix_solve
    # ----

	def test_solve_1 (self) :
		r = StringIO("10:\n1531863\n")
		w = StringIO()
		netflix_solve(r,w)
		self.assertEqual(w.getvalue(), "10:\n2.7\nRMSE: 0.3000\n")

# ----
# main
# ----

main()