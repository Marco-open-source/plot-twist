"""Plot Twist: the Streamlit screen. Start the app with:  uv run streamlit run app.py"""

import streamlit as st

import db
import logic
import story

st.set_page_config(page_title="Plot Twist", page_icon="🔎")


def load_state():
    """The saved game, or a new one if nothing has been saved yet."""
    saved = db.load_progress(db.DB_PATH)
    if saved is None:
        return logic.new_state()
    return saved


def apply(action, *arguments):
    """Run one rule. Save and redraw only if the action was accepted."""
    state = load_state()
    new_state, message = action(state, *arguments)
    if new_state != state:
        db.save_progress(db.DB_PATH, new_state)
    st.session_state["message"] = message
    st.rerun()


def show_actions(state, scene):
    """The buttons the player can press in the current scene. Only shown while the story runs."""
    if state["scene"] == "library" and not state["drawer_emptied"]:
        if st.button("Open the drawer and take the key"):
            apply(logic.take_key)
    if state["scene"] == "kitchen" and not state["table_emptied"]:
        if st.button("Pick up the letter from the table"):
            apply(logic.take_letter)
    if state["scene"] == "confrontation":
        if st.button("Accuse the butler"):
            apply(logic.accuse)

    st.write("Where do you want to go?")
    for exit_name in scene["exits"]:
        if st.button("Go to " + story.SCENES[exit_name]["title"], key="go-" + exit_name):
            apply(logic.move, exit_name)


def show_new_game():
    """The New game button. It first asks "Are you sure?" and only then resets."""
    if st.session_state.get("confirm_new_game"):
        st.warning("Are you sure? Your progress will be lost.")
        if st.button("Yes, start over"):
            st.session_state["confirm_new_game"] = False
            apply(logic.new_game, True)
        if st.button("No, keep playing"):
            st.session_state["confirm_new_game"] = False
            apply(logic.new_game, False)
    elif st.button("New game"):
        st.session_state["confirm_new_game"] = True
        st.rerun()


def show_game():
    state = load_state()
    scene = story.SCENES[state["scene"]]

    st.title("The Missing Necklace")
    st.subheader(scene["title"])
    st.write(scene["text"])

    if state["ending"] is not None:
        st.success(story.ENDINGS[state["ending"]])
    elif "message" in st.session_state:
        st.info(st.session_state["message"])

    if state["ending"] is None:
        show_actions(state, scene)

    st.subheader("Inventory")
    if state["inventory"]:
        st.write(", ".join(state["inventory"]))
    else:
        st.write("Empty")

    show_new_game()


show_game()
