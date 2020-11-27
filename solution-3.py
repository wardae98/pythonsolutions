#Question: write a function that returns true if the two provided license plates strings are visually similar. Only consider 26 English uppercase letters
#and the digits 0-9. These characters will be considered visually similar: (0,O, Q), (1,I,T), (2,Z), (5,S), (8,B)

def similar_license_plates(plate1,plate2):
    similar_1 = ["0","O","Q"]
    similar_2 = ["1","I","T"]
    similar_3 = ["2","Z"]
    similar_4 = ["5", "S"]
    similar_5 = ["8", "B"]
    if plate1.replace(" ","") == plate2.replace(" ",""):
        return True
    elif any(x in plate1.replace(" ","") for x in similar_1) and any(x in plate2.replace(" ","") for x in similar_1):
        return True
    elif any(x in plate1.replace(" ","") for x in similar_2) and any(x in plate2.replace(" ","") for x in similar_2):
        return True
    elif any(x in plate1.replace(" ","") for x in similar_3) and any(x in plate2.replace(" ","") for x in similar_3):
        return True
    elif any(x in plate1.replace(" ","") for x in similar_4) and any(x in plate2.replace(" ","") for x in similar_4):
        return True
    elif any(x in plate1.replace(" ","") for x in similar_5) and any(x in plate2.replace(" ","") for x in similar_5):
        return True
    else:
        return False
