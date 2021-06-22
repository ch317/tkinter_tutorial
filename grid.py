from tkinter import *
import sys

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.grid(row=3, column=0)

root = Tk()
myLabel1 = Label(root, text="2-way Odds (Equal Margin)")

odd1Str = StringVar()
odd2Str = StringVar()
odd1FairEqualMargin = StringVar()
odd2FairEqualMargin = StringVar()
marginSV = StringVar()
p1FairEqualMargin = StringVar()
p2FairEqualMargin = StringVar()

def calculateFairOddsEqualMargin(a,b,c):
    try:
        print("calculateFairOddsEqualMargin")
        print(odd1Str.get())
        print(odd2Str.get())

        odd1 = float(odd1Str.get())
        odd2 = float(odd2Str.get())
        margin = (1/odd1) + (1/odd2)
        marginSV.set("{:.3f}".format(margin))
        odd1FairEqualMargin.set("{:.3f}".format(odd1*margin))
        odd2FairEqualMargin.set("{:.3f}".format(odd2*margin))
        p1FairEqualMargin.set("{:.3f}".format(1/(odd1*margin)))
        p2FairEqualMargin.set("{:.3f}".format(1/(odd2*margin)))

        print(odd1FairEqualMargin)
        print(odd2FairEqualMargin)
    except IOError:
        type, value, traceback = sys.exc_info()
        print('Error opening %s: %s' % (value.filename, value.strerror))

odd1TextField = Entry(root, textvariable=odd1Str)
odd1Str.trace_add("write", calculateFairOddsEqualMargin)
odd2TextField = Entry(root, textvariable=odd2Str)
odd2Str.trace_add("write", calculateFairOddsEqualMargin)

marginTitle = Label(root, text="Margin:")
marginLabel = Label(root, textvariable=marginSV)
odd1FairLabel = Label(root, textvariable=odd1FairEqualMargin)
odd2FairLabel = Label(root, textvariable=odd2FairEqualMargin)
p1FairLabel = Label(root, textvariable=p1FairEqualMargin)
p2FairLabel = Label(root, textvariable=p2FairEqualMargin)


myLabel1.grid(row=0, column=0)
marginTitle.grid(row=0, column=2)
odd1TextField.grid(row=1, column=0)
odd2TextField.grid(row=1, column=1)
marginLabel.grid(row=1, column=2)
odd1FairLabel.grid(row=2, column=0)
odd2FairLabel.grid(row=2, column=1)
p1FairLabel.grid(row=3, column=0)
p2FairLabel.grid(row=3, column=1)

root.mainloop()