import webbrowser

print("1. Open Google")
print("2. Open YouTube")
print("3. Open GitHub")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    webbrowser.open("https://www.google.com")
elif choice == "2":
    webbrowser.open("https://www.youtube.com")
elif choice == "3":
    webbrowser.open("https://github.com")
else:
    print("Invalid choice")