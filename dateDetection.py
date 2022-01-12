# dateDetection.py
'''
Write a regex that can detectdates in DD/MM/YYYY format.
Assume days range from 01 to 32, months range from 01 to 12,
and years range from 1000 to 2999.

Regex will take any date even if incorrect like 31/02/2020 or 31/04/2021,
it will store these strings into variables and named month,day,year and then
write additional code to validate date
date rules:
April,June, September, and November have 30 days
February has 28 days
The rest have 31 days
During leap year, February has 29 days
	Leap years are every year that is evenly divisible by 4,
		except for years evenly divisible by 100,
		unless the year is also evenly divisible by 400
'''

import re, pyperclip

message = str(pyperclip.paste())

# use regex to get dates
dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
dates = dateRegex.findall(message)

validDates = []
# validate using if statements
while True:
	for group in dates:
		valid = True
		# years
		if int(group[2])>2999 or int(group[2])<1000:
			valid = False
		# months
		elif int(group[1])>12 or int(group[1])<=0:
			valid = False
		# days
		elif int(group[0])<=31 or int(group[0])>0:
			# april, june, september, and november have 30 days
			if (int(group[1])==4 or int(group[1])==6 or int(group[1])==9 or int(group[1])==11) and int(group[0])>30:
				valid=False
			# february with leap years included
			elif int(group[1])==2:
				if int(group[0])>29:
					valid=False
				elif int(group[0])==29 and int(group[2])%4==0: # if leap year and 29 days
					if group[2]%100==0 and int(group[2])%400!=0:				# if leap year is divisible by 100, it's not valid
						valid=False										# if leap year is divisible by 400, it's valid
				elif int(group[0])>28 and int(group[2])%4!=0:	# if feb is greater than 28 days and not leap year, its not valid
					valid = False
		elif int(group[0])>31 or int(group[0])<0:
			valid=False
		if valid==True:
			validDates.append(group[0]+'/'+group[1]+'/'+group[2])
	break

# plug in validDates to clipboard to be pasted
if len(validDates)>0:
	pyperclip.copy('\n'.join(validDates))
	print('The dates you have copied are:')
	for dates in validDates:
		print(''.join(dates))
else:
	print('You have not copied any valid dates.')



