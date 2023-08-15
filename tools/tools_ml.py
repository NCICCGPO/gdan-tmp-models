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

def get_model_info(method, platform, cancer):
    '''retrieves TMP model information
    includes: model name, model parameters, and feature list (reported in TMP nomenclature)

    specify which model you would like to look at. example: top performing jadbio gene expression only model

    options method = ['skgrid', 'aklimate', 'cloudforest', 'subscope', 'jadbio']
    options platform = ['GEXP', 'CNVR', 'MIR', 'MUTA', 'METH']
    options cancer = ['BRCA', 'LGGGBM', 'COADREAD', 'SKCM', 'ACC', 'BLCA', 'CESC', 'ESCC', 'GEA', 'HNSC', 'KIRCKICH', 'KIRP', 'LIHCCHOL', 'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'SARC', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UVM']
    '''
    import json

    with open('tools/model_info.json', 'r') as fh:
        data = json.load(fh)
    return data[method][cancer][platform]