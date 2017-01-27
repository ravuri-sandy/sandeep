# sandeep poll script
import cgi

def htmltop():
  print("""content-type;text/html\n\n
<! DOCTYPE html>
<html lang = "en">
    <head>
        <meta charset= "utf-8"/>
<title>my server-side template</title> 
     </head>
     <body>""")

def htmltail():
    print("""</body>)
      </html""">
def createRadioButtons(movie):
	for hero in movie:
     print("""<input type="radio" name="hero" value="balakrishna">
  <input type="radio" name="hero" value="chiru"> 
  <input type="radio" name="hero" value="ntr"> 
  <input type="radio" name="hero" value="other"> """ )
  print ("<br>")
def createForm(people):
	print("""<form method="post" action="  ">""")
	createRadioButton(movie)
        print("""<input type = "submit" name="submit" />""")
	print("</form>")

      	
if__name__=="__main__":
	try:
		htmltop()
		htmltop()
		
	except:
		cgi.print_exception()
