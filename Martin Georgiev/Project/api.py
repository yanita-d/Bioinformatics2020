from flask import Flask, request
import requests, json
from Bio.SeqUtils import GC

app = Flask(__name__)
ensembl_server = 'https://rest.ensembl.org'

#check for errors
def check_status(r):
    if not r.ok:
        r.raise_for_status()
        sys.exit()

def swapSeq(seq, first, second):
    swapping = {'A':'T', 'T':'A'}
    res = ''
    for i in range(len(seq)):
        if(seq[i] in swapping):
            res += swapping[seq[i]]
        else:
            res += seq[i]
    return res

def getSeqData(id):
    seq_result = requests.get(ensembl_server + '/sequence/id/' + id + '?content-type=application/json')
    check_status(seq_result)
    return seq_result.json()

def getSeqDataLookup(id):
    transcript_result = requests.get(ensembl_server + '/lookup/id/' + id + '?content-type=application/json&expand=1')
    check_status(transcript_result)
    return transcript_result.json()

def getExons(id, sequence):
    transcript = getSeqDataLookup(id)
        
    exons = []
    for tr in transcript['Transcript']:
        for exon in tr['Exon']:

            current = {}
            current['start'] = exon['start']
            current['id'] = exon['id']
            current['seq'] = sequence[exon['start']-transcript['start']:exon['end']-transcript['start']]
            current['end'] = exon['end']
            exons.append(current)
    return exons

def fasta(seq_data):
    return {"seq": seq_data['seq'], "id": '>' + seq_data['id']}

def x_fasta(seq_data):
    return {"seq": seq_data['seq'], "id": '>' + seq_data['id'] + seq_data['desc']}

def multi_fasta(id):
    sequence = getSeqData(id)['seq']
    transcript_data = getSeqDataLookup(id)

    result = ''

    for tr in transcript_data['Transcript']:
        for exon in tr['Exon']:
            result += str('> id:' + exon['id'] + '\n' + sequence[exon['start']-transcript_data['start']:exon['end']-transcript_data['start']] + '\n')

    return result

def format_output(id, format):
    if format == 'fasta':
        return fasta(getSeqData(id))
    elif format == 'x-fasta':
        return x_fasta(getSeqData(id))
    else:
        return multi_fasta(id)

@app.route('/v1/sequence/gene/<id>/', methods=['GET'])
def gene_data(id):

    if(request.args.get('gc_content') is None or request.args.get('swap') is None):
        gene_seq_exons = {}
        
        #get sequence and add to result dictionary
        sequence = getSeqData(id)['seq']
        gene_seq_exons['sequence'] = sequence

        #get exons and add to result dictionary
        exons = getExons(id, sequence)
        gene_seq_exons['exons'] = exons
        
        return gene_seq_exons
    else:
        gene_seq_data = {}
        swapLetters = request.args.get('swap').split(':')

        sequence = getSeqData(id)['seq']
        gene_seq_data['sequence'] = sequence
        gene_seq_data['gcContent'] = GC(sequence)
        gene_seq_data['swap_sequence'] = swapSeq(sequence, swapLetters[0], swapLetters[1])

        return gene_seq_data

@app.route('/v1/sequence/<id>/', methods=['GET'])
def seq_data(id):
    content_type = request.args.get('content-type')
    
    formats = ['fasta', 'x-fasta', 'multi-fasta']

    if(content_type in formats):
        return format_output(id, content_type)
    else:
        return 'Format not supported!'

if __name__ == '__main__':
    app.run()
    