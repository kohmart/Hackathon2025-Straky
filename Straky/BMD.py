import json

test_data = {
    "test_case_id": "4.1.1.1",
    "title": "Create Purchase Requisition (Standard)",
    "role": "Purchaser",
    "fiori_app": {
        "name": "Manage Purchase Requisitions - Professional",
        "id": "F2229"
    },
    "steps": [
        {
            "step_name": "Log on",
            "action": "Login to SAP Fiori launchpad",
            "expected_result": "Fiori launchpad is displayed"
        },
        {
            "step_name": "Open App",
            "action": "Open 'Manage Purchase Requisitions - Professional'",
            "expected_result": "App screen is displayed"
        },
        {
            "step_name": "Create New",
            "action": "Click 'Create' to start new requisition",
            "expected_result": "New Purchase Requisition screen is shown"
        },
        {
            "step_name": "Enter Header Data",
            "fields": {
                "Document Type": "NB",
                "Automatic Source Determination": True
            }
        },
        {
            "step_name": "Enter Item 1",
            "fields": {
                "Material": "TG10",
                "Plant": "1010",
                "Quantity": 50,
                "Requirement Tracking Number": "Test_Track",
                "Purchasing Group": "001"
            }
        },
        {
            "step_name": "Enter Item 2",
            "fields": {
                "Material": "TG11",
                "Plant": "1010",
                "Quantity": 30,
                "Requirement Tracking Number": "Test_Track",
                "Purchasing Group": "001"
            }
        },
        {
            "step_name": "Submit",
            "action": "Click 'Create' to save requisition",
            "expected_result": "Purchase Requisition is saved"
        }
    ]
}

with open("test_create_purchase_requisition.json", "w", encoding="utf-8") as f:
    json.dump(test_data, f, indent=2)
