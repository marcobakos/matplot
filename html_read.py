# We can import data using lxml

from pandas import read_html
import pandas as pd
from pandas import Series, DataFrame

# Lets grab a url for list of failed banks
url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'


# Grab data from html and put it intop a list of DataFrame objects!
dframe_list = pd.io.html.read_html(url)

# Grab the first list item from the data base and set as a DataFrame
dframe = dframe_list[0]

# Show
print(dframe)
