from glob import glob
import pandas as pd
from datetime import datetime as dt
from logger_setup import logger
from tkinter import simpledialog as sd
from tkinter import messagebox
import mappings


class RPA_File_Month_Combine():
    def __init__(self, use_case):
        self.use_case = use_case
        self.file_path = mappings.use_case_dict[f"{self.use_case}"]["file_path"]
        self.out_path = mappings.use_case_dict[f"{self.use_case}"]["out_path"]
        self.status_crosswalk = mappings.use_case_dict[f"{self.use_case}"]["status_crosswalk"]
        self.scenario_crosswalk = mappings.use_case_dict[f"{self.use_case}"]["scenario_crosswalk"]
        self.use_case_columns = mappings.use_case_dict[f"{self.use_case}"]["columns"]
        self.name_format_str = mappings.use_case_dict[f"{self.use_case}"]["name_format"]
        self.columns_crosswalk = mappings.use_case_dict[f"{self.use_case}"]["column_crosswalk"]
        
        # Retrieve today's date and confirm with user 
        self.today = dt.today()
        logger.info(f'Starting combine process for {self.use_case}')
        logger.info(f'Current month and year: {dt.strftime(self.today, "%m/%Y")}')
        logger.info('Confirming month with user')
        answer = messagebox.askyesno(f"{self.use_case}", f"Do you want to run for the month of {dt.strftime(self.today, '%B %Y')}?")
        if not answer:
            logger.debug('Current month & year not selected')
            logger.info('Asking user to select month to be combined')
            # ask user to select a month number
            self.month = sd.askinteger("Follow Up", "Please enter a month number (e.g. March = 3): ", minvalue=1, maxvalue=12)
            self.year = sd.askinteger("Follow Up", "Please enter a year: ", minvalue=2020, maxvalue=2030)
            if self.month == "":
                logger.critical("No month selected")
                logger.info("Stopping Process")
                exit()
            try:
                # set date variables to month selected by user
                date = self.today.replace(month=self.month)
                date = date.replace(year=self.year)
                self.month_str = dt.strftime(date, "%m")
                self.today_str = dt.strftime(date, "%m/%Y")
                self.month_name = dt.strftime(date, "%B")
                self.year_str = dt.strftime(date, "%Y")
            except TypeError:
                logger.critical("No month selected")
                logger.info("Stopping Process")
                exit()
        else:
            # set date variables to current month
            self.month_str = dt.strftime(self.today, "%m")
            self.month_name = dt.strftime(self.today, "%B")
            self.today_str = dt.strftime(self.today, "%m/%Y")
            self.year_str = dt.strftime(self.today, "%Y")
        
        self.name_format = self.name_format_str.format(
            file_path=self.file_path,
            month_str=self.month_str,
            year_str=self.year_str
        )

        self.get_files()
        self.combine_files()
        self.export_to_excel()

    def get_files(self):
        # retrieve the file paths and glob together into one list
        logger.info(f'Retrieving Files for {self.today_str}')
        self.files_list = glob(self.name_format)
        self.num_files = len(self.files_list)
        logger.debug(f'{self.num_files} files found to be combined')
    
    def combine_files(self):
        # take glob list and read excel. Combine dataframes into 1
        logger.debug(f'Attempting to combine files')
        self.df_list = []
        try:
            for f in self.files_list:
                df_temp = pd.read_excel(f, engine='openpyxl')
                self.df_list.append(df_temp)
            self.df_comb = pd.concat(self.df_list)
            self.df_comb = self.df_comb.loc[:, self.use_case_columns]
            self.num_lines = len(self.df_comb)
        except ValueError:
            logger.error(f'No files to combine for {self.today_str}')
            logger.info('Stopping Process')
            exit()
        else:
            # apply business status and scenario crosswalk to the files
            logger.debug('Evaluating Business Status')
            self.df_comb['Business Status'] = self.df_comb.apply(lambda row: self.get_business_status(row), axis=1)
            logger.debug('Translating Business Scenarios')
            self.df_comb['Business Scenario'] = self.df_comb.apply(lambda row: self.get_business_scenario(row), axis=1)
            # Rename the columns based on the grid
            self.df_comb.rename(columns=self.columns_crosswalk, inplace=True)
            logger.debug(f'There are {self.num_lines} lines to export')

    def get_business_status(self, row):
        # based on mappings status crosswalk, retrievel relevant business status
        # If Key not found in crosswalk, will return Unknown value
        return self.status_crosswalk.get(row['RetrievalDescription'], 'Unknown')
    
    def get_business_scenario(self, row):
        # based on mappings scenarios crosswalk, retrievel relevant business scenarios
        # If Key not found in crosswalk, will return Unknown value
        return self.scenario_crosswalk.get(row['RetrievalDescription'], 'Unknown')
    
    def export_to_excel(self):
        # save master dataframe with status/scenarios to expected file path based on use case
        logger.info(f'Attempting to export all lines to excel file')
        self.file_name = f"{self.use_case} - {self.month_name} {self.year_str} Combined Outbound"
        try:
            self.df_comb.to_excel(f"{self.out_path}/{self.file_name}.xlsx", index=False)
            logger.success(f"{self.file_name} successfully saved to {self.out_path}")
        except OSError:
            logger.critical("Failed to combine files")
            exit()
