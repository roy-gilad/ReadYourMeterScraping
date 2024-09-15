from datetime import datetime, timedelta

# Get current date
current_date = datetime.now()

# Calculate the date 3 days ago
three_days_ago = current_date - timedelta(days=3)

# Format both dates as YYYY-MM-DD
current_date_str = current_date.strftime("%Y-%m-%d")
three_days_ago_str = three_days_ago.strftime("%Y-%m-%d")

# Print both dates
print(f"https://eu-customerportal-api.harmonyencoremdm.com/consumption/daily/179/{three_days_ago_str}/{current_date_str}")
