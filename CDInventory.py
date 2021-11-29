#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# EGlen, 2021-Nov-28, Edited File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = []
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
listing = 1

# Get user Input
print('The Magic CD Inventory\n')
while True:
    #Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        #Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Load existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id':lstRow[0], 'album':lstRow[1], 'artist':lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()        
        
    elif strChoice == 'a':
        #Add data to the table (2d-list) each time the user wants to add data

        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID':listing, 'album':strTitle, 'artist':strArtist}
        lstTbl.append(dicRow)
        listing += 1
    
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, Album, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    
    
    elif strChoice == 'd':
        # Delete an entry
        cdDel = input('Enter the ID of the CD you wish to delete: ')
        cdDel = int(cdDel)
        for row in lstTbl:
            if row['ID'] == cdDel:
                lstTbl.remove(row) 
        
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
        
    else:
        print('Please choose either l, a, i, d, s or x!')

