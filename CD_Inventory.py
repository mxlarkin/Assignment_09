#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Larkin, 2021-Sep-04, Created code for adding tracks
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
boolean = False

while True:
    if lstOfCDObjects == []:
        IO.ScreenIO.print_menu_newfile()
        strChoice = IO.ScreenIO.menu_choice_newfile()
        boolean = True
        print('\nYour CD inventory is empty.')
    else:
        IO.ScreenIO.print_menu()
        strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'y\' to continue and reload from file. Otherwise reload will be cancelled.\n').strip().lower()
        if strYesNo.lower() == 'y':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        bool1 = True
        while bool1:
            try:
                cd_idx = int(input('Select the CD / Album index: '))
                bool1 = False
            except ValueError:
                print('\nCD Index selection must be an integer!')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        
        # TODO add code to handle tracks on an individual CD
        
        while True:
            if boolean == True:
                print('\nYour Track Inventory is Empty.')
                IO.ScreenIO.print_CD_menu_newfile()
                cdChoice = IO.ScreenIO.menu_CD_choice_newfile()
            else:
                IO.ScreenIO.print_CD_menu()
                cdChoice = IO.ScreenIO.menu_CD_choice()
            
            if cdChoice == 'x':
                break
            if cdChoice == 'a':
                tplTrackInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrackInfo, cd)
                IO.ScreenIO.show_tracks(cd)
                boolean = False
                continue
            elif cdChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                continue
            elif cdChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                bool2 = True
                while bool2:
                    try:
                        track_ID = int(input('\nEnter ID of track you would like to remove: '))
                        bool2 = False
                    except ValueError:
                        print('\nThe track selection must be an integer!')
                cd.rmv_track(track_ID)
                continue
            else:
                print('General Error')
            
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Enter y to save inventory to file, anything else to continue without saving.\n').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')
end = input('\nThank you for using the CD inventory program!')