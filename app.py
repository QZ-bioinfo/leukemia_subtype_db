from flask import Flask,request
from db_search import db_search
import re

app = Flask(__name__)

search_tool = db_search()

@app.route('/')
def return_blank():
    return ''

@app.route('/total')
def database_total():
    return search_tool.get_total_()

@app.route('/search',methods=["GET"])
def database_search():
    data_type = request.args.get('data_type', type=str, default='lnc')
    cell_type = request.args.get('cell_type', type=str, default='AML')
    lnc_id = request.args.get('lnc_id', type=str, default='NONHSAG058641.2')
    gene_name = request.args.get('gene_name', type=str, default='ZBP1')
    if data_type == 'lnc':
        for key in search_tool.lnc_pc_list:
            if cell_type == key:
                return search_tool.get_data_({'data_type':'lnc','cell_type':key,'id':lnc_id})
    if data_type == 'Protein-Coding-RNA':
        for key in search_tool.lnc_pc_list:
            if cell_type == key:
                return search_tool.get_data_({'data_type':'pc','cell_type':key,'gene_name':gene_name})
    if data_type == 'Alternative-Splicing':
        for key in search_tool.as_list:
            if cell_type == key:
                return search_tool.get_data_({'data_type':'as','cell_type':key,'gene_name':gene_name})
    return "{'data':[],total:0}"

@app.route('/diff',methods=["GET"])
def database_diff():
    cell_type = request.args.get('cell_type', type=str)
    lnc_id = request.args.get('lnc_id', type=str, default='NONHSAG058641.2')
    try:
        cell_type = re.search('\[(.*)\]',cell_type).group(1)
        cell_type_list = cell_type.replace(' ','').split(',')
        for i in range(len(cell_type_list)):
            if cell_type_list[i] != '':
                cell_type_list[i] = cell_type_list[i].replace(cell_type_list[i][0],'')
        print(cell_type_list)
        temp_list = []
        for i in cell_type_list:
            for key in search_tool.lnc_pc_list:
                if i == key:
                    temp_list.append(key)
                    continue
        if len(temp_list) == 0:
            return '{}'
        return search_tool.get_lnc_diff({'cell_type':temp_list,'id':lnc_id})
    except:
        return "{}"

if __name__ == "__main__":
    app.run(host='localhost',port = 8080)