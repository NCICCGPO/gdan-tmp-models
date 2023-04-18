def cnvr_converter(data_symbol_list, cancer):
    '''input list of gene symbol (gene name) strings for CNVR. output feature name in TMP nomenclature'''
    import json
    # Open conversion file and convert
    with open('tools/ft_name_convert/symbol2tmp_{}_CNVR.json'.format(cancer), 'r') as fh:
        symbol2tmp = json.load(fh)

        results = []
        for e in data_symbol_list:
            try:
                results.append(symbol2tmp[e]['TMP_representative_ft'])
            except:
                results.append('nan')
    return results


def gexp_converter(data_entrez_list, cancer):
    '''input list of entrez strings for GEXP. output feature name in TMP nomenclature'''
    import json
    # Open conversion file and convert
    with open('tools/ft_name_convert/entrez2tmp_{}_GEXP.json'.format(cancer), 'r') as fh:
        entrez2tmp = json.load(fh)
        results = []
        for e in data_entrez_list:
            try:
                results.append(entrez2tmp[e])
            except:
                results.append('nan')
    return results
