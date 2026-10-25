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


def show_game():
    state = load_state()
    scene = story.SCENES[state["scene"]]

    st.title("The Missing Necklace")
    st.subheader(scene["title"])
    st.write(scene["text"])

    if "message" in st.session_state:
        st.info(st.session_state["message"])

    if state["scene"] == "library" and not state["drawer_emptied"]:
        if st.button("Open the drawer and take the key"):
            apply(logic.take_key)

    st.write("Where do you want to go?")
    for exit_name in scene["exits"]:
        if st.button("Go to " + story.SCENES[exit_name]["title"], key="go-" + exit_name):
            apply(logic.move, exit_name)

    st.subheader("Inventory")
    if state["inventory"]:
        st.write(", ".join(state["inventory"]))
    else:
        st.write("Empty")


show_game()
