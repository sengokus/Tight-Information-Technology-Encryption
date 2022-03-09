import os, sys
# adds a path where the program can import added modules
sys.path.append(os.path.dirname("Modules/"))
from tkinter import *
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
from vigenereCipher import encryption, decryption, alphabet

# MAIN MENU
# main window that user interacts with
window = Tk()
window.configure(bg = "#1e222b")
window.geometry("225x120")
window.resizable(False, False)
logo = PhotoImage(file = "logo.gif")
window.iconphoto(True, logo)
window.title("T.I.T.E. v0.69")
Label(window, text = "Welcome to T.I.T.E. v0.69!", font = ("Helvetica", 10,"bold"), fg = "white", bg = "#1e222b").grid(columnspan = 3, sticky = N, ipadx = 30, ipady = 15)

# OPENING NEW WINDOWS
# encryption window
def EncryptionWindow():
    encryptionWindow = Toplevel(window)
    encryptionWindow.configure(bg = "#1e222b")
    encryptionWindow.title("Encryption")
    encryptionWindow.resizable(False, False)
    encryptionWindow.geometry("200x100")

    # FILE SELECTION IN DROPDOWN LAYOUT
    files = [] # initializes files as a list

    for file in os.listdir(os.getcwd()+"/1. Source"):
        # appends the txt file names to the list "files"
        if file.endswith(".txt"):
            files.append(os.path.join(file))

    # label for file select
    # autofill search input
    fileselect_label = Label(encryptionWindow, text = "File Select:", bg = "#1e222b", fg = "white")
    filename = AutocompleteCombobox(encryptionWindow, width = 15, completevalues = files, )
    # file reading
    def read_file():
        file_content= [i for i in (open(os.getcwd() + '\\1. Source\\' + filename.get()).read())]
        return file_content

    # keyword label and entry
    keyword_label = Label(encryptionWindow, text = "Keyword:", bg = "#1e222b", fg = "white")
    entry = Entry(encryptionWindow, width = 18)

    def export():
        # initializing versions
        encrypted_versions = []
        version_nums = []
        version = 0

        # write to new text file
        # validation
        valid_input = True
        if entry.get() == "" or filename.get() not in files:
            valid_input = False

        for i in entry.get():
            if i not in alphabet:
                valid_input = False

        # if invalid inputs
        if not valid_input:
            messagebox.showinfo(title = "Error", message = "Input not valid!")
        
        else:
            valid_file_content = True

            # select text file
            file_content = read_file()

            # adds all the names of the encrypted text files from the same source to a list
            for file in os.listdir(os.getcwd()+"/2. Encrypted"):
                if file.endswith(".txt") and filename.get().removesuffix(".txt") in file:
                    encrypted_versions.append((os.path.join(file)).removesuffix(".txt"))

            # increases the version number of the resulting text file according to the number of encrypted versions of the source file
            for i in encrypted_versions:
                if not encrypted_versions:
                    version += 1
                else:
                    version_nums.append((i.replace(filename.get().removesuffix(".txt")+"_Encrypted","").replace("(","").replace(")","")))
                    version = int(max(version_nums)) + 1

            # checks for invalid characters in the source text file
            for i in file_content:
                if i not in alphabet:
                    valid_file_content = False

            # if invalid character found in file
            if not valid_file_content:
                messagebox.showinfo(title = "Error", message = "Invalid character in text file!")

            else:
                # write to new text file
                file = open(os.getcwd() + "\\2. Encrypted\\" + (filename.get().removesuffix(".txt")) + "_Encrypted" + "(" + str(version) + ")" + ".txt", "w+")
                file.write(encryption(file_content, entry.get()))

                # save keywords
                keyword_saves = open(os.getcwd() + "\\4. Key Storage\\Keys.txt", "a+")
                keyword_saves.write("\n" + (filename.get().removesuffix(".txt")) + "_Encrypted" + "("+str(version) + ")" + " = " + entry.get())

                # success message
                messagebox.showinfo(title = "Success", message = "Encryption successful!")
                encryptionWindow.destroy()

    encrypt = Button(encryptionWindow, text = "Encrypt", command = export, bg = "#495569", fg = "white", width = 10)

    # LAYOUT
    # file select
    fileselect_label.grid(row = 3, column = 1, pady = 3)
    filename.grid(row = 3, column = 2, pady = 2)
    # keyword and entry
    keyword_label.grid(row = 4, column = 1, pady = 3)
    entry.grid(row = 4, column = 2, pady = 2)
    # encrypt button
    encrypt.grid(row = 5, column = 2, pady = 7)

