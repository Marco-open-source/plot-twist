"""The rules of Plot Twist. Pure functions on a state dict: no screen code, no database code.

State: {"scene": str, "inventory": list of str, "drawer_emptied": bool}
Every function returns (new_state, message) and never changes the state it was given.
A rejected action returns a copy that is equal to the old state.
"""

import story


def new_state():
    """The state of a brand new game."""
    return {"scene": story.START_SCENE, "inventory": [], "drawer_emptied": False}


def _copy(state):
    return {
        "scene": state["scene"],
        "inventory": list(state["inventory"]),
        "drawer_emptied": state["drawer_emptied"],
    }


def move(state, destination):
    """Try to walk to another scene. Rejected if there is no such exit or the route is locked."""
    if destination not in story.SCENES[state["scene"]]["exits"]:
        return _copy(state), "You can't go there from here."
    needed_item = story.LOCKED_ROUTES.get(destination)
    if needed_item is not None and needed_item not in state["inventory"]:
        return _copy(state), story.LOCKED_MESSAGE
    new = _copy(state)
    new["scene"] = destination
    return new, "You go to " + story.SCENES[destination]["title"] + "."


def take_key(state):
    """Take the key from the Library drawer. Works once per game."""
    new = _copy(state)
    if state["scene"] != "library":
        return new, "There is no key here."
    if state["drawer_emptied"]:
        return new, "The drawer is empty."
    new["inventory"].append("key")
    new["drawer_emptied"] = True
    return new, "You take a brass key from the drawer."
