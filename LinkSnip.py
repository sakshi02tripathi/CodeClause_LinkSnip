import requests
import tkinter as tk

BITLY_ACCESS_TOKEN = "de53cdf7fe6457c12452d4da7b7bca17f0af0d2b"
def shorten_url():
    long_url = entry.get()
    api_endpoint = "https://api-ssl.bitly.com/v4/shorten"
    api_params = {
        "long_url": long_url
    }
    api_headers = {
        "Authorization": f"Bearer {BITLY_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(api_endpoint, headers=api_headers, json=api_params)
    if response.ok:
        data = response.json()
        short_url = data["link"]
        short_url_label.configure(text=f"Shortened URL: {short_url}")
    else:
        short_url_label.configure(text="Error: Failed to get shortened URL")

root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")
long_url_label = tk.Label(root, text="Enter the URL to be shortened:")
long_url_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()
button = tk.Button(root, text="Shorten URL", command=shorten_url)
button.pack()
short_url_label = tk.Label(root, text="")
short_url_label.pack()
root.mainloop()