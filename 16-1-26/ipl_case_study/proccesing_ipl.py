import pandas as pd
df=pd.read_csv("16-1-26\ipl_case_study\ipl_data.csv")
print(df.columns)
print(df.isnull().sum())
print(df.info())
print(df["match_id"].fillna(549,inplace=True))
print(df.isnull().sum())
print(df["season"].fillna(df["season"].mode()[0],inplace=True))
print(df.isnull().sum())
print(df["city"].fillna(df["city"].mode()[0],inplace=True))
print(df.isnull().sum())
print(df["team1"].fillna("unknown",inplace=True))
print(df.isnull().sum())
print(df["team2"].fillna("unknown",inplace=True))
print(df["winning_team"].fillna("unknown",inplace=True))
print(df.isnull().sum())
print(df["player_of_match"].fillna("unknown",inplace=True))
print(df.isnull().sum())

print(df["venue"].fillna(df["venue"].mode()[0],inplace=True))
print(df.isnull().sum())
print(df["runs_scored"].fillna(df["runs_scored"].mean(),inplace=True))
print(df.isnull().sum())
print(df["wickets"].fillna(df["wickets"].median(),inplace=True))
print(df.isnull().sum())
#matchs per season
print(df["season"].value_counts())
#top match count
print("topmatch count season",df["season"].value_counts().idxmax)
#total match won by each team
print("total match won by each team",df["winning_team"].value_counts())
# avg runs per season
print(df.groupby("season")["runs_scored"].mean())
# venu _wise match count
print(df["venue"].value_counts())
# venue wise avg runs
print(df.groupby("venue")["runs_scored"].mean())
# city_wise match count
print(df["city"].value_counts())
# city_wise avg runs
print(df.groupby("city")["runs_scored"].mean())
# which winnig_team has the highest aveg runs
print(df.groupby("winning_team")["runs_scored"].mean().idxmax())
#top 3 match
print(df.head(3))
