import webbrowser
import sqlite3
# Program to open multiple website in different tab at once.

def addURL(url):
	# Adding website URL in Database, less the better
	if len(url) < 1:
		return
	else:
		handleDB = sqlite3.connect("links")
		h = handleDB.cursor()
		h.execute("INSERT INTO URL_Links(url, Importance) VALUES (?, ?);", (url, 3))
		print("URL ADDED")
		print("Closing Connection\n")
		handleDB.commit()
		h.close()
		return
def removeURL(url):
	# Removing website URL from Database.
	if len(url) < 1:
		return
	else:
		handleDB = sqlite3.connect("links")
		h = handleDB.cursor()
		h.execute("DELETE FROM URL_Links WHERE url=?;", (url,))
		print("URL REMOVED")
		print("Closing Connection\n")
		handleDB.commit()
		h.close()
		return
def BrowserAndWebsitesDB(path):
	# function to fetch URL from database and open it
	if len(path) < 1:
		return
	else:
		handleDB = sqlite3.connect(path)
		h = handleDB.cursor()
		h.execute("SELECT url FROM URL_Links;")
		for link in h:
			#print(link)
			webbrowser.open_new_tab(link[0])
		print("Closing Connection\n")
		handleDB.commit()
		h.close()
		return

def BrowerAndWebsiteFile(path):
	# function to fetch URL from file and open it
	print()
	
def ShowUrlList():
	# Displaying all the URL in the lisk
	handleDB = sqlite3.connect("links")
	h = handleDB.cursor()
	h.execute(" SELECT * FROM URL_Links;")
	for row in h:
		print(row[1])
	print()
	handleDB.commit()
	h.close()
	return
	

print("Website Opener")
print("yash kundnani (yash.kundnani@outlook.com)")
print('''
#     #                                        #######                                    
#  #  # ###### #####   ####  # ##### ######    #     # #####  ###### #    # ###### #####  
#  #  # #      #    # #      #   #   #         #     # #    # #      ##   # #      #    # 
#  #  # #####  #####   ####  #   #   #####     #     # #    # #####  # #  # #####  #    # 
#  #  # #      #    #      # #   #   #         #     # #####  #      #  # # #      #####  
#  #  # #      #    # #    # #   #   #         #     # #      #      #   ## #      #   #  
 ## ##  ###### #####   ####  #   #   ######    ####### #      ###### #    # ###### #    # 

''')


print("=============================================================================")


while(1):
	#file or database
	a = input("Enter S To show list of URL\nEnter D for opening from database\nA to Add URL\nR to Delete URL\nEnter Any Other Key To Exit\n")


	if a == 'S':
		'''fileName = input("Enter File Location ")
		BrowserAndWebsiteFile(fileName)'''
		ShowUrlList()
	elif a =='D':
		dbname = input("Enter DB Location ")
		BrowserAndWebsitesDB(dbname)
	
	elif a == 'A':
		url=input("Enter URL to Add ")
		addURL(url)
	elif a == 'R':
		url=input("Enter URL to Remove ")
		removeURL(url)
	else:
		exit()
	


