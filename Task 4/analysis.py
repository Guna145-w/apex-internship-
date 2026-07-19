import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("cleaned_cafe_sales.csv")

cash = df[df["payment_method"] == "Cash"]["total_spent"]
card = df[df["payment_method"] == "Card"]["total_spent"]

t_stat, p_value = ttest_ind(cash, card)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("There is a significant difference in average spending.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no significant difference in average spending.")