cgpa_list= [3.74, 4.00,3.68, 3.88,3.65] #Al-Amin


out_of_four= 0
out_of_cgpa= 0

for i in range(0, len(cgpa_list)):
    if i<=2:
        out_of_four +=(cgpa_list[i]*5)/100
        out_of_cgpa += (4*5)/100
    elif i ==3:
        out_of_four += (cgpa_list[i]*10)/100
        out_of_cgpa +=(4*10)/100
    elif i==4:
        out_of_four += (cgpa_list[i]*15)/100
        out_of_cgpa += (4*15)/100
    elif i==5:
        out_of_four += (cgpa_list[i]*20)/100
        out_of_cgpa +=(4*20)/100
    elif i==6:
        out_of_four +=(cgpa_list[i]*25)/100
        out_of_cgpa +=(4*25)/100
    elif i==7:
        out_of_four +=(cgpa_list[i]*15)/100
        out_of_cgpa +=(4*15)/100
print("You got: "+ str(out_of_four), end="")
print("Out of: "+ str(out_of_cgpa))
