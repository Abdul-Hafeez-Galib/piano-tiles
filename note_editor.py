import json

twinkle_twinkle = ['c4', 'c4', 'g4', 'g4', 'a4', 'a4', 'g4',
                   'f4', 'f4', 'e4', 'e4', 'd4', 'd4', 'c4',
                   'g5', 'g5', 'f4', 'f4', 'e4', 'e4', 'd4',
                   'g5', 'g5', 'f4', 'f4', 'e4', 'e4', 'd4',
                   'c4', 'c4', 'g4', 'g4', 'a4', 'a4', 'g4',
                   'f4', 'f4', 'e4', 'e4', 'd4', 'd4', 'c4',
                   ]

happy_birthday = ["g4", "g4", "a4", "g4", "c5", "b4",
                  "g4", "g4", "a4", "g4", "d5", "c5",
                  "g4", "g4", "g5", "e5", "c5", "b4", "a4",
                  "f5", "f5", "e5", "c5", "d5", "c5"]

jan_gan_man = ['c5', 'd5', 'e5', 'e5', 'e5', 'e5', 'e5',
               'e5', 'e5', 'e5', 'e5', 'd5', 'e5', 'f5',
               'e5', 'e5', 'e5', 'd5', 'd5', 'd5', 'b4',
               'd5', 'c5', 'c5', 'g5', 'g5', 'g5', 'g5',
               'g5', 'f-5', 'g5', 'g5', 'g5', 'f-5', 'a5',
               'g5', 'f5', 'f5', 'f5', 'e5', 'e5', 'f5',
               'd5', 'f5', 'e5', 'e5', 'e5', 'e5', 'e5',
               'd5', 'g5', 'g5', 'g5', 'f5', 'f5', 'e5',
               'e5', 'e5', 'd5', 'd5', 'd5', 'd5', 'b4',
               'd5', 'c5', 'c5', 'd5', 'e5', 'e5', 'e5',
               'e5', 'd5', 'e5', 'f5', 'e5', 'f5', 'g5',
               'g5', 'g5', 'f5', 'e5', 'd5', 'f5', 'e5',
               'e5', 'e5', 'd5', 'd5', 'd5', 'd5', 'b4',
               'd5', 'c5', 'g5', 'g5', 'g5', 'g5', 'g5',
               'g5', 'f-5', 'g5', 'g5', 'g5', 'f-5', 'a5',
               'g5', 'f5', 'f5', 'f5', 'e5', 'e5', 'f5',
               'df', 'e5', 'c5', 'b4', 'c5', 'b4', 'a5',
               'b4', 'a5', 'g5', 'a5', 'c5', 'c5', 'd5',
               'd5', 'e5', 'e5', 'd5', 'e5', 'f5']

o_mere_dil_ke_chain = ['a4', 'g4', 'a4', 'a4', 'g4', 'a4',
                       'g4', 'e4', 'b4', 'g4', 'a4', 'a4',
                       'g4', 'a4', 'g4', 'e4', 'g4', 'e4',
                       'd4', 'd4', 'e4', 'e4', 'g4', 'g4',
                       'a4', 'a4', 'b4', 'b4', 'g4', 'a4',
                       'b4', 'b4', 'g4', 'a4', 'c5', 'b4',
                       'a4', 'c5', 'b4', 'a4', 'c5', 'b4', 'a4']

naruto_theme = ['a4', 'b4', 'a4', 'g4', 'e4', 'g4', 'a4', 'd4',
                'c4', 'd4', 'c4', 'a3', 'b3', 'a4', 'b4', 'a4',
                'g4', 'e4', 'g4', 'a4', 'd4', 'c4', 'd4', 'c4',
                'a3', 'a3', 'e4', 'd4', 'c4', 'a3', 'e4', 'd4',
                'e4', 'a4', 'c5', 'b4', 'a4', 'g4', 'a4', 'e4',
                'd4', 'e4', 'd4', 'b3', 'a3', 'a3', 'e4', 'd4',
                'c4', 'a3', 'e4', 'd4', 'e4', 'a4', 'c5', 'b4',
                'a4', 'g4', 'a4', 'e4', 'g4', 'a4', 'a4', 'b4',
                'a4', 'g4', 'e4', 'g4', 'a4', 'd4', 'c4', 'd4',
                'c4', 'a3', 'b3', 'g3', 'a4', 'b4', 'a4', 'g4',
                'e4', 'g4', 'a4', 'd4', 'c4', 'd4', 'c4', 'a3',
                'a3', 'e4', 'd4', 'c4', 'a3', 'e4', 'd4', 'e4',
                'a4', 'c5', 'b4', 'a4', 'g4', 'a4', 'e4', 'd4',
                'e4', 'd4', 'b3', 'a3', 'a3', 'e4', 'd4', 'c4',
                'a3', 'e4', 'd4', 'e4', 'a4', 'c5', 'b4', 'a4',
                'g4', 'a4', 'e4', 'g4', 'a4', 'a4', 'b4', 'a4',
                'g4', 'e4', 'g4', 'a4', 'd4', 'c4', 'd4', 'c4',
                'a3', 'b3', 'g3', 'a4', 'b4', 'a4', 'g4', 'e4',
                'g4', 'a4', 'd4', 'c4', 'd4', 'c4', 'a3']

notes = {
    '1': twinkle_twinkle,
    '2': happy_birthday,
    '3': jan_gan_man,
    '4': o_mere_dil_ke_chain,
    '5': naruto_theme
}

with open('notes.json', 'w') as file:
    json.dump(notes, file)
