#Take Questions from Lecture

#Explain Plan

	- teach CSV writer
	- review output of dict, items values keys
	- break into groups and start breaking down problem into steps; compare possible strategies for completing assignment

#Dict outputs

	- to review, you can dump the items in a dictionary into a list of items or a list of tuples
	- .values(), .keys(), .items()
	- for example use FreqDist(text1.tokens) from nltk.book

#CSV Writer

	- outputting to CSV is made easy by the CSV Writer tool in Python
	- import it like you import any other module:
	
`        import csv
	
	- open the file; for good measure, write the close function too

`        csvf = open('ww_class.csv','w')
`        csvf.close()

	- create a *writer object*, which will be an object you can use to write things to a csv using specific commands like "writerow"
'''
		cwrite = csv.writer(csvf)
		for n in new_list:
		    csvf.writerow(n[0],n[1])
'''

	- the above assumes that new_list is a list of 2-part elements



