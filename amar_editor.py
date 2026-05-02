import tkinter as tk
from tkinter import scrolledtext
import bangla_compiler 

class BanglaEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Amar Bangla Editor")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")
        
        self.toolbar = tk.Frame(self.root, bg="#2c3e50", height=45)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.run_btn = tk.Button(self.toolbar, text="▶ RUN", command=self.run_logic, 
                                 bg="#27ae60", fg="white", font=("Arial", 10, "bold"), padx=20)
        self.run_btn.pack(side=tk.LEFT, padx=10, pady=7)

        self.editor = scrolledtext.ScrolledText(self.root, font=("Consolas", 14), 
                                                bg="#1e1e1e", fg="#dcdcdc", insertbackground="white")
        self.editor.pack(fill=tk.BOTH, expand=True)

        self.console = scrolledtext.ScrolledText(self.root, height=10, bg="#000000", 
                                                 fg="#00ff00", font=("Consolas", 12))
        self.console.pack(fill=tk.X)

        self.editor.bind("<KeyRelease>", self.highlight_keywords)

    def highlight_keywords(self, event=None):
        # Highlighting updated keywords
        keywords = ["dhoro", "dekhao", "jodi", "tahole", "nahole"]
        self.editor.tag_remove("kw", "1.0", tk.END)
        for word in keywords:
            start = "1.0"
            while True:
                start = self.editor.search(word, start, stopindex=tk.END)
                if not start: break
                end = f"{start}+{len(word)}c"
                self.editor.tag_add("kw", start, end)
                self.editor.tag_config("kw", foreground="#569cd6", font=("Consolas", 14, "bold"))
                start = end

    def run_logic(self):
        self.console.delete("1.0", tk.END)
        self.console.config(fg="#00ff00") # Reset to green
        bangla_compiler.variables = {} 
        
        code = self.editor.get("1.0", tk.END).strip()
        lines = code.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line: continue
            
            try:
                bangla_compiler.last_output = ""
                bangla_compiler.parser.parse(line)
                if bangla_compiler.last_output != "":
                    self.console.insert(tk.END, f"> {bangla_compiler.last_output}\n")
            except Exception as e:
                self.console.config(fg="#ff3333") # Switch to red for "Bhul"
                self.console.insert(tk.END, f"❌ {str(e)}\n")
        
        self.console.insert(tk.END, "\n--- Run Finished ---")

if __name__ == "__main__":
    root = tk.Tk()
    app = BanglaEditor(root)
    root.mainloop()