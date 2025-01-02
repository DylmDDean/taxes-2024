import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\dmdmd\Downloads\taxes-2025.json', scope)
client = gspread.authorize(creds)

# Replace with the actual URL of your Google Sheet
sheet = client.open_by_url('')

# Select the first worksheet
worksheet = sheet.get_worksheet(0)

# Extract all values from the worksheet
data = worksheet.get_all_values()

# Print the data
for row in data:
    print(row)

import pandas as pd

columns = ['Date', 'ID', 'Type', 'Currency', 'Amount', 'Fee', 'Net Amount', 'Status', 'Note', 'Description', 'Completion Status', 'Category', 'Reference', 'Balance'] 
df = pd.DataFrame(data, columns=columns)

df_filtered = df[df['Type'] != 'Withdrawal']

print(df_filtered)

completed_transactions = df[df['Completion Status'] == 'COMPLETE']

total_amount = df_filtered['Amount'].sum()


amounts = [""]


amounts = [float(amount.replace(',', '')) for amount in amounts if amount.replace('-', '').replace('.', '').replace(',', '').isdigit()]


positive_amounts = [amount for amount in amounts if amount >= 0]


total_sum_positive = sum(positive_amounts)


print("Total Sum of Positive Amounts:", total_sum_positive)
