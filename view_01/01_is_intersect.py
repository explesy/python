#!/usr/bin/python3

def is_intersect(rect_one, rect_two):
	""" Check intersection of two rectangles. """

	#  r2_x1 < r1_x1 < r2_x2 or r2_x1 < r1_x2 < r2_x2
	print(rect_two[0][0], rect_one[0][0], rect_two[1][0], rect_two[0][0], rect_one[1][0], rect_two[1][0]) 
	if((rect_two[0][0] < rect_one[0][0] < rect_two[1][0]) or (rect_two[0][0] < rect_one[1][0] < rect_two[1][0]) ):
		#  r2_y2 < r1_y1 < r2_y1 or r2_y2 < r1_y2 < r2_y1
		print(rect_two[1][1], rect_one[0][1], rect_two[0][1], rect_two[1][1], rect_one[1][1], rect_two[0][1])
		if((rect_two[1][1] < rect_one[0][1] < rect_two[0][1]) or (rect_two[1][1] < rect_one[1][1] < rect_two[0][1]) ):
			return True
	return False

def test():
	rectangle_one = ((1,3), (6,1))
	rectangle_two = ((5,6), (8,2))

	print(is_intersect(rectangle_one, rectangle_two))


test()

