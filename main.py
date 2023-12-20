from bulk_combine import RPA_File_Month_Combine

if __name__ == '__main__':
    use_case_list = ["CSE1235", "CSE1236", "TES1249", "TES6146", "MCD MCO", "MCR ADV", "MCR PARTB", "MNP", "NCOA", "PRINT IS"]
    for use_case in use_case_list:
        RPA_File_Month_Combine(use_case=use_case)