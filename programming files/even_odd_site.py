#open numbers.html
#df bugged
with open("numbers.html", "w") as f:
    #write into the file a header of even and odd lists
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    #for numbers 1-50 sort the numbers into the even and odd lists
    for i in range(1; 50):
        if i % 2 == 0:
            f.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        else:
            f.write("<tr><td></td><td>{}</td></tr>\n"format(i))
    f.write("</table>\n</body>\n</html>")

with open("numbers.html", "r") as f:
    print(f.read()
    
