import tkinter as tk
from tkinter import ttk
import pandas as pd

movies_df = pd.read_csv("movies.csv")

root = tk.Tk()
root.title("Movie Search Results")
root.geometry("800x600")

search_frame = ttk.Frame(root, padding=10)
search_frame.pack(fill="x")

search_label = ttk.Label(search_frame, text="Search Movies:")
search_label.pack(side="left")

search_entry = ttk.Entry(search_frame, width=40)
search_entry.pack(side="left", padx=10)

search_button = ttk.Button(search_frame, text="Search")
search_button.pack(side="left")

results_frame = ttk.Frame(root)
results_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(results_frame)
scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


def display_movies(df):

    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    if df.empty:
        ttk.Label(scrollable_frame, text="No results found.", padding=10).pack()
        return

    for _, movie in df.head(50).iterrows():
        card = ttk.Frame(scrollable_frame, padding=10, relief="ridge")
        card.pack(fill="x", padx=10, pady=5)


        title_label = ttk.Label(
            card,
            text=movie["title"],
            font=("Arial", 12, "bold")
        )
        title_label.pack(anchor="w")

        genre_label = ttk.Label(card, text=f"Genres: {movie['genres']}")
        genre_label.pack(anchor="w")


def search_movies():
    query = search_entry.get().strip()

    if not query:
        display_movies(movies_df)
        return

    filtered = movies_df[movies_df["title"].str.contains(query, case=False, na=False)]
    display_movies(filtered)


search_button.config(command=search_movies)

display_movies(movies_df)

root.mainloop()