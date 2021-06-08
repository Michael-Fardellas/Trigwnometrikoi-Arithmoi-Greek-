
import tkinter as tk
from tkinter import messagebox

HEIGHT =500
WIDTH = 800


ef = {"εφ0" : "0",
"εφ30" : "√3/3",
"εφ45" : "1", 
"εφ60" : "√3", 
"εφ90" : "Δεν οριζεται",
"εφ180" : "0"}

sun = {"συν0" : "1", 
"συν270" : "0",
"συν30" : "√3/2", 
"συν45" : "√2/2", 
"συν60" : "1/2", 
"συν90" : "0"}

hm = {"ημ0" : "0", 
"ημ30" : "1/2", 
"ημ45" : "√2/2", 
"ημ60" : "√3/2", 
"ημ90" : "1",}

sf = {"σφ0" : "Δεν οριζεται", 
"σφ30" : "√3", 
"σφ45" : "1", 
"σφ60" : "√3/3", 
"σφ90" : "1",}

ef1 = {"εφ0" : "0",
"εφ30" : "√3/3",
"εφ45" : "1", 
"εφ60" : "√3", 
"εφ90" : "Δεν οριζεται"}

sun1 = {"συν0" : "-1", 
"συν30" : "-√3/2", 
"συν45" : "-√2/2", 
"συν60" : "-1/2", 
"συν90" : "-0"}

hm1 = {"ημ0" : "0", 
"ημ30" : "-1/2", 
"ημ45" : "-√2/2", 
"ημ60" : "-√3/2", 
"ημ90" : "-1",}

sf1 = {"σφ0" : "Δεν οριζεται", 
"σφ30" : "-√3", 
"σφ45" : "-1", 
"σφ60" : "-√3/3", 
"σφ90" : "-1",}

def cleartext():
	label3 = tk.Label(frame, bg = "grey",  text = "")
	label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)

def trigwnometrikoi_arithmoi(entry, entry1):
	try:
		nummer = 0
		entry = int(entry)
		nummer = 0
		if entry < 0:
			entry = -entry
			if entry > 360:
				entry = entry % 360
				entry = 360 - entry
		while entry >= 360:
			entry -= 360
		if 90 < entry < 180 and entry != 0:
			entry = entry - 90
			if entry1 == "ημ":
				entry1 = "συν"
			elif entry1 == "συν":
				entry1 = "ημ"
			elif entry1 == "εφ":
				entry1 = "σφ"
			elif entry1 == "σφ":
				entry1 = "εφ"
		if entry > 180 and  entry != 0 and entry != 270:
			entry = entry - 180
			nummer = nummer + 1
		if 90 < entry < 180:
			entry = 180 - entry
			if entry1 == "ημ":
				nummer = nummer + 0
			elif entry1 == "συν" or entry1 == "εφ" or entry1 == "σφ":
				nummmer = nummer + 1
		word = "{}{}".format(entry1, entry)
		if entry1 == "ημ" and nummer == 0:
			label3 = tk.Label(frame, bg = "grey",  text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, hm[word]), font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0., relwidth = 1 , relheight = 0.2)
		elif entry1 == "συν" and nummer == 0:
			label3 = tk.Label(frame, bg = "grey", text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, sun[word]), font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)
		elif entry1 == "σφ" and nummer == 0:
			label3 = tk.Label(frame, bg = "grey", text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, sf[word]), font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)
		elif entry1 == "εφ" and nummer == 0:
			label3 = tk.Label(frame, bg = "grey", text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, ef[word]), font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)
		if entry1 == "ημ" and nummer != 0:
			label3 = tk.Label(frame, bg = "grey", text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, hm1[word]), font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)
		elif entry1 == "συν" and nummer != 0:
			label3 = tk.Label(frame, bg = "grey", text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, sun1[word]) , font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)
		elif entry1 == "σφ" and nummer != 0:
			label3 = tk.Label(frame, bg = "grey", text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, sf1[word]), font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)
		elif entry1 == "εφ" and nummer != 0:
			label3 = tk.Label(frame, bg = "grey", text = "Η γωνια σας μετατραπηκε σε {} και η ο τριγωνομετρικος αριθμος ειναι {}".format(word, ef1[word]), font = ('Helvetica', 15))
			label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)
	except Exception as e:
		messagebox.showerror("Προβλημα", "Δωσε μου σωστο τριγωνομετρικο αριθμο η τριγωνομετρικο λογο")
		#label3 = tk.Label (frame, bg = "grey", text = "Δωσε μου σωστο τριγωνομετρικο αριθμο η τριγωνομετρικο λογο",  font = ('Helvetica', 15))
		#label3.place(rely = 0.35, relx = 0, relwidth = 1 , relheight = 0.2)

root = tk.Tk()

root.title("Προγραμμα τριγωνομετρικων αριθμων")

canvas = tk.Canvas(root, height= HEIGHT, width = WIDTH)
canvas.pack()

e = tk.Frame(root, bg = "white")
e.place(relwidth = 0.4, relheight = 0.4)

frame = tk.Frame(root, bg="grey")
frame.place(relwidth=1, relheight=1)

entry1 = tk.Entry(frame)
entry1.place(relx = 0.11, rely = 0.15, relwidth = 0.24, relheight = 0.05)

entry = tk.Entry(frame)
entry.place(relx = 0.45, rely = 0.15, relwidth = 0.1444, relheight = 0.05)


#koumpia

button = tk.Button(frame, text = "Βρες", command = lambda: trigwnometrikoi_arithmoi(entry.get(), entry1.get()))
button.place(relx = 0.67, rely = 0.12, relwidth = 0.18)

button2= tk.Button(frame, text = "Καθαρισε το πλαισιο", command = lambda: cleartext())
button2.place(relx = 0.67, rely = 0.17, relwidth = 0.2444)

#label = tk.Label(frame, text = "Προγραμμα Τριγωνομετρικων αριθμων")
#label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.05)

# εδω ειναι τα δωσε

label = tk.Label(frame, text = "Δωσε μου τριγωνομετρικο λογο")
label.place(relx = 0.11, rely = 0.1, relwidth = 0.244, relheight = 0.05)

label1 = tk.Label(frame, text = "Δωσε μου μοιρες:")
label1.place(relx = 0.45, rely = 0.1, relwidth = 0.144, relheight = 0.05)

root.mainloop()
