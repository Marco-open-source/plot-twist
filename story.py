"""Fixed story content for "The Missing Necklace". Nothing here changes while playing."""

START_SCENE = "hall"

LOCKED_MESSAGE = "The door is locked. You need a key."
STORY_OVER_MESSAGE = "The story is over."

SCENES = {
    "hall": {
        "title": "The Hall",
        "text": "You stand in the front hall of the manor. The necklace is missing and everyone is a suspect. "
        "Doors lead to the Library and the Kitchen. A heavy oak door marked Study is locked.",
        "exits": ["library", "kitchen", "study"],
    },
    "library": {
        "title": "The Library",
        "text": "Dusty shelves reach the ceiling. A small drawer in the reading desk looks like it might hold something.",
        "exits": ["hall"],
    },
    "kitchen": {
        "title": "The Kitchen",
        "text": "Copper pots hang above a cold stove. A scrubbed wooden table stands in the middle of the room.",
        "exits": ["hall"],
    },
    "study": {
        "title": "The Study",
        "text": "The key turns and the door swings open. A desk and a safe wait in the dim light. "
        "Beyond them, the butler stands by the window.",
        "exits": ["hall", "confrontation"],
    },
    "confrontation": {
        "title": "The Confrontation",
        "text": "The butler turns to face you. Everyone in the manor is listening. It is time to name the thief.",
        "exits": ["study"],
    },
}

# Routes that need an item in the inventory before the player can enter.
LOCKED_ROUTES = {"study": "key"}

ENDINGS = {
    "A": "You show the letter. The butler confesses and the necklace is returned. THE END (ending A)",
    "B": "You have no proof. The butler smiles and the thief walks free. THE END (ending B)",
}
