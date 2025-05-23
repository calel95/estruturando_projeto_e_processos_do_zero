import streamlit as st

class ExcelValidadorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Excel Validador de schemas"
        )
            # page_icon=":bar_chart:",
            # layout="wide",
            # initial_sidebar_state="expanded",
        # )
        # st.title("Excel Validador")
        # st.markdown(
        #     """
        #     Esta aplicación permite validar archivos Excel para asegurarse de que cumplen con los requisitos establecidos.
        #     """
        # )

    def display_header(self):
        st.title("Validador de Schemas")
        
    def upload_file(self):
        return st.file_uploader(
            "Suba o arquivo Excel",
            type=["xlsx", "xls"]
        )
    
    def display_results(self, result, error):
        if error:
            st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo Excel está correto!")

    def display_save_message(self):
        return st.button(f"Salvar no banco de dados")

    def display_success_message(self):
        return st.success("O arquivo foi carregado com sucesso!")

    def display_wrong_message(self):
        return st.error("Precisa corrigir a planilha")