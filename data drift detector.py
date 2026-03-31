import pandas as pd
import numpy as np

def detect_drift(df_old, df_new):
    report = {}

    # 1. Column changes
    old_cols = set(df_old.columns)
    new_cols = set(df_new.columns)

    report['columns_added'] = list(new_cols - old_cols)
    report['columns_removed'] = list(old_cols - new_cols)

    # 2. Null comparison
    null_old = df_old.isnull().mean()
    null_new = df_new.isnull().mean()

    null_diff = (null_new - null_old).sort_values(ascending=False)
    report['null_spike'] = null_diff[null_diff > 0.1]

    # 3. Numeric distribution drift
    numeric_cols = df_old.select_dtypes(include=np.number).columns
    drifted_cols = {}

    for col in numeric_cols:
        if col in df_new.columns:
            mean_old = df_old[col].mean()
            mean_new = df_new[col].mean()

            if mean_old != 0:
                change = abs(mean_new - mean_old) / abs(mean_old)
                if change > 0.2:  # 20% change threshold
                    drifted_cols[col] = {
                        'old_mean': mean_old,
                        'new_mean': mean_new,
                        'pct_change': change
                    }

    report['distribution_drift'] = drifted_cols

    return report


# Example usage
df_yesterday = pd.read_csv("data_2026_03_30.csv")
df_today = pd.read_csv("data_2026_03_31.csv")

drift_report = detect_drift(df_yesterday, df_today)

print("DRIFT REPORT:")
for k, v in drift_report.items():
    print(f"\n{k}:")
    print(v)