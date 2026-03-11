import numpy as np
import streamlit as st
from links import FROH, TRAURIG
import pandas as pd
state = st.session_state

st.title("Bücher")
st.subheader("Im Besitz:")
state["bücherListe"] = [
#bücherliste 
        #{"Titel": "Der Hobbit", "Autor": "J.R.R. Tolkin", "gelesen": False},
    ]


if st.button("Buch hinzufügen"):
    state["bücherListe"].append({"Titel": "", "Autor": "", "gelesen": False})
    

df = pd.DataFrame(
    state["bücherListe"],
    #bücherliste,
    #columns=["Titel", "Autor", "gelesen"]
)
#df = df.astype({"Titel": str, "Autor": str, "gelesen": bool})

edited_df = st.data_editor(
    df,
    column_config={
    # Checkbox für Boolean (dein Beispiel "gelesen")
    "gelesen": st.column_config.CheckboxColumn(
        "Gelesen?",
        default=False,
    )
    }
)

