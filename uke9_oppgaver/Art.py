'''
This includes all the arts for the boat project.
'''

class Art :
    def __init__(self):
        self.art_a = {       # Everything that include position A
            'a_with_items_person': "     A \n           O\\\n          /|\\\n  ^^-@-^^^/-\+",
            'a_with_items_noPerson': "     A\n\n  ^^-@-^^^---"
        }
        self.art_b = {       # Everything that include position A

        }

        self.art_boat = {    # everything that includes boat
            'a_boat_noItems' : "      O\n     /|\\\n  `\_/_\__/`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`",
            'a_boat_items' : "    O\n   /|\\\n `\/_\_@_/`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`"
        }


art = Art()
print art.art_boat['a_boat_noItems']
print art.art_boat['a_boat_items']