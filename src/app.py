from frontend import ExcelValidadorUI
from backend import process_excel, excel_to_sql
from logging import error, info

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
        df, result, error = process_excel(uploaded_file)
        ui.display_results(result,error)

        if error:
            ui.display_wrong_message()
        elif ui.display_save_message():
            excel_to_sql(df)
            ui.display_success_message()
            info("File uploaded and saved to the database successfully.")

if __name__ == "__main__":
    main()