import requests, json
from collections import Counter


geneID = "ENSG00000157764"

# provides the sequence in text format

server = "https://rest.ensembl.org"
ext = "/sequence/id/" + geneID + "?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
print(r.text)

geneSequence = r.text

# provides ids of transcripts and exons and processes the outcome 

def fetch_endpoint(server, request, content_type):

    r = requests.get(server+request, headers={ "Accept" : content_type})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    if content_type == 'application/json':
        return r.json()
    else:
        return r.text

def fetch_endpoint_POST(server, request, data, content_type):

    r = requests.post(server+request,
                      headers={ "Accept" : content_type},
                      data=data )

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    if content_type == 'application/json':
        return r.json()
    else:
        return r.text

server = "http://rest.ensembl.org/"
ext_gene = "lookup/id/" + geneID + "?expand=1"
con_json = "application/json"
ext_sequence = "/sequence/id/"
con_seq = "text/x-fasta"
get_gene = fetch_endpoint(server, ext_gene, con_json)


# for each transcript get a list of the exon ids
for transcript in get_gene['Transcript']:
	print (">", transcript['id'])
	exons = []
	for exon in transcript['Exon']:
		exons.append(exon['id'])
	
	# create a json dump of the exon ids
	exon_json = json.dumps({ "ids" : exons })
	sequences = fetch_endpoint_POST(server, ext_sequence, exon_json, con_seq)
	
	print(sequences)

# calculates GC content

elements = Counter(geneSequence)

a = (((elements["G"] + elements["C"]) / (elements["G"] + elements["C"] + elements["T"] + elements["A"]))*100)

print("GC content of", geneID, "is",  format(a, '.2f'), "%")

# modifies the sequence

print (geneSequence.replace('A','T'))