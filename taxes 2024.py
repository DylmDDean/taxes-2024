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


amounts = ["100.00", "0.00", "500.00", "500.00", "700.00", "100.00", "600.00", "-300.00", "500.00", "-155.00", "-45.00", "100.00", "-25.00", "800.00", "500.00", "650.00", "137.00", "15.00", "-200.00", "500.00", "400.00", "100.00", "500.00", "20.00", "20.00", "564.00", "250.00", "1000.00", "-150.00", "750.00", "320.00", "400.00", "500.00", "-10.00", "250.00", "500.00", "400.00", "500.00", "765.00", "700.00", "500.00", "300.00", "500.00", "470.00", "700.00", "6.00", "500.00", "-30.00", "40.00", "-5.00", "50.00", "1050.00", "500.00", "500.00", "-20.00", "500.00", "50.00", "500.00", "100.00", "60.00", "60.00", "20.00", "650.00", "625.00", "600.00", "150.00", "150.00", "650.00", "150.00", "150.00", "1250.00"]


amounts = [float(amount.replace(',', '')) for amount in amounts if amount.replace('-', '').replace('.', '').replace(',', '').isdigit()]


positive_amounts = [amount for amount in amounts if amount >= 0]


total_sum_positive = sum(positive_amounts)


print("Total Sum of Positive Amounts:", total_sum_positive)
