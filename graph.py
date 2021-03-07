# o is the block the columns are made of
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

def setRow( cols, vals, high ):
	arr = []

	for x in range( cols ):
		if vals[x] > high - x:
			arr.append( o )
		else:
			arr.append( e )

	return arr

class Graph():
	def __init__( self, ids, values ):
		# useful values
		columnNums = len( ids )
		highestCol = findHighest( values, columnNums )

		for i in range( highestCol ):
			sett = setRow( columnNums, values, highestCol )
			highestCol -= 1
			row = ""
			for j in range( columnNums ):
				row += " "
				row += sett[j]
			print( row )
		print( base*(columnNums * 2 + 1 ) )

# sample graph
myIds = [ "a", "b", "c" ]
myValues = [ 1, 2, 3 ]
myGraph = Graph( myIds, myValues )

# test
#print( " " + o )
#print( " " + o )
#print( base + o + base )