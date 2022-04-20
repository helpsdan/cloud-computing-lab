from filesDAO import FilesDAO
import json
import urllib.parse


files = FilesDAO('files-dev')

def handler(event, context):
    print("Parsing bucket key and event name...")
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    eventName = event['Records'][0]['eventName']
    filename = extractFileNameFromKey(key)
    
    print("Perform event...")
    performFileEvent(eventName, filename)
    
    
def extractFileNameFromKey(key):
    print("Extracting filename from bucket key...")
    return key[14:len(key)-5]
    

def isCreationEvent(eventName):
    print("Validating creation event...")
    return "ObjectCreated:Put" == eventName


def performFileEvent(eventName, filename):
    if isCreationEvent(eventName):
        print("Adding new file to s3 bucket...")
        files.put_item({
            'nomearquivo': filename,
            'ativo': True
        })
    else: 
        print("Removing file to s3 bucket...")
        files.put_item({
            'nomearquivo': filename,
            'ativo': False
        })