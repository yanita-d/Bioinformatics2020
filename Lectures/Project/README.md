# Project
Да се разработи RESTFul приложение на Python (по желание може и друг език), което да оперира върху данни от [ensambl](https://www.ensembl.org/index.html):

- /v1/sequence/gene/id/<id>
> Да приема id на gene и да връща като резултат цялата секвенция на гена и всички екзони като отделни свойства.

Примерен отговор:

```json
{
    "seq":"GTAGTTGATCTCCGGAGTTTCGCCATGCGGAACTTGGGGGCTTTCGCGGCCCGCGTCGGTGCGGAGTAGCTGCTTT",
    "exons":[
        {"start":38327340,"end":38327509,"id":"ENSE00003819676","seq":"TCCGGAGTTTC"},
        {"start":38727340,"end":38327509,"id":"ENSE00003819676","seq":"GGTGCGGAGTAGC"},
        {"start":38318829,"end":38318987,"id":"ENSE00001025712","seq":"GAACTTGGGGGCTTTCGCGGCCCGCGTCGGTGC"}
    ]
}
```

- /v1/sequence/gene/id/<id>?gc_content=true&swap=A:T
> Да приема id на gene и да връща като резултат секвенцията с пресметнато процентното GC съдържание и разменени аминокиселини аденин с тимин в конкретния пример

```json
{
    "seq":"GTAGTTGATCTCCGGAGTTTCGCCATGCGGAACTTGGGGGCTTTCGCGGCCCGCGTCGGTGCGGAGTAGCTGCTTT",
    "gc_content":45,
    "swap_sequence":"GTAGTTGATCTCCGGAGTTTCGCCATGCGGAACTTGGGGGCTTTCGCGGCCCGCGTCGGTGCGGAGTAGCTGCTTT"
}
```

- /v1/sequence/id/<id>?content-type=fasta
> Да пиема ID и да връща секвенция в специфичен формат. Поддържаните формати трябва да са: fasta, multi-fasta, x-fasta

x-fasta format
```json 
{
    "id":">ENSE00001025715.1 chromosome:GRCh38:X:38317316:38317465:-1",
    "seq":"AGGATGGAAGACTTTTTATGTGGGGTGACAATTCCGAAGGGCAAATTGGTTTAAAAAATG"
}
```

Помощни материали:
- [ensambl rest api documentation](https://rest.ensembl.org/)
- [rest api sequence](https://rest.ensembl.org/documentation/info/sequence_id) - request example 
```http
https://rest.ensembl.org/sequence/id/ENSE00001025715?content-type=text/plain
```
- [lookup documentation](https://rest.ensembl.org/documentation/info/lookup) information about exons- request example

```http
https://rest.ensembl.org/lookup/id/ENST00000645032?content-type=application/json;expand=1
```
