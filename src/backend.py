def process_excel(uploaded_file):
    """
    Process the uploaded Excel file and return the data.
    """
    import pandas as pd
    import streamlit as st

    # Read the Excel file
    df = pd.read_excel(uploaded_file, sheet_name=None)

    # Display the data in the app
    st.write("Data from the uploaded Excel file:")
    for sheet_name, data in df.items():
        st.write(f"Sheet: {sheet_name}")
        st.dataframe(data)