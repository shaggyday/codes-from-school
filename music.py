import tones
tones.setup()
note = input("enter note: ")
while note != 'q':
    x = float(note)
    y = int(input("enter note length:"))
    z = int(input("enter pause length:"))
    #note = input("enter q to quit: ")
    a = int(x)
    b = int(a*6+(x-a)*10)
    tones.addNote(b, y)
    tones.addPause(z)
    note = input("enter note: ")
tones.closefile()
