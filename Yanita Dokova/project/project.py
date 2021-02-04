from flask import Flask, request
import requests, sys, json, os

server = "https://rest.ensembl.org"

app = Flask(__name__)

def get_ensembl_response(path, id, attr):
    ext = path + id + attr
    r = requests.get(server + ext, headers = { "Content-Type": "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()

    return r.json()

def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def swap_a_t(seq):
    new_seq = ""
    for base in seq:
        if base == 'A':
            new_seq += 'T'
        elif base == 'T':
            new_seq += 'A'
        else:
            new_seq += base

    return new_seq

def convert_to_fasta(decoded_seq):
    desc = ">" + decoded_seq["id"] + "." + str(decoded_seq["version"]) + " " + decoded_seq["desc"]
    result = {
        "id": desc,
        "seq": decoded_seq["seq"]
        }

    return result

def convert_to_multifasta(decoded_seq):
    result = []

    for seq in decoded_seq["seq"]:
        desc = ">" + seq["id"] + "." + str(seq["version"]) + " " + str(seq["desc"])
        result += {
            "id": desc,
            "seq": seq["seq"]
            }

    return result

def convert_to_xfasta(decoded_seq):
    desc = ">" + decoded_seq["id"]
    result = {
        "id": desc,
        "seq": decoded_seq["seq"]
        }

    return result

def get_exons(transcript, seq):
    result = []
    for exon in transcript["Exon"]:
        result.append(
            {
                "start": exon["start"],
                "end": exon["end"],
                "id": exon["id"],
                "seq": seq[exon["start"] - transcript["start"] : exon["end"] - transcript["end"]]
            }
        )

    return result

@app.route('/v1/sequence/gene/<string:id>/', methods=['GET'])
def seq_with_exons(id):
    decoded_seq = get_ensembl_response("/sequence/id/", id, "")

    gc_content_arg = request.args.get('gc_content')
    swap_arg = request.args.get('swap')
    if gc_content_arg == "true" and swap_arg == "A:T":
        result = {
            "seq": decoded_seq["seq"],
            "gc_content": gc_content(decoded_seq["seq"]),
            "swap_sequence": swap_a_t(decoded_seq["seq"])
        }

        return result
    
    decoded_exons = get_ensembl_response("/lookup/id/", id, "/?expand=1")
    exons = []
    if "Transcript" in decoded_exons:
        for transcript in decoded_exons["Transcript"]:
            exons += get_exons(transcript, decoded_seq["seq"])
    else:
        exons += get_exons(decoded_exons, decoded_seq["seq"])

    result = {
        "seq": decoded_seq["seq"],
        "exons": exons
    }

    return result

@app.route('/v1/sequence/<string:id>/', methods=['GET'])
def format_seq(id):
    decoded_seq = get_ensembl_response("/sequence/id/", id, "")
    content_type = request.args.get('content-type')

    if content_type == "multi-fasta":
        return convert_to_multifasta(decoded_seq)
    elif content_type == "x-fasta":
        return convert_to_xfasta(decoded_seq)
    elif content_type == "fasta":
        return convert_to_fasta(decoded_seq)
    else:
        return "Content-type must be fasta, x-fasta or multi-fasta"

app.run(port=8080)
