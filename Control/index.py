#!/usr/bin/python

#import modules
import RPi.GPIO as GPIO
import cgi, cgitb 
import virtuallcd

#enable debugging output
cgitb.enable()

#define functions for repetitive html stuff
def printHeader():
	print "<!DOCTYPE html><!-- <!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\"> --><!-- <!DOCTYPE html> -->"
	print "<html>"
	print "<head>"
	print "<meta http-equiv=\"Content-type\" content=\"text/html;charset=UTF-8\">"
	print"<link rel=\"stylesheet\" type=\"text/css\" href=\"styles/stylesheet.css\">"
	print "<title>CoffeeControl v0.1</title>"
	print "</head>"
	print "<body>"
	print "<div id=\"container\">"
	print "<div id=\"header\"><h1>Coffee Control Panel</h1></div>"
	print "<div id=\"menu\"><b>Menu</b><br>Coffee<br></div>"
	
def printFooter():
	print "</div>"
	print "</body>"
	print "</html>"
	
def  printControls():
	print "<div id=\"content\">"
	print "<img src=\"output.png\" style=\"height:50px;width:300px;image-rendering:-webkit-optimize-contrast;\">"
	print "<form action=\"index.py\" method=\"post\">"
	print "<select name=\"coffeeselection\">"
	print "<option value=\"cappuccino\">Cappuccino</option>"
	print "<option value=\"espresso\">Espresso</option>"
	print "</select>"
	print "<input type=\"submit\" value=\"Brew\"/>"
	print "</form>"

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

#set up GPIO Mode
GPIO.setmode(GPIO.BOARD)

#set up GPIO Channel
GPIO.setup(23, GPIO.OUT)

printHeader()

if form.getvalue('coffeeselection') == "cappuccino":
	printControls()
	print "Making Cappuccino</div>"
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(23, GPIO.LOW)
	
elif form.getvalue('coffeeselection') == "espresso":
	printControls()
	print "Making Espresso</div>"
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(23, GPIO.LOW)
	
#if the webpage has been opened for the first time, do this
else:
	printControls()
	

printFooter()
GPIO.cleanup()