import pymongo
import json

client = pymongo.MongoClient('')

AML = client['AML']
AML_lnc = AML['lnc']
AML_pc = AML['Protein-coding']

APL = client['APL']
APL_lnc = APL['lnc']
APL_as = APL['alternative-splicing']
APL_pc = APL['Protein-coding']

BcellAll = client['B-Cell-ALL']
BcellAll_lnc = BcellAll['lnc']
BcellAll_pc = BcellAll['Protein-coding']

CLL = client['CLL']
CLL_lnc = CLL['lnc']
CLL_as = CLL['alternative-splicing']
CLL_pc = CLL['Protein-coding']

CML = client['CML']
CML_lnc = CML['lnc']
CML_pc = CML['Protein-coding']

MDS = client['MDS']
MDS_lnc = MDS['lnc']
MDS_pc = MDS['Protein-coding']

PreBCellALL = client['Pre-B-Cell-ALL']
PreBCellALL_lnc = PreBCellALL['lnc']
PreBCellALL_pc = PreBCellALL['Protein-coding']

TcellAll = client['T-Cell-ALL']
TcellAll_lnc = TcellAll['lnc']
TcellAll_as = TcellAll['alternative-splicing']
TcellAll_pc = TcellAll['Protein-coding']

aCML = client['aCML']
aCML_lnc = aCML['lnc']
aCML_pc = aCML['Protein-coding']
aCML_as = aCML['alternative-splicing']

Normal_white_cell = client['Normal-white-cell']
Normal_white_cell_lnc = Normal_white_cell['lnc']
    
lnc_dic = {'AML':AML_lnc,'APL':APL_lnc,'B-Cell-ALL':BcellAll_lnc,'CLL':CLL_lnc,'CML':CML_lnc,'MDS':MDS_lnc,'Pre-B-Cell-ALL':PreBCellALL_lnc,'T-Cell-ALL':TcellAll_lnc,'aCML':aCML_lnc}
pc_dic = {'AML':AML_pc,'APL':APL_pc,'B-Cell-ALL':BcellAll_pc,'CLL':CLL_pc,'CML':CML_pc,'MDS':MDS_pc,'Pre-B-Cell-ALL':PreBCellALL_pc,'T-Cell-ALL':TcellAll_pc,'aCML':aCML_pc}
as_dic = {'APL':APL_as,'CLL':CLL_as,'T-Cell-ALL':TcellAll_as,'aCML':aCML_as}
search_dic = {'lnc':lnc_dic,'pc':pc_dic,'as':as_dic}

class db_search(object):

    lnc_pc_list = ['AML','APL','B-Cell-ALL','CLL','CML','MDS','Pre-B-Cell-ALL','T-Cell-ALL','aCML']
    as_list = ['APL','CLL','T-Cell-ALL','aCML']

    def get_data_(self,dic):
        return_dic = {'data':[]}
        if dic['data_type'] == 'as':
            for single_record in search_dic[dic['data_type']][dic['cell_type']].find({'geneSymbol':dic['gene_name']}):
                single_record.pop('_id')
                return_dic['data'].append(single_record)
        if dic['data_type'] == 'lnc':
            for single_record in search_dic[dic['data_type']][dic['cell_type']].find({'id':dic['id']}):
                single_record.pop('_id')
                single_record['Mean_exp'] = float(single_record['Mean_exp'])
                return_dic['data'].append(single_record)
        if dic['data_type'] == 'pc':
            for single_record in search_dic[dic['data_type']][dic['cell_type']].find({'gene_name':dic['gene_name']}):
                single_record.pop('_id')
                single_record['Mean_exp'] = float(single_record['Mean_exp'])
                return_dic['data'].append(single_record)
        return_dic['total'] = len(return_dic['data'])
        return str(json.dumps(return_dic))

    def get_total_(self):
        return_dic = {}
        return_dic['Long-Non-Coding-RNA'] = {}
        return_dic['Protein-Coding-RNA'] = {}
        return_dic['alternative-splicing'] = {}
        for key,value in lnc_dic.items():
            return_dic['Long-Non-Coding-RNA'][key] = value.count_documents({})
        for key,value in pc_dic.items(): 
            return_dic['Protein-Coding-RNA'][key] = value.count_documents({})
        for key,value in as_dic.items(): 
            return_dic['alternative-splicing'][key] = value.count_documents({})
        return str(json.dumps(return_dic))

    def get_lnc_diff(self,dic):
        if Normal_white_cell_lnc.find_one({'id':dic['id']}) == None:
            return '{}'
        return_dic = {'Normal_white_cell':[]}
        for every_cell_type in dic['cell_type']:
            return_dic[every_cell_type] = []
            for single_record in lnc_dic[every_cell_type].find({'id':dic['id']}):
                single_record.pop('_id')
                single_record['Mean_exp'] = float(single_record['Mean_exp'])
                return_dic[every_cell_type].append(single_record)
        for single_record in Normal_white_cell_lnc.find({'id':dic['id']}):
            single_record.pop('_id')
            single_record['Mean_exp'] = float(single_record['Mean_exp'])
            return_dic['Normal_white_cell'].append(single_record)
        return str(json.dumps(return_dic))