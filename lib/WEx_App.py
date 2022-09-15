#!/usr/bin/python3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class WordExApp:
    def __init__(self, master=None):
        
        self.WExTopLevel = tk.Tk() if master is None else tk.Toplevel(master)

        # Getting image path for the app banner and icon
        self.img_WEx_Logo = tk.PhotoImage(file="res/image/WEx_Logo.png")
        self.img_WEx_Banner = tk.PhotoImage(file="res/image/WEx_Banner.png")
        
        
        # Build toplevel window
        self.WExTopLevel.geometry("585x495")
        self.WExTopLevel.iconphoto(True, self.img_WEx_Logo)
        self.WExTopLevel.resizable(False, False)
        self.WExTopLevel.title("Word Extractor")
        
        
        # Creating the main frame to place all widgets
        self.WExMainFrame = tk.Frame(self.WExTopLevel)
        self.WExMainFrame.configure(height=300, relief="flat", width=585)
        
        
        # Creating the banner frame to place the app banner
        self.BannerFrame = tk.Frame(self.WExMainFrame)
        #  Adding the banner image to the banner frame
        self.BannerLabel = tk.Label(self.BannerFrame)
        
        # Customizing banner frame and label
        self.BannerFrame.configure(height=100, width=585)
        self.BannerLabel.configure(image=self.img_WEx_Banner)
        
        
        
        # Creating the text frame 
        self.TextFrame = tk.Frame(self.WExMainFrame)
        # Adding a scrollable text box the the text frame
        self.SentenceEntryBox = ScrolledText(self.TextFrame)
        # Adding the default text into the scrollable text box 
        _text_ = " \n\n\n\n\n\t   E N T E R    Y O U R    T E X T    H E R E ."
        self.SentenceEntryBox.insert("0.0", _text_)
        
        # Customizing the text frame and scrollable text box 
        self.TextFrame.configure(
            height=200,
            takefocus=True,
            width=585
            )
        
        self.SentenceEntryBox.configure(
            blockcursor="false",
            cursor="arrow",
            font="{Microsoft JhengHei} 14 {}",
            foreground="#0e2845",
            height=10,
            insertbackground="#64dd73",
            insertunfocussed="hollow",
            insertwidth=3,
            selectbackground="#64dd73",
            selectforeground="#0e2845",
            spacing1=2,
            state="normal",
            tabstyle="wordprocessor",
            takefocus=True,
            undo="true",
            wrap="word"
        )



        # Creating buttons frame
        self.ButtonsFrame = tk.Frame(self.WExMainFrame)
        # Customizing button frame so that the button and label widgets
        self.ButtonsFrame.configure(background="#0e2845", height=150, width=585)
        
        # Creating all buttons and label to place on button frame
        
        # Extract button
        self.ExtractWordBtn = tk.Button(self.ButtonsFrame)
        # Clear button
        self.ClearBtn = tk.Button(self.ButtonsFrame)
        # Save button
        self.SaveBtn = tk.Button(self.ButtonsFrame)
        
        # App version label
        self.VersionLabel = tk.Label(self.ButtonsFrame)
        
        # Customizing buttons and label
        
        # Extract button
        self.ExtractWordBtn.configure(
            activebackground="#0e2845",
            activeforeground="#64dd73",
            background="#64dd73",
            compound="top",
            cursor="hand2",
            default="normal",
            font="{@Microsoft JhengHei} 12 {bold}",
            foreground="#0e2845",
            height=2,
            text="E X T R A C T",
            width=12,
            command=self.extract_words_to_list
        )
        

        # Clear button
        self.ClearBtn.configure(
            activebackground="#0e2845",
            activeforeground="#e3edf9",
            background="#e3edf9",
            compound="top",
            cursor="hand2",
            default="normal",
            font="{Microsoft JhengHei UI} 12 {bold}",
            foreground="#0e2845",
            height=2, 
            text="C L E A R", 
            width=12,
            command=self.clear_sentence
        )



        # Save button
        self.SaveBtn.configure(
            activebackground="#0e2845",
            activeforeground="#5093dc",
            background="#5093dc",
            compound="top",
            cursor="hand2",
            default="normal",
            font="{Microsoft JhengHei UI} 12 {bold}",
            foreground="#0e2845",
            height=2, 
            text="S A V E", 
            width=12, 
            command=self.save_words_to_file
        )


        # App version label
        self.VersionLabel.configure(
            background="#0e2845",
            font="{Microsoft} 10 {bold}",
            foreground="#64dd73",
            text="V 1 . 1",
        )
        
        
        
        

        
        
        
        
        
        #######################
        # PACKING AND PLACING #
        #     ALL WIDGETS     #
        #######################
        
        
        # Section 1
        self.WExMainFrame.pack(side="top")
        self.BannerFrame.pack(side="top")
        self.BannerLabel.pack(side="top")

        # Section 2
        self.TextFrame.pack(side="top")
        self.SentenceEntryBox.pack(side="top")
        
        # Section 3
        self.ButtonsFrame.pack(side="top")
        self.ExtractWordBtn.place(relx=0.09, rely=0.19, x=0, y=0)
        self.ClearBtn.place(relx=0.39, rely=0.19, x=0, y=0)
        self.SaveBtn.place(relx=0.69, rely=0.19, x=0, y=0)
        self.VersionLabel.place(relx=0.47, rely=0.71, x=0, y=0)
       

        
        
        
        # Launching the toplevel window
        self.mainwindow = self.WExTopLevel
        
        

    def run(self):
        self.mainwindow.mainloop()

    def extract_words_to_list(self):
        pass

    def clear_sentence(self):
        pass

    def save_words_to_file(self):
        pass


if __name__ == "__main__":
    app = WordExApp()
    app.run()
