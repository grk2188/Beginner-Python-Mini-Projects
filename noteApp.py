import tkinter as tk

class NoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Note App")

        # Create Text widget to display notes
        self.notes_display = tk.Text(master)
        self.notes_display.pack()

        # Create Entry widget to enter new notes
        self.new_note_entry = tk.Entry(master)
        self.new_note_entry.pack()

        # Create button to add new note
        self.add_note_button = tk.Button(master, text="Add Note", command=self.add_note)
        self.add_note_button.pack()

    def add_note(self):
        # Get new note from Entry widget
        new_note = self.new_note_entry.get()

        # Add new note to Text widget and clear Entry widget
        self.notes_display.insert(tk.END, new_note + "\n")
        self.new_note_entry.delete(0, tk.END)

#Create main window and run the application
root = tk.Tk()
app = NoteApp(root)
root.mainloop()
#In this example, we define a NoteApp class that creates a window with a Text widget to display the notes, an Entry widget to enter new notes, and a Button widget to add new notes to the display. When the "Add Note" button is clicked, the add_note method is called, which retrieves the new note from the Entry widget, adds it to the Text widget, and clears the Entry widget.

#You can customize this example to suit your needs, such as adding additional buttons for editing or deleting notes, or saving notes to a file.




