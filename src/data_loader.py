import csv

def load_transactions_from_csv(file_path):
    
    #Read data from CSV file and merge purchase records of the same member on the same day into a single transaction.
    
    
    # Use dictionary for grouping
    # Key: (Member_number, Date)
    # Value: List of items
    grouped_data = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            header = next(reader, None)

            for row in reader:
                # --- Data Cleaning ---
                
                # 1. Check column count: if a row has fewer than 3 columns, it is incomplete, skip it
                if not row or len(row) < 3:
                    continue
                
                # Trim whitespace
                member_id = row[0].strip()
                date = row[1].strip()
                item = row[2].strip()

                if not member_id or not date or not item:
                    continue

                # --- Grouping Algorithm ---
                key = (member_id, date)
                
                if key not in grouped_data:
                    grouped_data[key] = []
                
                grouped_data[key].append(item)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return []

    return list(grouped_data.values())