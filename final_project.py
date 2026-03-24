from sklearn.neighbors import KNeighborsClassifier

print("=== AI Career Recommendation System ===\n")

# ------------------ USER INPUT ------------------
math = int(input("Math (0-10): "))
programming = int(input("Programming (0-10): "))
creativity = int(input("Creativity (0-10): "))
communication = int(input("Communication (0-10): "))
tech_interest = int(input("Tech Interest (0-10): "))
business_interest = int(input("Business Interest (0-10): "))

# ------------------ RULE-BASED AI ------------------
se_score = programming + tech_interest + math
ds_score = math + programming + (10 - creativity)
designer_score = creativity + communication
manager_score = communication + business_interest

scores = {
    "Software Engineer": se_score,
    "Data Scientist": ds_score,
    "Designer": designer_score,
    "Manager": manager_score
}

rule_career = max(scores, key=scores.get)

# Confidence
total = sum(scores.values())
confidence = (scores[rule_career] / total) * 100

# ------------------ MACHINE LEARNING ------------------
X = [
    [9, 9, 3, 4, 10, 2],
    [7, 8, 5, 6, 8, 4],
    [5, 4, 9, 7, 3, 6],
    [6, 5, 6, 9, 4, 8]
]

y = [
    "Software Engineer",
    "Data Scientist",
    "Designer",
    "Manager"
]

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

user = [[math, programming, creativity, communication, tech_interest, business_interest]]
ml_career = model.predict(user)[0]

# ------------------ FINAL OUTPUT ------------------
print("\n--- RESULTS ---")
print("Rule-Based Recommendation:", rule_career)
print("Confidence: {:.2f}%".format(confidence))
print("ML Recommendation:", ml_career)

# Final suggestion
if rule_career == ml_career:
    print("\nFinal Suggestion:", rule_career)
else:
    print("\nFinal Suggestion: Consider both", rule_career, "and", ml_career)
