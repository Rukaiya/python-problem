import re
filename = '/home/rukaiya/Developments/MisfitTech/shopoth_staging_wv.odt'

textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("", filetext)