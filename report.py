import requests, pandas as pd

# vars
src_filename = 'owid-covid-latest.csv'
dst_filename = 'table.html'
dst_path = 'public/'
url = 'https://covid.ourworldindata.org/data/latest/' + src_filename

# Define lists with the fields and required country names
fieldnames = ['location', 'new_cases', 'total_cases', 'new_vaccinations', 'total_vaccinations']
countrynames = ['Ukraine', 'Poland', 'Denmark', 'Switzerland', 'United States']

# Download the latest data OWID dataset 
r = requests.get(url, allow_redirects=True)
open(src_filename, 'wb').write(r.content)

# Read CSV specific columns
df = pd.read_csv(src_filename, usecols = fieldnames)

# Filter rows when matches one of the values on countrynames list
boolean_series = df.location.isin(countrynames)
filtered_df = df[boolean_series]

# Write the output to dest_filename
print(filtered_df)
# filtered_df.to_csv(dst_path + dst_filename, sep=',', index=False) 
filtered_df.to_html(dst_path + dst_filename, index=False)
# print(filtered_df.to_html())