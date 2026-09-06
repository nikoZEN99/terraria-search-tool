import tkinter as tk
import webbrowser
import difflib
import time
# window
root = tk.Tk()
root.geometry("500x400")
root.title("nikoZEN99 terraria wiki")
root.config(bg="light green")

def search():
    que = search_entry.get()
    
    with open("terrarialist.txt", "r") as f:
        the_list = [line.strip() for line in f if line.strip()]
    matches = difflib.get_close_matches(que, the_list, n=1, cutoff=0.6)
    if matches:
        que = matches[0]
    webbrowser.open(f'https://terraria.wiki.gg/wiki/{que}')


# terraria wiki label
terraria_label = tk.Label(root, text="terraria wiki search", font=("Andy", 40), bg="light green")
terraria_label.pack(pady=10)

# label
search_label = tk.Label(root, text="search:", font=("Andy", 40), bg="light green")
search_label.pack(pady=10)

# search entry
search_entry = tk.Entry(root, font=("Andy", 20), width=25)
search_entry.pack(pady=10)

# submit button
submit_button = tk.Button(root, font=("Andy", 20), text="submit", command=search)
submit_button.pack(pady=10)

# label
output_label = tk.Label(root, font=("Andy", 40), bg="light green")
output_label.pack(pady=10)

root.mainloop()