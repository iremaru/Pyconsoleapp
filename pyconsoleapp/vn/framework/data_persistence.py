import json

# -----------------------
#       DATA PERSISTENCE - DATA
# -----------------------

__SCENES__ = []
__STATS__ = {
    'gameScenes': [
        {
            'sceneID': 'ID',
            'scenePassages': [
                {
                    'passageID': 'ID',
                    'passagetype': 'narration/dialogue/fork',
                    'text': ''
                }
            ]
        }
    ],
    'historyAtStart': {
        'conditions': {
            'toStartScene' : {},
            'others' : {}},
        'characters' : {
            'mainCharacter': {
                'name': 'Prota',
                'health': 100 
            },
            'characterA' : {
                'name': '',
                'health': 100,
                'friendPoints': 0,
            },
            'characterB' : {
                'name': '',
                'health': 100,
                'friendPoints': 0,
            }
        },
    },
    'historyCurrently': [
        {
            'name': '',
            'data': {}
        }
    ]
}

__SAVE_FILE_PATH__ = 'vn/build/saves/'
__SAVE_FILE_NAME__ = 'sv'
__SAVE_FILE_EXTENSION__ = '.vn'
__DEFAULT_NEW_GAME_NAME__ = 'New Game'

__SAVE_FILE_DATA__ = [
    {
        'save name': None,
        'conditions': {
            'toStartScene' : {},
            'others' : {}},
        'characters' : {
            'mainCharacter': {
                'name': 'Prota',
                'health': 100 
            },
            'characterA' : {
                'name': '',
                'health': 100,
                'friendPoints': 0,
            },
            'sideCharacter' : {
                'name': '',
            }
        },
        'currentScene': None,
        'currentPassage': None,
    }
]

# -----------------------
#       DATA PERSISTENCE - PUBLIC METHODS
# -----------------------

def get_save_game_list():
    return __SAVE_FILE_DATA__

def __generate_save_file():
    with open(__SAVE_FILE_PATH__ + __SAVE_FILE_NAME__ + __SAVE_FILE_EXTENSION__, 'w') as save_file:
        save_file.write( json.dumps(__STATS__['historyAtStart']) )

def fill_save_file_data():
    with open(__SAVE_FILE_PATH__ + __SAVE_FILE_NAME__  + __SAVE_FILE_EXTENSION__, 'w') as save_file:
        global __SAVE_FILE_DATA__
        __SAVE_FILE_DATA__ = json.loads( save_file.read() )

def save_game():
    with open(__SAVE_FILE_PATH__ + __SAVE_FILE_NAME__  + __SAVE_FILE_EXTENSION__, 'w') as save_file:
        save_file.write( json.dumps(__STATS__['historyCurrently']) )