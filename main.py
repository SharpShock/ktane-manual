def main():
    serial = ""
    serial = list(serial)
    wires("none", "none", "none", "none", "none", "none")

# Definir função do butão
def button(color,text,label,batteries):
    if (color == "blue" and text == "abort"):
        strip = input("Hold. What is the strip colored? (red, other...)  > ")
        if strip == "blue":
            print("Release when the countdown timer has a 4 in any position.")
        elif strip == "white":
            print("Release when the countdown timer has a 1 in any position.")
        elif strip == "yellow":
            print("Release when the countdown timer has a 5 in any position.")
        elif strip == "other":
            print("Release when the countdown timer has a 1 in any position.")

    elif batteries > 1 and text == "detonate":
        print("Press and immediately release the button.")

    elif color == "white" and label == "car":
        strip = input("Hold. What is the strip colored? (red, other...)  > ")
        if strip == "blue":
            print("Release when the countdown timer has a 4 in any position.")
        elif strip == "white":
            print("Release when the countdown timer has a 1 in any position.")
        elif strip == "yellow":
            print("Release when the countdown timer has a 5 in any position.")
        elif strip == "other":
            print("Release when the countdown timer has a 1 in any position.")
    
    elif batteries > 2 and label == "frk":
        print("Press and immediately release the button.")

    elif color == "yellow":
        strip = input("Hold. What is the strip colored? (red, other...)  > ")
        if strip == "blue":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 4 IN ANY POSITION. ---")
        elif strip == "white":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 1 IN ANY POSITION. ---")
        elif strip == "yellow":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 5 IN ANY POSITION. ---")
        elif strip == "other":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 1 IN ANY POSITION. ---")
    
    elif color == "red" and text == "hold":
        print("Press and immediately release the button")

    else:
        strip = input("Hold. What is the strip colored? (red, other...)  > ")
        if strip == "blue":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 4 IN ANY POSITION. ---")
        elif strip == "white":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 1 IN ANY POSITION. ---")
        elif strip == "yellow":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 5 IN ANY POSITION. ---")
        elif strip == "other":
            print("--- RELEASE WHEN THE COUNTDOWN TIMER HAS 1 IN ANY POSITION. ---")

# Definir função dos Fios
def wires(wire1, wire2, wire3, wire4, wire5, wire6):
    wires = []
    wires.append(wire1)
    wires.append(wire2)
    wires.append(wire3)
    wires.append(wire4)
    wires.append(wire5)
    wires.append(wire6)

    totalWires = 0
    redWires = 0
    blueWires = 0
    whiteWires = 0
    yellowWires = 0
    blackWires = 0

    for wire in wires:
        if wire != ["red", "blue", "white", "yellow", "black", "none"]:
            print("Invalid wire sequence, value must be a color or none.")
        if wire == "red":
            redWires += 1
        if wire == "blue":
            blueWires += 1
        if wire == "white":
            whiteWires += 1
        if wire == "yellow":
            yellowWires += 1
        if wire == "black":
            blackWires += 1
        if wire != "none":
            totalWires += 1
    
    wires.remove("none")

    print("Wires: " + str(wires))
    print("Number of Wires: " + str(totalWires))
    print("Number of red Wires: " + str(redWires))
    print("Number of blue Wires: " + str(blueWires))
    print("Number of white Wires: " + str(whiteWires))
    print("Number of yellow Wires: " + str(yellowWires))
    print("Number of black Wires: " + str(blackWires))

    if totalWires < 3 or totalWires > 6:
        print("Error. Total number of wires must be between 3 and 6.")

    elif totalWires == 3:
        if redWires == 0:
            print("--- CUT THE SECOND WIRE " + "(" +str(wires[1]) + ")" + " ---")
        elif wires[-1] == "white":
            print("--- CUT THE LAST WIRE " + "(" +str(wires[-1]) + ")" + " ---")
        elif blueWires > 1:
            print("--- CUT THE LAST BLUE WIRE (blue) ---")
        else:
            print("--- CUT THE LAST WIRE " + "(" +str(wires[-1]) + ")" + " ---")

    elif totalWires == 4:
        if redWires > 1 and (serial[-1] % 2) != 0:
            print("--- CUT THE LAST WIRE " + "(" +str(wires[-1]) + ")" + " ---")
        elif wires[-1] == "yellow" and redWires == 0:
            print("--- CUT THE FIRST WIRE " + "(" +str(wires[0]) + ")" + " ---")
        elif blueWires == 1:
            print("--- CUT THE FIRST WIRE " + "(" +str(wires[0]) + ")" + " ---")
        elif yellowWires > 1:
            print("--- CUT THE LAST WIRE " + "(" +str(wires[-1]) + ")" + " ---")
        else:
            print("--- CUT THE SECOND WIRE " + "(" +str(wires[1]) + ")" + " ---")
    
    elif totalWires == 5:
        if wires[-1] == "black" and (serial[-1] % 2) != 0:
            print("--- CUT THE FOURTH WIRE " + "(" +str(wires[3]) + ")" + " ---")
        elif redWires == 1 and yellowWires > 1:
            print("--- CUT THE FIRST WIRE " + "(" +str(wires[0]) + ")" + " ---")
        elif blackWires == 0:
            print("--- CUT THE SECOND WIRE " + "(" +str(wires[1]) + ")" + " ---")
        else:
            print("--- CUT THE FIRST WIRE " + "(" +str(wires[0]) + ")" + " ---")

    elif totalWires == 6:
        if yellowWires == 0 and (serial[-1] % 2) != 0:
            print("--- CUT THE THIRD WIRE " + "(" +str(wires[2]) + ")" + " ---")
        elif yellowWires == 1 and whiteWires > 1:
            print("--- CUT THE FOURTH WIRE " + "(" +str(wires[3]) + ")" + " ---")
        elif redWires == 0:
            print("--- CUT THE LAST WIRE " + "(" +str(wires[-1]) + ")" + " ---")
        else:
            print("--- CUT THE FOURTH WIRE " + "(" +str(wires[3]) + ")" + " ---")

main()