# decryption window
def DecryptionWindow():
    decryptionWindow = Toplevel(window)
    decryptionWindow.configure (bg = "#1e222b")
    decryptionWindow.title("Decryption")
    decryptionWindow.resizable(False, False)
    decryptionWindow.geometry("200x100")

    # FILE SELECTION IN DROPDOWN LAYOUT
    files = [] # initializes files as a list
    file_content = [] # initializes text within file as a list

    for file in os.listdir(os.getcwd()+"/2. Encrypted"):
        # appends the txt file names to the list "files"
        if file.endswith(".txt"):
            files.append(os.path.join(file))

    # label for file select
    # autofill search input
    fileselect_label = Label(decryptionWindow, text = "File Select:", bg = "#1e222b", fg = "white")
    filename = AutocompleteCombobox(decryptionWindow, width = 15, completevalues = files)

    # file reading
    def read_file():
        file_content.append(open(os.getcwd() + '\\2. Encrypted\\' + filename.get()).read())

    # keyword label and entry
    keyword_label = Label(decryptionWindow, text = "Keyword:", bg = "#1e222b", fg = "white")
    entry = Entry(decryptionWindow, width = 18)

    def export():
        # validation
        valid_input = True
        if entry.get() == "" or filename.get() not in files:
            valid_input = False

        for i in entry.get():
            if i not in alphabet:
                valid_input = False
                
        # if invalid input
        if not valid_input:
            messagebox.showinfo(title = "Error", message = "Input not valid!")

        else:
            # select text file
            read_file()  

            # write to new text file
            file = open(os.getcwd() + "\\3. Decrypted\\" + (filename.get().removesuffix(".txt").replace("_Encrypted","_Decrypted")) + ".txt", "w+")
            file.write(decryption(file_content, entry.get()))   

            # success message
            messagebox.showinfo(title = "Success", message = "Decryption successful!")
            decryptionWindow.destroy()

    decrypt = Button(decryptionWindow, text = "Decrypt", command = export, bg = "#495569", fg = "white", width = 10)

    # LAYOUT
    # file select
    fileselect_label.grid(row = 3, column = 1, pady = 3)
    filename.grid(row = 3, column = 2, pady = 2)
    # keyword and entry
    keyword_label.grid(row = 4, column = 1, pady = 3)
    entry.grid(row = 4, column = 2, pady = 2)
    # encrypt button
    decrypt.grid(row = 5, column = 2, pady = 7)

