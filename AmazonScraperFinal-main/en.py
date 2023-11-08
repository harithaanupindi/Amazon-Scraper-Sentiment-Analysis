import pandas as pd


encodings = ['ISO-8859-1']
filepath = 'C:/Users/Haritha/Downloads/AmazonScraperFinal-main/csv/amazon_reviews_Consolidated.xlsx'

for encoding in encodings:
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            lines = file.readlines()

        data = []
        for line in lines:
            try:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    data.append(parts)
            except Exception as e:
                print(f"Skipped a line due to an error: {str(e)}")

        df = pd.DataFrame(data, columns=['Name', 'Rating', 'Reviews'])
        print(df.head())
        print("CSV file successfully loaded with encoding:", encoding)
        break  # Exit the loop if successful
    except Exception as e:
        print(f"Could not read the file with encoding {encoding}: {str(e)}")

# Now, df contains the DataFrame with the data (if successful)
