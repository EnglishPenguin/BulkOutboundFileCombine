from bulk_combine import RPA_File_Month_Combine

if __name__ == '__main__':
    file_path = "M:/CPP-Data/Sutherland RPA/Coding/CSE1236"
    out_path = "M:/CPP-Data/Sutherland RPA/Coding/CSE1236/References/Monthly Combined"
    use_case = "CSE 1236"
    RPA_File_Month_Combine(file_path=file_path, out_path=out_path, use_case=use_case)