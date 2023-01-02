import pymongo

client = pymongo.MongoClient('')

AML = client["AML"]
AML_lnc = AML["lnc"]
AML_pc = AML["Protein-coding"]

APL = client["APL"]
APL_lnc = APL["lnc"]
APL_as = APL["alternative-splicing"]
APL_pc = APL["Protein-coding"]

BcellAll = client["B-Cell-ALL"]
BcellAll_lnc = BcellAll["lnc"]
BcellAll_pc = BcellAll["Protein-coding"]

CLL = client["CLL"]
CLL_lnc = CLL["lnc"]
CLL_as = CLL["alternative-splicing"]
CLL_pc = CLL["Protein-coding"]

CML = client["CML"]
CML_lnc = CML["lnc"]
CML_pc = CML["Protein-coding"]

MDS = client["MDS"]
MDS_lnc = MDS["lnc"]
MDS_pc = MDS["Protein-coding"]

PreBCellALL = client["Pre-B-Cell-ALL"]
PreBCellALL_lnc = PreBCellALL["lnc"]
PreBCellALL_pc = PreBCellALL["Protein-coding"]

TcellAll = client["T-Cell-ALL"]
TcellAll_lnc = TcellAll["lnc"]
TcellAll_as = TcellAll["alternative-splicing"]
TcellAll_pc = TcellAll["Protein-coding"]

aCML = client["aCML"]
aCML_lnc = aCML["lnc"]
aCML_pc = aCML["Protein-coding"]
aCML_as = aCML["alternative-splicing"]

    
lnc_dic = {'AML':AML_lnc,'APL':APL_lnc,'B-Cell-ALL':BcellAll_lnc,'CLL':CLL_lnc,'CML':CML_lnc,'MDS':MDS_lnc,'Pre-B-Cell-ALL':PreBCellALL_lnc,'T-Cell-ALL':TcellAll_lnc,'aCML':aCML_lnc}
pc_dic = {'AML':AML_pc,'APL':APL_pc,'B-Cell-ALL':BcellAll_pc,'CLL':CLL_pc,'CML':CML_pc,'MDS':MDS_pc,'Pre-B-Cell-ALL':PreBCellALL_pc,'T-Cell-ALL':TcellAll_pc,'aCML':aCML_pc}
as_dic = {'APL':APL_as,'CLL':CLL_as,'T-Cell-ALL':TcellAll_as,'aCML':aCML_as}
search_dic = {"lnc":lnc_dic,"pc":pc_dic,"as":as_dic}

class db_search(object):

    lnc_pc_list = ["AML","APL","B-Cell-ALL","CLL","CML","MDS","Pre-B-Cell-ALL","T-Cell-ALL","aCML"]
    as_list = ["APL","CLL","T-Cell-ALL","aCML"]

    def get_data_(self,dic):
        return_dic = {}
        num = 1
        if dic['data_type'] == 'as':
            for single_record in search_dic[dic['data_type']][dic['cell_type']].find({'geneID':dic['id']}):
                single_record.pop('_id')
                return_dic[num] = single_record
                num += 1
            return return_dic
        for single_record in search_dic[dic['data_type']][dic['cell_type']].find({'id':dic['id']}):
            single_record.pop('_id')
            return_dic[num] = single_record
            num += 1 
        return return_dic

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
        return return_dic






