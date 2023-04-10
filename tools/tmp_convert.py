def cnvr_converter(data_symbol_list, cancer):
    '''input list of gene symbol (gene name) strings for CNVR. output feature name in TMP nomenclature'''
    import json

    # Open conversion file and convert
    with open('tools/entrez2tmp_{}_CNVR.json'.format(cancer), 'r') as fh:
        entrez2tmp = json.load(fh)
    return [entrez2tmp[e]['TMP_representative_ft'] for e in data_symbol_list]

def gexp_converter(data_entrez_list, cancer):
    '''input list of entrez strings for GEXP. output feature name in TMP nomenclature'''
    import json

    # Open conversion file and convert
    with open('tools/entrez2tmp_{}_GEXP.json'.format(cancer), 'r') as fh:
        entrez2tmp = json.load(fh)
    return [entrez2tmp[e] for e in data_entrez_list]
