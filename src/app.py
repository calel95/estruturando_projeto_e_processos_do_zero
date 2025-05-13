from frontend import ExcelValidadorUI

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
        # Process the uploaded file
        ui.process_file(uploaded_file)


if __name__ == "__main__":
    main()