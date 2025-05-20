from frontend import ExcelValidadorUI
from backend import process_excel, excel_to_sql
import logging
import sentry_sdk

sentry_sdk.init(
    dsn="https://7efef447db2aa2b67c5234001a0ae52f@o4509353079865344.ingest.us.sentry.io/4509353098280960",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0
)

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
            logging.error("Validation failed. Please correct the Excel file.")
            sentry_sdk.capture_message("Validation failed :(. Please correct the Excel file")
        elif ui.display_save_message():
            excel_to_sql(df)
            ui.display_success_message()
            logging.info("File uploaded and saved to the database successfully.")

if __name__ == "__main__":
    main()