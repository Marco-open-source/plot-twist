"""Fixed story content for "The Missing Necklace". Nothing here changes while playing."""

START_SCENE = "hall"

LOCKED_MESSAGE = "The door is locked. You need a key."

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
        "text": "Copper pots hang above a cold stove. There is nothing useful here yet.",
        "exits": ["hall"],
    },
    "study": {
        "title": "The Study",
        "text": "The key turns and the door swings open. A desk, a safe and a half-finished letter wait in the dim light.",
        "exits": ["hall"],
    },
}

# Routes that need an item in the inventory before the player can enter.
LOCKED_ROUTES = {"study": "key"}
