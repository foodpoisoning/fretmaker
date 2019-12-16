from tkinter import *

root = Tk()


#This contains default mappings for any variables (position markers)
mappings = {
    'position_marker_0': '0',
    'position_marker_1': '1',
    'position_marker_2': '2',
    'position_marker_3': '3',
    'position_marker_4': '4',
    'position_marker_5': '5',
    }

topframe = Frame(root)
topframe.pack()

#The button that will eventually be bound to the new_note function
next_button = Button(topframe, text = "Next Note", fg = 'black')
next_button.pack(side = TOP)

bottomframe = Frame(root, background = "bisque")
bottomframe.pack(side = BOTTOM)

#labels for all the strings
ylabel0 = Label(bottomframe, text = 'E')
ylabel1 = Label(bottomframe, text = 'B')
ylabel2 = Label(bottomframe, text = 'G')
ylabel3 = Label(bottomframe, text = 'D')
ylabel4 = Label(bottomframe, text = 'A')
ylabel5 = Label(bottomframe, text = 'E')

ylabel0.grid(row = 0, column = 0)
ylabel1.grid(row = 1, column = 0)
ylabel2.grid(row = 2, column = 0)
ylabel3.grid(row = 3, column = 0)
ylabel4.grid(row = 4, column = 0)
ylabel5.grid(row = 5, column = 0)

#labels for position markers(variable)
xlabel0 = Label(bottomframe, text = mappings['position_marker_0'])
xlabel1 = Label(bottomframe, text = mappings['position_marker_1'])
xlabel2 = Label(bottomframe, text = mappings['position_marker_2'])
xlabel3 = Label(bottomframe, text = mappings['position_marker_3'])
xlabel4 = Label(bottomframe, text = mappings['position_marker_4'])
xlabel5 = Label(bottomframe, text = mappings['position_marker_5'])

xlabel0.grid(row = 6, column = 1)
xlabel1.grid(row = 6, column = 2)
xlabel2.grid(row = 6, column = 3)
xlabel3.grid(row = 6, column = 4)
xlabel4.grid(row = 6, column = 5)
xlabel5.grid(row = 6, column = 6)


#Canvas with the default fretboard drawn
fretboard_canvas = Canvas(bottomframe, bg = "blue", width = 450, height = 200)
fretboard_canvas.grid(row = 0, rowspan = 6, column = 1, columnspan = 6)
fretboard_canvas.create_rectangle(36, 15, 418, 190, outline = 'black')
fretboard_canvas.create_line(36, 50, 418, 50)
fretboard_canvas.create_line(36, 85, 418, 85)
fretboard_canvas.create_line(36, 120, 418, 120)
fretboard_canvas.create_line(36, 155, 418, 155)
fretboard_canvas.create_line(112, 15, 112, 190)
fretboard_canvas.create_line(189, 15, 189, 190)
fretboard_canvas.create_line(265, 15, 265, 190)
fretboard_canvas.create_line(342, 15, 342, 190)

fretboard_canvas.create_oval()

root.mainloop()
