#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """

        # TODO modify method to accept a list of file names.
        file_name_CD = file_name[0]
        file_name_track = file_name[1]
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            # TODO add code to save track data to file
            with open(file_name_track, 'w') as file:
                for disc in lst_Inventory:
                    tracks = disc.cd_tracks
                    album_id = disc.cd_id
                    for item in tracks:
                        if item is not None:
                            record = '{},{}'.format(album_id, item.get_record())
                            file.write(record)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.

        """
        lst_Inventory = []
        file_name_CD = file_name[0]
        file_name_track = file_name[1]
        # TODO modify method to accept a list of file names
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    cd = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(cd)
        except FileNotFoundError:
            with open(file_name_CD, 'w') as file:
                print('\n{} has been created!'.format(file_name_CD))
        # TODO add code to load track data
        try:
            with open(file_name_track, 'r') as file:
                for row in file:
                    track_data = row.strip().split(',')
                    cd = PC.DataProcessor.select_cd(lst_Inventory, int(data[0]))
                    track = DC.Track(track_data[1], track_data[2], track_data[3])
                    cd.add_track(track)
        except FileNotFoundError:
            with open(file_name_track, 'w') as file:
                print('\n{} has been created!'.format(file_name_track))
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album to edit or display\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def print_menu_newfile():
        '''Displays menu for if no data is stored to cd/track file
        Args:
            None
        Returns:
            None
            '''
        print('\nMain Menu\n\n[a] Add CD / Album')
        print('[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod
    def menu_choice_newfile():
        '''Get user input for menu with new file
        Args:
            None
        Returns:
            choice: (string) menu choice fo user'''
        choice = ' '
        while choice not in ['a', 's', 'x']:
            choice = input('Which operation would you like to perform? [a, s, or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.
            
        Returns:
            None.
        """

        print('\nCD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x
        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def print_CD_menu_newfile():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.
            
        Returns:
            None.
        """

        print('\nCD Sub Menu\n\n[a] Add track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice_newfile():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x
        """
        choice = ' '
        while choice not in ['a', 'x']:
            choice = input('Which operation would you like to perform? [a or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory
        Args:
            Table: (list of objects) Holds CDs to compare
        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """
        bool3 = True
        while bool3:
            try:
                cdId = int(input('Enter ID: ').strip())
                bool3 = False
            except ValueError:
                print('\nThe CD ID must be an integer.')
        cdTitle = input('\nWhat is the CD\'s title? ').strip()
        cdArtist = input('\nWhat is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album


        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """
        bool4 = True
        while bool4:
            try:
                trkId = int(input('\nEnter Position on CD / Album: ').strip())
                bool4 = False
            except ValueError:
                print('\nThe Track ID must be an integer.')
                
        trkTitle = input('\nWhat is the Track\'s title? ').strip()
        trkLength = input('\nWhat is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength

