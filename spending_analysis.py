import csv

def read_data(filename):
    data = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['amount'] = float(row['amount'])
            data.append(row)
    return data

def total_spending(data):
    return sum(item['amount'] for item in data)

def spending_by_category(data):
    categories = {}
    for item in data:
        category = item['category']
        amount = item['amount']
        categories[category] = categories.get(category, 0) + amount
    return categories

def highest_category(categories):
    return max(categories, key=categories.get)

def category_percentages(categories, total):
    percentages = {}
    for category, amount in categories.items():
        percentages[category] = (amount / total) * 100
    return percentages

def average_daily_spending(data):
    dates = set(item['date'] for item in data)
    total = total_spending(data)
    return total / len(dates)

def main():
    data = read_data("spending_data.csv")

    total = total_spending(data)
    categories = spending_by_category(data)
    top_category = highest_category(categories)
    percentages = category_percentages(categories, total)
    avg_daily = average_daily_spending(data)

    print("n\SPENDING ANALYSIS REPORT\n")
    print(f"Total Spending: ${total:.2f}\n")

    print("Spending by Category:")
    for category, amount in categories.items():
        print(f"- {category}: ${amount:.2f} ({percentages[category]:.2f}%)")

    print(f"\nHighest Spending Category: {top_category}")
    print(f"Average Daily Spending: ${avg_daily:.2f}")

if __name__ == "__main__":
    main()