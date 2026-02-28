import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "student": ["A","B","C","D","E","F","G","H","I","J","K","L"],
    "study_hours": [2,5,4,7,8,10,6,3,9,4,8,7],
    "sleep_hours": [8,6,7,5,4,6,7,5,3,6,5,8],
    "exam_score": [55,68,72,78,83,90,74,60,88,70,85,80]
}

df = pd.DataFrame(data)

# -------- Plot 1 --------
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="study_hours", y="exam_score", s=80)

z = np.polyfit(df["study_hours"], df["exam_score"], 1)
p = np.poly1d(z)
plt.plot(df["study_hours"], p(df["study_hours"]), color="red")

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.savefig("plot1.png")
plt.close()

# -------- Plot 2 --------
def bucket(hours):
    if hours <= 4:
        return "Low (0–4)"
    elif hours <= 7:
        return "Medium (5–7)"
    else:
        return "High (8+)"

df["study_bucket"] = df["study_hours"].apply(bucket)

plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x="sleep_hours",
    y="exam_score",
    hue="study_bucket",
    palette={"Low (0–4)": "blue", "Medium (5–7)": "green", "High (8+)": "orange"},
    s=80
)

plt.title("Sleep Hours vs Exam Score")
plt.xlabel("Sleep Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.savefig("plot2.png")
plt.close()
