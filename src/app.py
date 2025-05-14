from frontend import ExcelValidadorUI
from backend import process_excel

def main():
    # Initialize the UI
    ui = ExcelValidadorUI()
    
    # Set the page configuration
    #ui.set_page_config()
    
    # Display the header
    ui.display_header()
    
    #Upload the file
    uploaded_file = ui.upload_file()
    
    if uploaded_file:
        result, erros = process_excel(uploaded_file)
        ui.display_results(result,erros)


if __name__ == "__main__":
    main()