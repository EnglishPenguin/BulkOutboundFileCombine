rd_status_crosswalk_1236 = {
    "Patient Not Found": "Business Exception",
    "Encounter reviewed": "Business Success",
    "Pending Representative Review": "Business Exception", 
    "No Proc Code to Extract": "Technical Exception", 
    "PopUp while editing 'Proc'": "Technical Exception",
    "Update Task Failed": "Technical Exception",
    "CPT not in Crosswalk": "Business Exception", 
    "No Proc Code to Edit": "Technical Exception", 
    "Page Edit Selector Header not found": "Technical Exception", 
    "Edit Transaction Failed": "Technical Exception", 
    "": "Other"
}

rd_scenario_crosswalk_1236 = {
    "Patient Not Found": "No search results after searching for encounter",
    "Encounter reviewed": "End-to-end Success",
    "Pending Representative Review": "Multiple Edits found on encounter", 
    "No Proc Code to Extract": "Unable to determine which CPT to be modified", 
    "PopUp while editing 'Proc'": "Pop-up encountered while editing the CPT",
    "Update Task Failed": "Failed to add note to the encounter",
    "CPT not in Crosswalk": "Lookup Key Missing from Crosswalk", 
    "No Proc Code to Edit": "Unable to Extract the CPT from the Edit Descr", 
    "Page Edit Selector Header not found": "Unable to detect the Edit Selector Header screen", 
    "Edit Transaction Failed": "Unable to edit the transaction details", 
    "": "Manually excluded volume"
}

columns_1236 = [
    "PTFULLNAME",
    "INVNUM",
    "CRN#",
    "CPT",
    "Reason",
    "BotName",
    "RetrievalStatus",
    "RetrievalDescription",
    "StatusCode",
    "StatusDescription",
    "RecordAttemptCount",
    "RecordAttemptMachineName",
    "CPConfigID",
    "FileID",
    "SeqID",
    "BOTRequestDate",
    "TransactionStartDate",
    "TransactionEndDate",
    "BatchID",
    "URN",
    "CreatedDate",
    "LastModifiedBy",
    "LastModifiedDate",
    "ProcessComments"
]

use_case_file_path = {
    "CSE1235": "M:/CPP-Data/Sutherland RPA/Coding/CSE1235",
    "CSE1236": "M:/CPP-Data/Sutherland RPA/Coding/CSE1236",
    "TES1249": "M:/CPP-Data/Sutherland RPA/Coding/TES1249",
    "TES6146": "M:/CPP-Data/Sutherland RPA/Coding/TES6146"
}

use_case_out_path = {
    "CSE1235": "M:/CPP-Data/Sutherland RPA/Coding/CSE1235/Monthly Combined",
    "CSE1236": "M:/CPP-Data/Sutherland RPA/Coding/CSE1236/References/Monthly Combined",
    "TES1249": "M:/CPP-Data/Sutherland RPA/Coding/TES1249/Monthly Combined",
    "TES6146": "M:/CPP-Data/Sutherland RPA/Coding/TES6146/Monthly Combined"
}

use_case_dict = {
    "CSE1235": {
        "file_path": "M:/CPP-Data/Sutherland RPA/Coding/CSE1235",
        "out_path": "M:/CPP-Data/Sutherland RPA/Coding/CSE1235/Monthly Combined",
        "columns": [

        ],
        "status_crosswalk": {

        },
        "scenario_crosswalk": {

        },
        "name_format": "{file_path}/*Outbound_{month_str}*{year_str}.xlsx"
    },
    "CSE1236": {
        "file_path": "M:/CPP-Data/Sutherland RPA/Coding/CSE1236",
        "out_path": "M:/CPP-Data/Sutherland RPA/Coding/CSE1236/References/Monthly Combined",
        "columns": [
            "PTFULLNAME",
            "INVNUM",
            "CRN#",
            "CPT",
            "Reason",
            "BotName",
            "RetrievalStatus",
            "RetrievalDescription",
            "StatusCode",
            "StatusDescription",
            "RecordAttemptCount",
            "RecordAttemptMachineName",
            "CPConfigID",
            "FileID",
            "SeqID",
            "BOTRequestDate",
            "TransactionStartDate",
            "TransactionEndDate",
            "BatchID",
            "URN",
            "CreatedDate",
            "LastModifiedBy",
            "LastModifiedDate",
            "ProcessComments"
        ],
        "status_crosswalk": {
            "Patient Not Found": "Business Exception",
            "Encounter reviewed": "Business Success",
            "Pending Representative Review": "Business Exception", 
            "No Proc Code to Extract": "Technical Exception", 
            "PopUp while editing 'Proc'": "Technical Exception",
            "Update Task Failed": "Technical Exception",
            "CPT not in Crosswalk": "Business Exception", 
            "No Proc Code to Edit": "Technical Exception", 
            "Page Edit Selector Header not found": "Technical Exception", 
            "Edit Transaction Failed": "Technical Exception", 
            "": "Other"
        },
        "scenario_crosswalk": {
            "Patient Not Found": "No search results after searching for encounter",
            "Encounter reviewed": "End-to-end Success",
            "Pending Representative Review": "Multiple Edits found on encounter", 
            "No Proc Code to Extract": "Unable to determine which CPT to be modified", 
            "PopUp while editing 'Proc'": "Pop-up encountered while editing the CPT",
            "Update Task Failed": "Failed to add note to the encounter",
            "CPT not in Crosswalk": "Lookup Key Missing from Crosswalk", 
            "No Proc Code to Edit": "Unable to Extract the CPT from the Edit Descr", 
            "Page Edit Selector Header not found": "Unable to detect the Edit Selector Header screen", 
            "Edit Transaction Failed": "Unable to edit the transaction details", 
            "": "Manually excluded volume"
        },
        "name_format": "{file_path}/*Outbound_{month_str}*{year_str}.xlsx",
    },
    "TES1249": {
        "file_path": "M:/CPP-Data/Sutherland RPA/Coding/TES1249",
        "out_path": "M:/CPP-Data/Sutherland RPA/Coding/TES1249/Monthly Combined",
        "columns": [

        ],
        "status_crosswalk": {

        },
        "scenario_crosswalk": {

        },
        "name_format": "{file_path}/*Outbound_{month_str}*{year_str}.xlsx"
    },
    "TES6146": {
        "file_path": "M:/CPP-Data/Sutherland RPA/Coding/TES6146",
        "out_path": "M:/CPP-Data/Sutherland RPA/Coding/TES6146/Monthly Combined",
        "columns": [

        ],
        "status_crosswalk": {

        },
        "scenario_crosswalk": {

        },
        "name_format": "{file_path}/*Outbound_{month_str}*{year_str}.xlsx"
    },
}