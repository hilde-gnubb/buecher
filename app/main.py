import numpy as np
import streamlit as st
from links import FROH, TRAURIG
import pandas as pd
state = st.session_state

st.title("Bücher")
if "bücherListe" not in state:
    state["bücherListe"] = []

st.subheader("Wunschliste:")
if "wunschListe" not in state:
    state["wunschListe"] = []

if st.button("Buch hinzufügen", key="wunsch"):
    state["wunschListe"].append({"Titel": "", "Autor": "", "Preis": "", "gekauft": False})
    #wunschliste.append({"Titel": "", "Autor": "", "gelesen": False})    

df = pd.DataFrame(
    state["wunschListe"],
    #wunschliste,
    #columns=["Titel", "Autor", "gelesen"]
)
#df = df.astype({"Titel": str, "Autor": str, "gelesen": bool})

edited_df = st.data_editor(
    df,
    key = "wunsch_editor",
    column_config={
    # Checkbox für Boolean (dein Beispiel "gelesen")
    "gelesen": st.column_config.CheckboxColumn(
        "Gelesen?",
        default=False,
    )
    }
)

edited_df = edited_df.to_dict(orient="records")

st.write(edited_df)

for buch in list(edited_df):
    if buch["gekauft"] == True:
        state["bücherListe"].append({"Titel": buch["Titel"], "Autor": buch["Autor"], "gelesen": False})
        edited_df.remove(buch)
            



st.subheader("Im Besitz:")

if st.button("Buch hinzufügen", key="bücher"):
    state["bücherListe"].append({"Titel": "", "Autor": "", "gelesen": False})
    #bücherliste.append({"Titel": "", "Autor": "", "gelesen": False})    

df = pd.DataFrame(
    state["bücherListe"],
    #bücherliste,
    #columns=["Titel", "Autor", "gelesen"]
)
#df = df.astype({"Titel": str, "Autor": str, "gelesen": bool})

edited_df = st.data_editor(
    df,
    key = "bücher_editor",
    column_config={
    # Checkbox für Boolean (dein Beispiel "gelesen")
    "gelesen": st.column_config.CheckboxColumn(
        "Gelesen?",
        default=False,
    )
    }
)
st.write(state["bücherListe"])
#wenn gekauft geklickt wird muss es aus der wunschliste entfernt werden
#und in die bücherliste hinzugefügt werden.