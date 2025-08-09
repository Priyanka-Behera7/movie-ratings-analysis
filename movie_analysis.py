import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("movies.csv")

# Fill missing values
df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean())
df['Metascore'] = df['Metascore'].fillna(df['Metascore'].mean())

# 1. Average rating by genre
avg_rating_by_genre = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
avg_rating_by_genre.plot(kind='bar', color='skyblue')
plt.title('Average Movie Rating by Genre')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.savefig("output_screenshots/avg_rating_by_genre.png")
plt.close()

# 2. Movies released each year
movies_per_year = df['Year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
sns.lineplot(x=movies_per_year.index, y=movies_per_year.values, marker='o')
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.savefig("output_screenshots/movies_per_year.png")
plt.close()

# 3. Top 10 highest-grossing movies
top_grossing = df.sort_values(by='Revenue (Millions)', ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x='Revenue (Millions)', y='Title', data=top_grossing, palette='viridis')
plt.title('Top 10 Highest Grossing Movies')
plt.xlabel('Revenue (Millions USD)')
plt.ylabel('Movie Title')
plt.savefig("output_screenshots/top_grossing.png")
plt.close()

# 4. Budget vs Revenue correlation
if 'Budget (Millions)' in df.columns:
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='Budget (Millions)', y='Revenue (Millions)', data=df)
    plt.title('Budget vs Revenue')
    plt.xlabel('Budget (Millions USD)')
    plt.ylabel('Revenue (Millions USD)')
    plt.savefig("output_screenshots/budget_vs_revenue.png")
    plt.close()

# 5. Top rated movies (min 100k votes)
top_rated = df[df['Votes'] > 100000].sort_values(by='Rating', ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x='Rating', y='Title', data=top_rated, palette='coolwarm')
plt.title('Top 10 Rated Movies')
plt.xlabel('IMDb Rating')
plt.ylabel('Movie Title')
plt.savefig("output_screenshots/top_rated.png")
plt.close()

print("Analysis completed. Graphs saved in output_screenshots folder.")
