import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 90)

###1 Імпорт та первинне дослідження:

url = "data/uk-500.csv"
df_origin = pd.read_csv(url)

COLUMNS_TO_DROP = []

print("\n---head-----")
print(df_origin.head())

print("\n---info-----")
print(df_origin.info())

print("\n---describe-----")
print(df_origin.describe())

print("\n---describe for str-----")
print(df_origin.describe(include=[object]).T)

print("\n---isnull----")
print(df_origin.isnull().sum())

print("\n---null----")
# print(df.isna().sum()) """перевіряємо на пропуски; якщо пропуски є, то виводимо команду нижче з сортуванням, щоб постише побиачитиб де вони є"""
print(df_origin.isna().sum().sort_values(ascending=False).head(20))

print("\n---duplicated-----")
print(df_origin.duplicated().sum())

print("\n---List columns-----")
# list_col = df.columns
# print(list(list_col))
for i, col in enumerate(df_origin.columns):
    print(f"{i:02d}. {col}")


###2 Очищення даних:

df = df_origin.copy()

if COLUMNS_TO_DROP:
    print("\n-----delete columns in list----")
    df = df.drop(columns=[col for col in COLUMNS_TO_DROP if col in df.columns], errors='ignore')

else:
    print("\nCOLUBNS_TO_DROP = []")

def standardize_text(s):
    if pd.isna(s):
        return np.nan
    
    if not isinstance(s, str):
        s = str(s)

    s = s.strip()
    s = " ".join(s.split())

    return s

possible_email_cols = [c for c in df.columns if "email" in c.lower()]
possible_web_cols = [c for c in df.columns if ("web" in c.lower() or "website" in c.lower() or "url" in c.lower())]
possible_phone_cols = [c for c in df.columns if ("phone" in c.lower() or "telephone" in c.lower() or "tel" in c.lower())]
possible_fax_cols = [c for c in df.columns if "fax" in c.lower()]

print('\nPossible columns: ')
print("Email cols:", possible_email_cols)
print("Web cols:", possible_web_cols)
print("Phone cols:", possible_phone_cols)
print("Fax cols:", possible_fax_cols)


#приміняємо зміни

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(standardize_text)

# email
for col in possible_email_cols:
    df[col] = df[col].str.lower()

# web
for col in possible_web_cols:
    df[col] = df[col].str.lower()

#