import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

movies_df = pd.read_csv("movies.csv")

RATINGS_FILE = "user_ratings.csv"

if not os.path.exists(RATINGS_FILE):
    pd.DataFrame(columns=["movieId", "title", "rating"]).to_csv(RATINGS_FILE, index=False)


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


def open_movie_page(movie):
    """Open rating page for selected movie"""
    rating_window = tk.Toplevel(root)
    rating_window.title(movie["title"])
    rating_window.geometry("400x300")

    ttk.Label(
        rating_window,
        text=movie["title"],
        font=("Arial", 14, "bold")
    ).pack(pady=15)

    ttk.Label(
        rating_window,
        text=f"Genres: {movie['genres']}"
    ).pack(pady=5)

    ttk.Label(
        rating_window,
        text="Rate this movie:"
    ).pack(pady=10)

    rating_var = tk.IntVar()

    for i in range(1, 6):
        ttk.Radiobutton(
            rating_window,
            text=f"{i} ★",
            variable=rating_var,
            value=i
        ).pack(anchor="center")

    def submit_rating():
        rating = rating_var.get()

        if rating == 0:
            messagebox.showwarning("No Rating", "Please select a rating.")
            return

        ratings_df = pd.read_csv(RATINGS_FILE)

        if movie["movieId"] in ratings_df["movieId"].values:
            ratings_df.loc[
                ratings_df["movieId"] == movie["movieId"],
                "rating"
            ] = rating
        else:
            new_row = pd.DataFrame([{
                "movieId": movie["movieId"],
                "title": movie["title"],
                "rating": rating
            }])
            ratings_df = pd.concat([ratings_df, new_row], ignore_index=True)

        ratings_df.to_csv(RATINGS_FILE, index=False)

        messagebox.showinfo("Success", "Rating saved!")
        rating_window.destroy()

    ttk.Button(
        rating_window,
        text="Submit Rating",
        command=submit_rating
    ).pack(pady=15)


def display_movies(df):

    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    if df.empty:
        ttk.Label(scrollable_frame, text="No results found.", padding=10).pack()
        return

    for _, movie in df.head(50).iterrows():
        card = ttk.Frame(scrollable_frame, padding=10, relief="ridge")
        card.pack(fill="x", padx=10, pady=5)

        title_button = ttk.Button(
            card,
            text=movie["title"],
            command=lambda m=movie: open_movie_page(m)
        )
        title_button.pack(anchor="w")

        genre_label = ttk.Label(card, text=f"Genres: {movie['genres']}")
        genre_label.pack(anchor="w")


def search_movies():
    query = search_entry.get().strip()

    if not query:
        display_movies(movies_df)
        return

    filtered = movies_df[
        movies_df["title"].str.contains(query, case=False, na=False)
    ]
    display_movies(filtered)


search_button.config(command=search_movies)

display_movies(movies_df)

root.mainloop()