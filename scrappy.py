import urllib2
import os, sys, time, json

pos = os.getcwd()
count = 0
cd = ""
clientID = "2e7fa5b951e0a44"
## clientSecret = "e657a81a61f6fcc792a7f0585d2949fe1b67e786"

		
  
def makeFolder(sub):
  global cd
  cd = sub
  if not (os.path.exists(pos + "/" + cd)):
    os.mkdir(pos+"/"+cd, 0777)


#Just saves the image		
def saveSingleImage(d):
  global count
  imageData = urllib2.urlopen(d).read()
  dotLocation = d.rfind(".")
  ending = d[dotLocation:dotLocation+4]
  imageFileName = pos + "/" + cd + "/Image{:04d}{}".format(count, ending)
  putDataInFile(imageFileName, imageData)
  count = count + 1

    
def putDataInFile(f, d):
  with open(f, "w") as fl:
    fl.write(d)
    

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def lookAtAlbum(s):
  global clientID
  global count
  
  
  if "/" in s[-1]:
    s = s[:-1]
    print("Removing the trailing /")
  
  if "/" in s:
    p = s.split("/")
    s = p[len(p)-1]
    print(s)
  
  
  path = "{}/{}".format(os.getcwd(), s)
  if os.path.isdir(path):
    print("Already scrapped this album")
    return
  
  req = urllib2.Request("https://api.imgur.com/3/album/{}/images.json".format(s))
  req.add_header('Authorization', 'Client-ID ' + clientID)
  
  resp = urllib2.urlopen(req).read()
  pjson = json.loads(resp)
  pjson = json.dumps(pjson)
  
  
  data = json.loads(pjson)["data"]
  
  print(len(data))
  if len(data) == 0:
    return
  
  makeFolder(s)
  for i in range(0, len(data)):
    link = data[i]["link"]
    saveSingleImage(link)    
    if(not (len(data) == 1)):
      perc = percentage(i, len(data)-1)
      print("{}/{} {:.1f}%".format(i,len(data)-1, perc))
    else:
      print("Saved single image")
  
  
if __name__ == "__main__":
    lookAtAlbum(sys.argv[1])
