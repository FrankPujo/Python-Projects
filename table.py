# table elements
# REMEMBER: to repeat use line*x or space*x
divide = "|"
line = "-"
inter = "+"
space = " "

# print row with content inside
def contentRow( columns, lenght, cellsTexts ):
	row = ""

	return row

def lineRow( columns, lenght ):
	row = divide
	for number in range( columns ):
		print( "something" )

	return row

class Table():
	def __init__( self, titles, rows ):
		
		# number of columns
		colNums = len( titles )
		print( colNums )

		# TO DO 
		# find longest string
		# cal row functions with the just-found number
		# 

		"""
		for column in range( self.columns ):
			# idk
			title = titles[column]
			content = []
			for row in rows:
				content.append( row )
			print ( title )
			#for x in range( len( content ) ):
				#for y in range ( self.columns ):
					
				#print( content[x] )
				#for y in range( len( content[x] ) ):
					#print( content[x][y] )
		"""

# sample table
myTitles = [ "Title1", "Title2" ]
firstRow = [ "Stuff", "moore!" ]
secondRow = [ "Again", "and Again!!" ]
myRows = [ firstRow, secondRow ]
myTable = Table( myTitles, myRows )