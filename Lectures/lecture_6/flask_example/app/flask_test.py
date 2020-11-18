from flask import Flask, render_template, request, make_response, redirect, url_for, abort, session, jsonify
import requests, json
import os

app = Flask(__name__)
server = "https://rest.ensembl.org"

@app.route('/family/<name>')
def index(name):
    ext = "/family/id/"+str(name)+"?"
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
    result = r.text
    object_result = json.loads(result)  
    geneStableId = object_result["members"][0]["gene_stable_id"]
    return geneStableId

@app.route("/protein", methods=['POST'])
def postBody():
    print(request.get_data())
    return request.get_data()

@app.route("/protein/<id>")
def protein(id):
    r = requests.get(server+str("/lookup/id/")+str(id), headers={ "Content-Type" : "application/json"})
    object_result = json.loads(r.text)  
    assemblyName = object_result["assembly_name"]
    return assemblyName


# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)