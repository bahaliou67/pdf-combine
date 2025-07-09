import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def select_files():
    files = filedialog.askopenfilenames(
        title="Sélectionner les fichiers PDF",
        filetypes=[("Fichiers PDF", "*.pdf")]
    )
    if files:
        file_list.delete(0, tk.END)  # Vider la liste
        for file in files:
            file_list.insert(tk.END, file)  # Afficher les fichiers sélectionnés

def select_output():
    output = filedialog.asksaveasfilename(
        title="Choisir l'emplacement du PDF fusionné",
        defaultextension=".pdf",
        filetypes=[("Fichiers PDF", "*.pdf")]
    )
    if output:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output)

def merge_pdfs():
    files = file_list.get(0, tk.END)
    output = output_entry.get()
    
    if not files:
        messagebox.showerror("Erreur", "Veuillez sélectionner au moins un fichier PDF.")
        return
    if not output:
        messagebox.showerror("Erreur", "Veuillez spécifier un fichier de sortie.")
        return

    try:
        pdf_merger = PdfMerger()
        for file in files:
            pdf_merger.append(file)
        pdf_merger.write(output)
        pdf_merger.close()
        messagebox.showinfo("Succès", f"PDF fusionné sauvegardé à {output}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de la fusion : {str(e)}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Fusionneur de PDF")
root.geometry("600x400")

# Bouton pour sélectionner les fichiers
tk.Button(root, text="Sélectionner les PDF", command=select_files).pack(pady=10)

# Liste pour afficher les fichiers sélectionnés
file_list = tk.Listbox(root, width=80, height=10)
file_list.pack(pady=10)

# Entrée pour le fichier de sortie
tk.Label(root, text="Fichier de sortie :").pack()
output_entry = tk.Entry(root, width=60)
output_entry.pack(pady=5)
tk.Button(root, text="Choisir l'emplacement", command=select_output).pack(pady=5)

# Bouton pour lancer la fusion
tk.Button(root, text="Fusionner les PDF", command=merge_pdfs).pack(pady=20)

# Lancer l'application
root.mainloop()