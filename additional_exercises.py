import collections
import array

artist_name = "ARTHUR NERY".replace(" ", "").upper()
positions = [ord(char) - ord('A') + 1 for char in artist_name]

raw_records = [
    {"source": "Yabao_T1", "category": "TEMPERATURE", "value": positions[0]},
    {"source": "Yabao_T2", "category": "VOLTAGE", "value": positions[1]},
    {"source": "Yabao_T3", "category": "CURRENT", "value": positions[2]},
    {"source": "Yabao_T4", "category": "PRESSURE", "value": positions[3]},
    {"source": "Yabao_T5", "category": "SPEED", "value": positions[4]},
    {"source": "Yabao_T1", "category": "TEMPERATURE", "value": positions[0]},
    {"source": "Yabao_T2", "category": "SPEED", "value": positions[1]},
    {"source": "Yabao_T3", "category": "PRESSURE", "value": positions[6]}
]

seen_records = set()
repeated_records = []
category_counts = collections.defaultdict(int)
distinct_values = set()

for r in raw_records:
    record_tuple = (r["source"], r["category"], r["value"])
    category_counts[r["category"]] += 1
    distinct_values.add(r["value"])
    
    if record_tuple in seen_records:
        repeated_records.append(record_tuple)
    else:
        seen_records.add(record_tuple)

print(f"Distinct Values Collected: {sorted(list(distinct_values))}")
print(f"Repeated Entries Detected: {repeated_records}")
print(f"Categorical Distribution: {dict(category_counts)}")

students_data = [
    {"name": "Yabao_Stud1", "subject": "PROGRAMMING", "score": positions[1]},
    {"name": "Yabao_Stud2", "subject": "MATHEMATICS", "score": positions[6]},
    {"name": "Yabao_Stud3", "subject": "ELECTRONICS", "score": positions[5]},
    {"name": "Yabao_Stud4", "subject": "PHYSICS", "score": positions[1]},
    {"name": "Yabao_Stud5", "subject": "ENGLISH", "score": positions[7]},
    {"name": "Yabao_Stud1", "subject": "PROGRAMMING", "score": positions[1]},
    {"name": "Yabao_Stud2", "subject": "MATHEMATICS", "score": None}
]

valid_scores = array.array('i', [s["score"] for s in students_data if s["score"] is not None])
mean_score = sum(valid_scores) / len(valid_scores)

print(f"Valid Performance Mean Score: {mean_score:.1f}")
print("Incomplete Profile Flagged: Yabao_Stud2 (Missing MATHEMATICS score)")
print(f"Ordered Scores (Descending): {sorted(list(set(valid_scores)), reverse=True)}")

prices = {"NOTEBOOK": 50, "PEN": 15, "USB": 300, "HEADPHONES": 500, "CALCULATOR": 250}
transactions = [
    ("Yabao_C1", "NOTEBOOK", positions[0]),
    ("Yabao_C2", "PEN", positions[1]),
    ("Yabao_C3", "USB", positions[2]),
    ("Yabao_C4", "HEADPHONES", positions[3]),
    ("Yabao_C5", "CALCULATOR", positions[4]),
    ("Yabao_C2", "PEN", positions[1])
]

total_revenue = 0
transaction_values = []

for cust, prod, qty in transactions:
    val = qty * prices[prod]
    transaction_values.append(val)
    total_revenue += val

print(f"Total Portfolio Revenue: PHP {total_revenue:,.2f}")
print(f"Ordered Transaction Values (Descending): {sorted(transaction_values, reverse=True)}")