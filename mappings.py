rd_Status_crosswalk = {
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

rd_scenario_crosswalk = {
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

columns = [
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
