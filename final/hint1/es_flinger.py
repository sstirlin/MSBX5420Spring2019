import pandas as pd

# read in CSV
df = pd.read_csv('Online_Retail.csv')

# group by invoice num
invoice_groups = df.groupby('InvoiceNo')

# iterate over each group (each invoice)
for invoice_name, invoice in invoice_groups:
    basket = {}
    stockcodes = []
    descriptions = []
    quantities = []
    unitprices = []
    # iterate over rows in this invoice dataframe
    for row_index, row in invoice.iterrows():
        # these fields are the same for each row, so doesn't matter if we keep overwriting
        basket['InvoiceNo'] = row['InvoiceNo']
        basket['CustomerID'] = row['CustomerID']
        basket['InvoiceDate'] = row['InvoiceDate']
        basket['Country'] = row['Country']
        # these fields are different for each row, so we append to lists
        stockcodes.append(row['StockCode'])
        descriptions.append(row['Description'])
        quantities.append(row['Quantity'])
        unitprices.append(row['UnitPrice'])
    basket['StockCodes'] = stockcodes
    basket['Descriptions'] = descriptions
    basket['Quantities'] = quantities
    basket['UnitPrices'] = unitprices

    # now you should fling to elasticsearch!
    print(basket)
