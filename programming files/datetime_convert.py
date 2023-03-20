#import packages
from datetime import datetime

#create the date string
date_str = "2022-03-17 10:45:30"
#create the date object
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
#format the date object
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')
#print the formatted date
print(formatted_date)
