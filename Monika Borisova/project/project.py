import requests
import json
from flask import Flask, request
from Bio.SeqUtils import GC

app = Flask(__name__)

server = "https://rest.ensembl.org"
gene_id = "/sequence/id/"
exon_ext = "/lookup/id/"

# Transcripts and Exon function
def get_gene(transcripts, sequence):
    result = list()

    for transcript in transcripts:
        for exon in transcript['Exon']:
            result.append(
                {"start": exon["start"],
                 "end": exon["end"],
                 "id": exon["id"],
                 "seq": sequence[exon["start"]:exon["end"]]
                 })

    return result

# getting sequence and exons, Get request by default
@app.route('/v1/sequence/gene/id/<id>/')
def get_sequence(id):
    # in json format
    sequence = requests.get(server + gene_id + id,
                            headers={"Content-Type": "application/json"}).json()
    exons = requests.get(server + exon_ext + id + '?expand=1',
                         headers={"Content-Type": "application/json"}).json()

    # from the dictionary sequence, getting the value behind key seq
    seq = sequence["seq"]

    gcContent = request.args.get("gc_content")
    swap = request.args.get("swap")
    contentType = request.args.get("content-type")

    # if we have ?gc_content=true&swap=A:T
    if (gcContent == "true" or swap is not None):
        result = {"seq": seq}

        # check if gcContent is true and return calculated G and C content. The percentage is calculated against the full length. (0-100) - Biopython
        if (gcContent == "true"):
            result["gc_content"] = GC(seq)

        # check if swap is given and split by : for (A:T), swap the amino acids A with T
        if (swap is not None):
            swap = swap.split(":")
            result["swap_sequence"] = swapFunction(seq, swap[0], swap[1])

        return result

    # fasta, x-fasta, multi-fasta
    elif contentType:
        return sequenceByContentType(id, sequence, contentType)

    # default whole sequence and all the exons
    else:
        returnExons = get_gene(exons.get('Transcript'), str(sequence['seq']))
        return {'seq': sequence, 'exons': returnExons}


# swap function for A and T
def swapFunction(seq, n1, n2):
    seq = seq.replace(n1, 'S')
    seq = seq.replace(n2, n1)
    seq = seq.replace('S', n2)

    return seq

# different formats in query
def sequenceByContentType(id, sequence, contentType):
    if contentType == "fasta":
        return {"seq": sequence, "id": ">" + id}
    elif contentType == "x-fasta":
        return xFasta(id, sequence)
    elif contentType == "multi-fasta":
        return multiFasta(id, sequence)


def xFasta(id, sequence):
    description = ">" + sequence["id"]
    return description + "\n" + sequence["seq"]


def multiFasta(id, sequence):
    result = ""
    for seq in sequence:
        desc = ">" + sequence["id"] + "." + \
            str(sequence["version"]) + " " + sequence["desc"]
        result += desc + "\n" + seq

    return result

# run
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)


# Test:
# http://127.0.0.1:5000/v1/sequence/gene/id/ENSG00000157764/
# http://127.0.0.1:5000/v1/sequence/gene/id/ENSG00000157764/?gc_content=true&swap=A:T
# http://127.0.0.1:5000/v1/sequence/gene/id/ENSG00000157764/?content-type=fasta
# http://127.0.0.1:5000/v1/sequence/gene/id/ENSG00000157764/?content-type=x-fasta
# http://127.0.0.1:5000/v1/sequence/gene/id/ENSG00000157764/?content-type=multi-fasta
