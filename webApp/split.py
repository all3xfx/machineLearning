# This is a convenient python file
# to format the NN weights string ("wts" in gestures.js)
# to be 9 numbers per row (i.e. each matrix per timestamp, and each matrix has its own 3 rows printed along 1 row),
# with empty lines between each line.

# copy the wts string from gestures.html (in your browser) and put it between quotation marks here:
wts="0,0,0,0.86,0.91,0.86,0,0,0,0,0,0,0.86,0.91,0.86,0,0.86,0,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0,0.86,0,0,0.91,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0,0.91,0,0,0.86,0,0,0,0.86,0.86,0.86,0,0.86,0.91,0,0,0,0.86,0.86,0.91,0,0.86,0.86,0,0,0,0.86,0.86,0.86,0,0,0.91,0,0,0,0.86,0,0.91,0,0.86,0.86,0,0,0,0.86,0,0.91,0,0,0.86,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0.86,0.91,0,0.86,0,0,0,0,0.86,0.91,0.86,0,0,0.86,0,0,0,0.86,0.91,0.86,0,0.86,0.86,0,0,0,0.86,0.91,0.86,0,0.86,0.86,0,0,0,0.91,0.86,0.86,0,0,0.86,0,0,0,0.91,0.86,0.86,0,0,0,0,0,0,0.91,0,0.86,0,0,0.86,0,0,0,0.91,0,0.86,0,0,0.86,0,0,0,0.91,0.86,0.86,0,0,0.86,0,0,0,0.91,0.86,0.86,0,0,0,0,0,0,0.91,0.86,0.86,0,0.86,0.86,0,0,0,0.86,0.86,0.86,0,0,0.91,0,0,0,0.91,0.86,0.86,0,0.86,0.86,0,0,0,0.86,0.86,0.86,0,0,0.91,0,0,0,0.91,0.86,0.86,0,0,0.86,0,0,0,0.86,0.86,0.86,0,0,0.91,0,0,0,0.86,0.91,0.86,0,0,0.86,0,0,0,0.86,0,0.91,0,0.86,0.86,0,0,0,0.86,0.86,0.86,0,0.86,0.91,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0.86,0.86,0,0.86,0.91,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0.86,0.86,0,0,0.91,0,0,0,0.86,0,0.91,0,0,0.86,0,0,0,0.86,0.86,0.86,0,0,0.91,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0.86,0.86,0,0.91,0.86,0,0,0,0.86,0.86,0.91,0,0,0.86,0,0,0,0.86,0.86,0.91,0,0.86,0.86,0,0,0,0.86,0.86,0.91,0,0.86,0.86,0,0,0,0.86,0.91,0.86,0,0,0.86,0,0,0,0.86,0.91,0.86,0,0.86,0.86,0,0,0,0.86,0.91,0.86,0,0,0.86,0,0,0,0.91,0.86,0.86,0,0,0.86,0,0,0,0.91,0.86,0.86,0,0,0,0,0,0,0.91,0,0.86,0,0,0.86"

splitString = wts.split(",")

nthComma = 3

stringSplitByNthComma = [",".join(splitString[i:i+nthComma]) for i in range(0, len(splitString), nthComma)]

nthBracketComma = 3

stringSplitByNthBracketComma = ["],[".join(stringSplitByNthComma[i:i+nthBracketComma]) for i in range(0, len(stringSplitByNthComma), nthBracketComma)]

for matrix in stringSplitByNthBracketComma:
    #print ("")
    print ("[[" + matrix + "]],")