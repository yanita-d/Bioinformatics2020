import requests, sys, json
 
server = "https://rest.ensembl.org"
ext = "/family/id/PTHR15573?"

r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
result = r.text
object_result = json.loads(result)


geneStableId = object_result["members"][0]["gene_stable_id"]

r = requests.get(server+str("/lookup/id/")+str(geneStableId), headers={ "Content-Type" : "application/json"})
result = r.text
print(result)


exit(0)

for item in object_result["members"][0:3]:
  seq_result = ens_client.request("sequence/id/"+item["gene_stable_id"])
  print(json.loads(seq_result))

print(r.headers)
print(r)

exit(0)

if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print(repr(decoded))