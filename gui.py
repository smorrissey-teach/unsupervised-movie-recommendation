import tkinter as tk
from tkinter import ttk

movies = [
    {"title": "Inception", "year": 2010, "rating": "8.8", "description": "A thief steals corporate secrets through dream-sharing technology."},
    {"title": "The Dark Knight", "year": 2008, "rating": "9.0", "description": "Batman faces the Joker in Gotham City."},
    {"title": "Interstellar", "year": 2014, "rating": "8.6", "description": "Explorers travel through a wormhole in space."},
    {"title": "The Shawshank Redemption", "year": 1994, "rating": "9.3", "description": "Two imprisoned men bond over decades."},
    {"title": "The Matrix", "year": 1999, "rating": "8.7", "description": "A hacker discovers reality is a simulation."},
    {"title": "Gladiator", "year": 2000, "rating": "8.5", "description": "A Roman general seeks revenge against a corrupt emperor."},
]

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

def display_movies(movie_list):
    # Clear old results
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    if not movie_list:
        ttk.Label(scrollable_frame, text="No results found.", padding=10).pack()
        return

    for movie in movie_list:
        card = ttk.Frame(scrollable_frame, padding=10, relief="ridge")
        card.pack(fill="x", padx=10, pady=5)

        title_label = ttk.Label(card, text=f"{movie['title']} ({movie['year']})", font=("Arial", 14, "bold"))
        title_label.pack(anchor="w")

        rating_label = ttk.Label(card, text=f"Rating: {movie['rating']}")
        rating_label.pack(anchor="w")

        desc_label = ttk.Label(card, text=movie['description'], wraplength=700)
        desc_label.pack(anchor="w")

def search_movies():
    query = search_entry.get().lower()
    filtered = [movie for movie in movies if query in movie["title"].lower()]
    display_movies(filtered)

search_button.config(command=search_movies)

display_movies(movies)

root.mainloop()