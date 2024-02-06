from bulk_combine import RPA_File_Month_Combine
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from logger_setup import logger
from datetime import datetime as dt
from tkinter import messagebox

if __name__ == '__main__':
    use_case_list = ["CSE1235", "CSE1236", "TES1249", "TES6146", "MCD MCO", "MCR ADV", "MCR PARTB", "MNP", "NCOA", "PRINT IS", "BD IS PRINTING"]
    while True:
        try:
            logger.info("Asking user to specify which use case to combine")
            use_case_index = sd.askinteger(
                "Question", 
                "Please select which use case you would like to combine. \n0 = All \n1 = 1235; \n2 = 1236; \n3 = 1249; \n4 = 6146; \n5 = MCD MCO \n6 = MCR ADV; \n7 = PARTB Inact; \n8 = MNP; \n9 = NCOA; \n10 = IS PRINT; \n11=BD IS Printing", 
                minvalue=0, 
                maxvalue=len(use_case_list)+1
            )
            use_case_index -= 1
            logger.debug(f"Using index {use_case_index}")
        except TypeError:
            logger.error("No use case selected.")
            logger.info("Stopping Process")
            exit()
        else:    
            today = dt.today()
            logger.info(f'Current month and year: {dt.strftime(today, "%m/%Y")}')
            logger.info('Confirming month with user')
            answer = messagebox.askyesno(f"Date Confirmation", f"Do you want to run for the month of {dt.strftime(today, '%B %Y')}?")
            if not answer:
                logger.debug('Current month & year not selected')
                logger.info('Asking user to select month to be combined')
                month = sd.askinteger("Follow Up", "Please enter a month number (e.g. March = 3): ", minvalue=1, maxvalue=12)
                year = sd.askinteger("Follow Up", "Please enter a year: ", minvalue=2020, maxvalue=2030)
                if month == "" or year == "":
                    logger.critical("No month or year selected")
                    logger.info("Stopping Process")
                    exit()
            else:
                month = 0
                year = 0
            
            if use_case_index == -1:
                logger.info("Combining all use cases")
                for use_case in use_case_list:
                    try:
                        combine = RPA_File_Month_Combine(use_case=use_case, today=today, month=month, year=year)
                        combine.get_date_and_date_strings()
                        combine.format_name()
                        combine.get_files()
                        combine.combine_files()
                        combine.export_to_excel()
                    except ValueError or AttributeError:
                        continue
            else:
                combine = RPA_File_Month_Combine(use_case=use_case_list[use_case_index], today=today, month=month, year=year)
                combine.get_date_and_date_strings()
                combine.format_name()
                combine.get_files()
                combine.combine_files()
                combine.export_to_excel()

        answer = mb.askyesno("Question", "Do you want to combine another use case?")
        if not answer:
            logger.success("Program ended by user request")
            logger.info("Stopping Process")
            exit()