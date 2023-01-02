from flask import Flask,request
from flask import Flask
from db_search import db_search
import re

app = Flask(__name__)

search_tool = db_search()

@app.route('/total')
def database_total():
    return search_tool.get_total_()

@app.route('/search',methods=["GET"])
def database_search():
    data_type = request.args.get("data_type", type=str, default="lnc")
    cell_type = request.args.get("cell_type", type=str, default="AML")
    geneid = request.args.get("id", type=str, default="NONHSAG058641.2")
    if data_type == "lnc":
        for key in search_tool.lnc_pc_list:
            if cell_type == key:
                return search_tool.get_data_({'data_type':'lnc','cell_type':key,'id':geneid})
    if data_type == "Protein-Coding-RNA":
        for key in search_tool.lnc_pc_list:
            if cell_type == key:
                return search_tool.get_data_({'data_type':'pc','cell_type':key,'id':geneid})
    if data_type == "Alternative-Splicing":
        for key in search_tool.as_list:
            if cell_type == key:
                return search_tool.get_data_({'data_type':'as','cell_type':key,'id':geneid})
    return '{}'
if __name__ == "__main__":
    app.run(host='localhost',port = 8080)