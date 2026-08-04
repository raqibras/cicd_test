RESOURCE_GROUP_TO_PROJECT_MAPPING = {
    'rg-creditai-qa-001': 'CreditAI',
    'rg-ocm20_obe-dev-001': 'OCM20 OBE',
    'rg-devaiocm1': 'Knowledge Assistant V1.0 Shared Resources',
    'rg-alta-qa-01': 'ALTA-QA',
    'rg-ka-shared_resources-001': 'Knowledge Assistant V2.0 Shared Resources',
    'rg-contractinv-qa-001': 'Contract Invoice',
    'rg-devai-contentgen': 'Content Generation',
    'rg-actpto-lz-prod-001': 'PTO-Prod',
    'rg-ocmevl-lz-public-001':'OCM Evolve Prod',
    'rg-resume-ranker-dev-001': 'Resume Ranker'
    # Add more mappings as needed
}
    
    # Resource groups to INCLUDE in the report
INCLUDED_RESOURCE_GROUPS = [
    'devaiteam',
    'rg-creditai-qa-001',
    'rg-ocm20_obe-dev-001',
    'rg-ocm20_evolve-dev-001',
    'rg-devaiocm1',
    'rg-alta-qa-01',
    'rg-ka-shared_resources-001',
    'rg-contractinv-qa-001',
    'rg-devai-contentgen',
    'rg-actpto-lz-prod-001',
    'rg-ocmevl-lz-public-001',
    'rg-ocmka20-dev',
    'rg-resume-ranker-dev-001',
    'rg-creditai-lz-public-001'
    # Add more inclusions as needed
]

# Resource-level mapping for shared resource groups
# Maps specific resource names to projects
RESOURCE_TO_PROJECT_MAPPING = {
    # Format: 'resource-name': 'Project Name'
    'prodaiwebfxapp': 'ALTA-Prod',
    'asp-devaiteam-83e2': 'ALTA-Prod',
    'prodaidb': 'ALTA-Prod',
    'prodaitranslationstorage': 'ALTA-Prod',
    'prodaitranslatorus2': 'ALTA-Prod',
    'dev-app': 'ALTA-Prod',
    'prodwebfxapp': 'ALTA-Prod',
    'ag-alta-prod-001': 'ALTA-Prod',
    'devaiwebfunctions': 'ALTA-QA',
    'asp-alta-qa-001': 'ALTA-QA',
    'settings-details': 'ALTA-QA',
    'devaitranslationstorage': 'ALTA-QA',
    'devai-translation': 'ALTA-QA',
    'apin-alta-qa-001': 'ALTA-QA',
    '7b2f5ca9-5d55-4ff0-abc9-fea4aac92490-rg-alta-qa-01-EUS2': 'ALTA-QA',
    'test-pipe': 'ALTA-QA',
    'pto-qa-backend-webapp': 'PTO-QA',
    'asp-devaiteam-8c71': 'PTO-QA',
    'pto-static-webapp': 'PTO-QA',
    'prodFinal': 'PTO-QA',
    'ag-pto-qa-alerts': 'PTO-QA',
    'settings-details': 'Shared QA Database',
    '7b2f5ca9-5d55-4ff0-abc9-fea4aac92490-devaiteam-eus2': 'Shared Resources PTO-QA,ALTA-Prod',
    'qa-azure-search': 'OBE 1.0',
    'asp-rgdevaiocm1-bc22': 'OBE 1.0',
    'logic-filesync-addupdate-bullhorn': 'OBE 1.0',
    'logic-filesync-addupdate-interimpilotjob': 'OBE 1.0',
    'logic-filesync-addupdate-CRG': 'OBE 1.0',
    'logic-filesync-addupdate-OBE': 'OBE 1.0',
    'logic-filesync-delete-OBE': 'OBE 1.0',
    'logic-filesync-delete-interimpilotjob': 'OBE 1.0',
    'logic-filesync-delete-bullhorn': 'OBE 1.0',
    'logic-filesync-delete-CRG': 'OBE 1.0',
    'azuresearch-qa-ui': 'OBE 1.0',
    'app-azuresearch-qa-evolve': 'Evolve 1.0',
    'asp-evolve-instance': 'Evolve 1.0',
    'logic-filesync-qa': 'Evolve 1.0',
    'logic-filesync-addupdate-evolve-globalservices': 'Evolve 1.0',
    'logic-filesync-addupdate-evolve-fieldsupportgroup': 'Evolve 1.0',
    'logic-filesync-addupdate-evolve-evolveEBO': 'Evolve 1.0',
    'logic-filesync-addupdate-evolve-OSGFSG': 'Evolve 1.0',
    'logic-filesync-delete-evolve-globalservices': 'Evolve 1.0',
    'logic-filesync-delete-evolve-fieldsupportgroup': 'Evolve 1.0',
    'logic-filesync-delete-evolve-OSGFSG': 'Evolve 1.0',
    'logic-filesync-delete-evolve-evolveEBO': 'Evolve 1.0',
    'swa-azuresearch-qa-evolve': 'Evolve 1.0',
    'app-azuresearch-qa-ps-esa': 'PeopleSoft ESA',
    'asp-azuresearch-qa-ps-esa': 'PeopleSoft ESA',
    'swa-azuresearch-qa-ps-esa': 'PeopleSoft ESA',
    'app-azuresearch-qa-emo': 'Evolve Middle Office',
    'swa-azuresearch-qa-emo': 'Evolve Middle Office',
    'ea-oai-sandbox': 'OpenAI (Shared)',
    'ea-oai-sandbox-project-resource': 'OpenAI (Shared)',
    'aif-pto-qa': 'PTO-QA',
    'pto-prod-backend-webapp': 'PTO-Prod (Sandbox Subscription)',
    'webapp-plan-prod': 'PTO-Prod (Sandbox Subscription)',
    'pto-prod-qa-staticwebapp': 'PTO-Prod (Sandbox Subscription)',
    'search-ocmka20-dev': 'Knowledge Assistant V2.0 Shared Resources'

    # Add more resource-to-project mappings
}