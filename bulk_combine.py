from glob import glob
import pandas as pd
from datetime import datetime as dt
from logger_setup import logger
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox
import mappings


class RPA_File_Month_Combine():
    def __init__(self, file_path, out_path, use_case):
        self.file_path = file_path
        self.out_path = out_path
        self.use_case = use_case
        self.today = dt.today()
        logger.info(f'Current month and year: {dt.strftime(self.today, "%m/%Y")}')
        logger.debug('Confirming Month')
        answer = messagebox.askyesno("Question", f"Do you want to run the month {dt.strftime(self.today, '%B')}?")

        if not answer:
            logger.info('Current month not selected')
            logger.debug('Confirming month to be combined')
            self.month = sd.askinteger("Follow Up", "Please enter a month number (e.g. March = 3): ", minvalue=1, maxvalue=12)
            if self.month == "":
                logger.critical("No month selected; Stopping Process")
                exit()
            try:
                date = self.today.replace(month=self.month)
                self.month_str = dt.strftime(date, "%m")
                self.today_str = dt.strftime(date, "%m/%Y")
                self.month_name = dt.strftime(date, "%B")
                self.year_str = dt.strftime(date, "%Y")
            except TypeError:
                logger.critical("No month selected; Stopping Process")
                exit()
        else:
            self.month_str = dt.strftime(self.today, "%m")
            self.month_name = dt.strftime(self.today, "%B")
            self.today_str = dt.strftime(self.today, "%m/%Y")
            self.year_str = dt.strftime(self.today, "%Y")

        self.get_files()
        self.combine_files()
        self.export_to_excel()

    def get_files(self):
        logger.info(f'Retrieving Files for {self.today_str}')
        self.files_list = glob(f"{self.file_path}/*Outbound_{self.month_str}*{self.year_str}.xlsx")
        self.num_files = len(self.files_list)
        logger.debug(f'{self.num_files} files found to be combined')
    
    def combine_files(self):
        logger.info(f'Attempting to combine files')
        self.df_list = []
        try:
            for f in self.files_list:
                df_temp = pd.read_excel(f, engine='openpyxl')
                self.df_list.append(df_temp)
            self.df_comb = pd.concat(self.df_list)
            self.df_comb = self.df_comb.loc[:, mappings.columns]
            self.num_lines = len(self.df_comb)
        except ValueError:
            logger.error(f'No files to combine for {self.today_str}')
            logger.info('Stopping Process')
            exit()
        else:
            logger.info('Translating Business Statuses')
            self.df_comb['Business Status'] = self.df_comb.apply(lambda row: self.get_business_status(row), axis=1)
            logger.info('Translating business scenarios')
            self.df_comb['Business Scenario'] = self.df_comb.apply(lambda row: self.get_business_scenario(row), axis=1)
            logger.debug(f'There are {self.num_lines} lines to export')

    def get_business_status(self, row):
        return mappings.rd_Status_crosswalk.get(row['RetrievalDescription'], 'Unknown')
    
    def get_business_scenario(self, row):
        return mappings.rd_scenario_crosswalk.get(row['RetrievalDescription'], 'Unknown')
    
    def export_to_excel(self):
        logger.info(f'Attempting to export all lines to excel file')
        self.file_name = f"{self.use_case} - {self.month_name} {self.year_str} Combined Outbound"
        try:
            self.df_comb.to_excel(f"{self.out_path}/{self.file_name}.xlsx", index=False)
            logger.success(f"{self.file_name} successfully saved to {self.out_path}")
        except OSError:
            logger.critical("Failed to combine files")
            exit()

