def keylogger():
    print("Educational Keylogger (Consent Based)")
    print("Type something. Press ENTER to stop.\n")

    keys = input("Start typing: ")

    with open("keylog.txt", "w") as file:
        for key in keys:
            file.write(key)

    print("\nKeystrokes saved to keylog.txt")


# -------- MAIN --------
keylogger()
