import re
import codecs
import os

global numberOfLines
global numberOfLabels

def isLabelLine(line):
	patternIsLabel = re.compile("[\"]\w*[\"]\s*[=]\s*[\"].*[\"][;]", re.UNICODE)
	isLabelLine = patternIsLabel.match(line)
	return bool(isLabelLine)

def turnLineIntoXML(line):
	parts =  line.split('" = "')
	key = parts[0][1:len(parts[0])]
	value = parts[1].split('\";\n')[0]
	xmlLine = '\t<string name="'+key+'"'+'>'+value+'</string>\n'
	return xmlLine

def convertForLanguage(lang):
	f = codecs.open('./'+lang+'.lproj/Localizable.strings', encoding='utf-8')
	convertedFile = ""
	for line in f:
		encLine = line
		global numberOfLines
		numberOfLines += 1
		if encLine[0] == '"':
			pass
			if isLabelLine(encLine):
				global numberOfLabels
				numberOfLabels += 1
				convertedFile = convertedFile + turnLineIntoXML(encLine)
			else:
				print "Error: ", encLine
	return convertedFile


def getConvertedXMLContentForLanguage(lang):
	global numberOfLabels
	numberOfLabels = 0
	global numberOfLines
	numberOfLines = 0
	content = "<resources>\n"
	content = content+convertForLanguage(lang)
	content = content + "</resources>"
	return content


def printXMLForLanguages(langs):
	for lang in langs:
		print "\n\n\n"+ lang.upper() + "\n\n\n"
		print getConvertedXMLContentForLanguage(lang)
		print "\n"+"Labels:"+str(numberOfLabels)+"\n"+"Lines: "+str(numberOfLines)+"\n\n\n"

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def generateXMLFilesForLanguages(langs):
	for lang in langs:
		filename = "./android_xml/values-"+lang+"/strings.txt"
		ensure_dir(filename)
		if os.path.isfile(filename):
			os.remove(filename)

		f = codecs.open(filename,'a+',encoding='utf-8')
		f.write(getConvertedXMLContentForLanguage(lang))
		f.close()

# Add your languages here

langs = ['de', 'en']

# printXMLForLanguages(langs)
generateXMLFilesForLanguages(langs)