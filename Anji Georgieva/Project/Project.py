from flask import Flask, request
from Bio.SeqUtils import GC
import requests, json


app=Flask(__name__)
server = "https://rest.ensembl.org"

#функция за екзоните
def get_exons(seq, object_resultE):
    exons=[]
    for e in object_resultE["Exon"]:
        exons.append({"start": e["start"],
            "end": e["end"],
            "id": e["id"],
            "seq": seq[e["start"]-object_resultE["start"]:e["end"]-object_resultE["start"]]})

    return exons  

#показва секвенцията и екзоните
@app.route('/v1/sequence/gene/<id>/') #метода по подразбиране е GET
def get_seq(id):
    extS= "/sequence/id/"+id+"?content-type=application/json"
    extE = "/lookup/id/"+id+"?content-type=application/json&expand=1"
    
    gcContent=request.args.get("gc_content")
    swap=request.args.get("swap")

    s = requests.get(server+extS)
    e = requests.get(server+extE)
    
    sresult=s.text
    eresult=e.text

    object_resultS = json.loads(sresult)
    object_resultE = json.loads(eresult)

    seq = object_resultS["seq"]

#Ако се иска съдържанието на GC или смяна на базите 
    if(gcContent=="true" or swap is not None):
#Речник със секвенцията
        result ={"seq": seq}

#проверяваме gc content
        if(gcContent=="true"):
#Връща процентното съдържание на GC и секвенцията от GC
            result["gc_content"]=GC(seq)

#Проверяваме swap
        if(swap is not None): 
#използваме ":" за разделител на базите, които разменяме 
            rep=swap.split(":")
#връща секвенцията с разменени бази А:Т 
            result["swap"]=seq.replace(rep[0],rep[1]) 
        return result
    else:
#Ако не се иска GC content или swap връща цялата секвенция и екзоните
        return { "seq": seq, "exons": get_exons(seq, object_resultE)}  


#Секвенция в специфичен формат
@app.route('/v1/sequence/<id>/') #метода по подразбиране е GET
def get_fasta(id):
    fastaType=request.args.get("content-type")
    
    extS= "/sequence/id/"+id+"?content-type=application/json"
    s = requests.get(server+extS)
    sresult=s.text
    object_resultS = json.loads(sresult)
    seq = object_resultS["seq"]

    if (fastaType=="fasta"):
        return {"seq": seq, "id": ">"+id}
    elif (fastaType=="x-fasta"):
        return{"seq": seq, "id": ">"+ id + " " + object_resultS["desc"]}

    else: 
        return "Could not parse " + fastaType


app.run()