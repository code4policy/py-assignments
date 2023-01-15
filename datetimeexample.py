#Python 3-4

from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
print(date_str)



#This is the try it homework

from datetime import datetime

raw_date = "01-May-12"
date_format = "%d-%b-%y"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17
print(date_str)