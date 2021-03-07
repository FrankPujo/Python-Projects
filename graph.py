# o is the block the columns are made of
# e is a space and base is used in the lowest row of the graph
o = u"\u2588"
e = " "
base = 	"-"

# find highest value so the chart behaves correctly
def findHighest( arr, n ):
	highN = arr[0]
	for i in range(n):
		if arr[i] > highN:
			highN = arr[i]

	return highN

# returns an array used to print each single row, made of either a full block or an empty space
def setRow( cols, vals, high ):
	arr = []

	for x in range( cols ):
		if vals[x] > high - x:
			arr.append( o )
		else:
			arr.append( e )

	return arr

# Graph class called to create a graph
class Graph():
	def __init__( self, ids, values ):
		# useful values
		columnNums = len( ids )
		highestCol = findHighest( values, columnNums )

		# from the highest column print row by row the chart
		for i in range( highestCol ):
			sett = setRow( columnNums, values, highestCol )
			highestCol -= 1
			row = ""
			# add to the "row" array its correspondent component (space or block)
			for j in range( columnNums ):
				row += " "
				row += sett[j]
			print( row )
		print( base*(columnNums * 2 + 1 ) )

# sample graph
myIds = [ "a", "b", "c" ]
myValues = [ 1, 3, 2 ]
myGraph = Graph( myIds, myValues )

""" test (ignore)
print( " " + o )
print( " " + o )
print( base + o + base )
"""