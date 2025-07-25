import pandas as pd

phish = pd.read_csv('verified_online.csv')
safe = pd.read_csv('safe_urls.csv')

sample_size = min(len(phish), len(safe))

phish_sample = phish.sample(n=sample_size, random_state=42)
safe_sample = safe.sample(n=sample_size, random_state=42)

combined = pd.concat([phish_sample, safe_sample], ignore_index=True)
combined = combined.sample(frac=1, random_state=42).reset_index(drop=True)

combined.to_csv('combined_balanced_test.csv', index=False)

print(f"✅ Balanced test dataset saved with {len(combined)} rows")
print(combined['verified'].value_counts())

