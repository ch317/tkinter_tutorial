from tkinter import *
import sys

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.grid(row=3, column=0)

root = Tk()
myLabel1 = Label(root, text="2-way Odds (Equal Margin)")
odd1Label = Label(root, text="Odds 1")
odd2Label = Label(root, text="Odds 2")
marketOdds = Label(root, text="Marked Odds:")
fairOdds = Label(root, text="Fair Odds:")
fairProbability = Label(root, text="Fair Probability:")
boughtOdds = Label(root, text="Bought Odds:")

odd1Str = StringVar()
odd2Str = StringVar()
odd1FairEqualMargin = StringVar()
odd2FairEqualMargin = StringVar()
marginSV = StringVar()
p1FairEqualMargin = StringVar()
p2FairEqualMargin = StringVar()
boughtOdds1Str = StringVar()
boughtOdds2Str = StringVar()
ev1Str = StringVar()
ev2Str = StringVar()

toggle_isEV2WayWithOdds = True

def switch_toggle_isEV2WayWithOdds():
    global toggle_isEV2WayWithOdds
      
    # Determin is on or off
    if toggle_isEV2WayWithOdds:
        boughtOdds.config(text = "Bought Probability:", 
                        fg = "grey")
        evTypeButton.config(text = "ON: Probabilities")
        toggle_isEV2WayWithOdds = False
    else:
        boughtOdds.config(text = "Bought Odds:")
        evTypeButton.config(text = "ON: Odds")
        toggle_isEV2WayWithOdds = True


def setColorEVLabel(label, ev):
        if (ev > 1):
            label.config(fg = "green")
        else:
            label.config(fg = "red")

def setEVs2WayWithOdds():
        boughtOdds1 = float(boughtOdds1Str.get())
        boughtOdds2 = float(boughtOdds2Str.get())

        ev1 = boughtOdds1/float(odd1FairEqualMargin.get())
        ev2 = boughtOdds2/float(odd2FairEqualMargin.get())
        ev1Str.set("{:.3f}".format(ev1))
        ev2Str.set("{:.3f}".format(ev2))
        setColorEVLabel(ev1Label, ev1)
        setColorEVLabel(ev2Label, ev2)

def setEVs2WaysWithProbabilities():
        boughtProbability1 = float(boughtOdds1Str.get())
        boughtProbability2 = float(boughtOdds2Str.get())

        oddFair1 = float(odd1FairEqualMargin.get())
        oddFair2 = float(odd2FairEqualMargin.get())

        probabilityFair1 = 1/oddFair1
        probabilityFair2 = 1/oddFair2

        ev1 = probabilityFair1/boughtProbability1
        ev2 = probabilityFair2/boughtProbability2
        ev1Str.set("{:.3f}".format(ev1))
        ev2Str.set("{:.3f}".format(ev2))
        setColorEVLabel(ev1Label, ev1)
        setColorEVLabel(ev2Label, ev2)

def calculateEVFinal(a,b,c):
    try:
        if toggle_isEV2WayWithOdds:
            setEVs2WayWithOdds()
        else:
            setEVs2WaysWithProbabilities()

    except IOError:
        type, value, traceback = sys.exc_info()
        print('Error opening %s: %s' % (value.filename, value.strerror))

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

        calculateEVFinal(0,0,0) #We update EV calculations

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

#EV
boughtOdds1TextField = Entry(root, textvariable=boughtOdds1Str)
boughtOdds1Str.trace_add("write", calculateEVFinal)
boughtOdds2TextField = Entry(root, textvariable=boughtOdds2Str)
boughtOdds2Str.trace_add("write", calculateEVFinal)
evLabel = Label(root, text="EV:")
ev1Label = Label(root, textvariable=ev1Str)
ev2Label = Label(root, textvariable=ev2Str)
evTypeButton = Button(root, text="On: Odds", command = switch_toggle_isEV2WayWithOdds)

#Row 0
myLabel1.grid(row=0, column=0)
#Row 1
odd1Label.grid(row=1, column=1)
odd2Label.grid(row=1, column=2)
marginTitle.grid(row=1, column=3)
#Row 2
marketOdds.grid(row=2, column=0)
odd1TextField.grid(row=2, column=1)
odd2TextField.grid(row=2, column=2)
marginLabel.grid(row=2, column=3)
#Row 3
fairOdds.grid(row=3, column=0)
odd1FairLabel.grid(row=3, column=1)
odd2FairLabel.grid(row=3, column=2)
#Row 4
fairProbability.grid(row=4, column=0)
p1FairLabel.grid(row=4, column=1)
p2FairLabel.grid(row=4, column=2)

#Row 5
boughtOdds.grid(row=5, column=0)
boughtOdds1TextField.grid(row=5, column=1)
boughtOdds2TextField.grid(row=5, column=2)
evTypeButton.grid(row=5, column=3)

#Row 6
evLabel.grid(row=6, column=0)
ev1Label.grid(row=6, column=1)
ev2Label.grid(row=6, column=2)
root.mainloop()