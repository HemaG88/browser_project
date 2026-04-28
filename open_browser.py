import webbrowser

url = input("Enter website: ")

if not url.startswith("http"):
    url = "https://" + url

webbrowser.open(url)