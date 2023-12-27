from bulk_combine import RPA_File_Month_Combine
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from logger_setup import logger

if __name__ == '__main__':
    use_case_list = ["CSE1235", "CSE1236", "TES1249", "TES6146", "MCD MCO", "MCR ADV", "MCR PARTB", "MNP", "NCOA", "PRINT IS"]
    while True:
        try:
            logger.info("Asking user to specify which use case to combine")
            use_case_index = sd.askinteger(
                "Question", 
                "Please select which use case you would like to combine. \n0 = All \n1 = 1235; \n2 = 1236; \n3 = 1249; \n4 = 6146; \n5 = MCD MCO \n6 = MCR ADV; \n7 = PARTB Inact; \n8 = MNP; \n9 = NCOA; \n10 = IS PRINT ", 
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
            if use_case_index == -1:
                logger.info("Combining all use cases")
                for use_case in use_case_list:
                    RPA_File_Month_Combine(use_case=use_case)
            else:
                RPA_File_Month_Combine(use_case=use_case_list[use_case_index])

        answer = mb.askyesno("Question", "Do you want to combine another use case?")
        if not answer:
            logger.success("Program ended by user request")
            logger.info("Stopping Process")
            exit()