# instructions window
def InstructionsWindow():
    instructionsWindow = Toplevel(window)
    instructionsWindow.configure (bg = "#1e222b")
    instructionsWindow.title("Instructions")
    instructionsWindow.resizable(False, False)
    instructionsWindow.geometry("220x145")
    Label(instructionsWindow, fg = "#e4e7ec", bg="#1e222b", text = "Instructions", font = ("Helvetica", 10, "bold")).grid(row = 2, column = 3, ipadx = 75, pady = 15)

    def EncryptionInstructions():
        encryptionInstructions = Toplevel(window)
        encryptionInstructions.configure (bg = "#1e222b")
        encryptionInstructions.title("Encryption Instructions")
        encryptionInstructions.resizable(False, False)
        encryptionInstructions.geometry("350x165")
        
        Label(encryptionInstructions, fg = "#e4e7ec", bg="#1e222b", text = "Encryption Instructions", font = ("Helvetica", 10, "bold")).grid(row = 1, column = 3, pady = 10)
        encryptionText = """
        1. Use the dropdown menu to find your .txt file.
        2. Type your keyword in the input. Your keyword will be 
            saved in the Key Storage folder.
        3. Once you click Encrypt, your encrypted file will be
            saved in the Encrypted folder as a new file."""
        Label(encryptionInstructions, bg = "#1e222b", text = encryptionText, fg = "white", justify = LEFT).grid(row = 2, column = 3, ipadx = 5, pady = 2)

    def DecryptionInstructions():
        decryptionInstructions = Toplevel(window)
        decryptionInstructions.configure (bg = "#1e222b")
        decryptionInstructions.title("Decryption Instructions")
        decryptionInstructions.resizable(False, False)
        decryptionInstructions.geometry("350x165")
        
        Label(decryptionInstructions, bg = "#1e222b", fg = "white", text = "Decryption Instructions", font = ("Helvetica", 10, "bold")).grid(row = 1, column = 3, ipadx = 2, pady = 10)
        decryptionText = """
        1. Use the dropdown menu to find your .txt file.
        2. Type in your keyword in the input that corresponds 
            to the correct encrypted .txt file.
        3. Once you click Decrypt, your decrypted file will
            be saved in the Decrypted folder as a new file."""
        Label(decryptionInstructions, bg = "#1e222b", text = decryptionText, fg = "white", justify = LEFT).grid(row = 2, column = 3, ipadx = 5, pady = 2)

    # buttons for viewing instructions
    Button(instructionsWindow, fg = "#e4e7ec", bg="#1e222b", text = "Encryption", command = EncryptionInstructions).grid(row = 3, column = 3, ipadx = 40, pady = 2)
    Button(instructionsWindow, fg = "#e4e7ec", bg="#1e222b", text = "Decryption",  command = DecryptionInstructions).grid(row = 4, column = 3, ipadx = 40, pady = 2)

# about window
def AboutWindow():
    aboutWindow = Toplevel(window)
    aboutWindow.configure (bg = "#1e222b")
    aboutWindow.title("About Us")
    aboutWindow.geometry("725x200")
    aboutWindow.resizable(False, False)
    aboutText = """
    TEAM OPTIMUS PRIDE

    Presenting you a Modified Vigenere Cipher Program for safer communication in modern times.
    We are programmers, students, critical thinkers, athletes, artists, aspiring musicians, procrastinators, gamers and jack-of-all trades.
    Having such unique people from the different parts of region VI, we bring a diverse perspective to every program we do. 

    Agura, Gabriel Dax - Role: Duelist | Jett/Yoru/Aggressive Omen/Sova | Anstrick #5209
    Ferrer, Franz Peter - Role: Sentinel/Controller | Cypher/Chamber/Brimstone/Viper | Nitric Acid #bread
    Parcon, Mary Nicolette - Role: Sentinel | Sage/Viper/Chamber | Bun #shino
    Penafiel, Jeremy Jobert - Role: Fill | Phoenix/Omen/Cypher/Sova/Raze/Reyna | haku #2089
    Saluria, Precious Kaira - Role: Coach | kyeraaaa #3659"""
    Label(aboutWindow, text = aboutText, bg = "#1e222b",  fg = "white", justify = CENTER).grid(row = 1, column = 2, ipadx = 5, pady = 2)


# INTERACTABLE MAIN MENU BUTTONS
# encrypt
Button(window, text="Encrypt", fg = "#e4e7ec", bg = "#212630", command = EncryptionWindow).grid(column = 0, row = 2, ipadx = 10.5, pady = 2)
# decrypt
Button(window, text="Decrypt",  fg = "#e4e7ec", bg = "#212630", command = DecryptionWindow).grid(column = 1, row = 2, ipadx = 10.5, pady = 2)
# instructions
Button(window, text="Instructions", fg = "#e4e7ec", bg = "#212630", command = InstructionsWindow).grid(column = 0, row = 3, padx = 17, pady = 2)
# about
Button(window, text="About Us",  fg = "#e4e7ec", bg = "#212630", command = AboutWindow).grid(column = 1, row = 3, ipadx = 7, pady = 2)

# runs window infinitely
window.mainloop()