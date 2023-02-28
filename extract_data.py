ns = {
    'ram':
    'urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100',
    'rsm': 'urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100',
    'udt': 'urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100',
    'qdt': 'urn:un:unece:uncefact:data:standard:QualifiedDataType:100'   
}

# extractions des données
def extract_data_from_xml(root):
    data = {}

    float_values = ["GrandTotalAmount", "TaxTotalAmount", "TotalPrepaidAmount"]
    for value in float_values:
        data[value] = float(extract_ram_content(root, value))

    # numero de facture 
    data["FactureID"] = element_path_content(root,'.//rsm:ExchangedDocument/ram:ID')
    
    # Date de la facture 
    data["IssueDateTime"] = element_path_content(root,
    './/ram:IssueDateTime/udt:DateTimeString')

    # Numéro de TVA
    data["SpecifiedTaxRegistration"] = element_path_content(root, './/ram:SpecifiedTaxRegistration/ram:ID')
    return data


def element_path_content(root, path):
    return root.find(path, ns).text

def extract_ram_content(root, element):
    return element_path_content(root, './/ram:'+element)