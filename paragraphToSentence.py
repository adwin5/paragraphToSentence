import nltk.data
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

input_file_name = "input.txt"
output_file_name = "output.txt"

with open(input_file_name, 'r') as myfile:
    data=myfile.read().decode("utf-8").replace('\n', '')
# print '\n---\n'.join(sent_detector.tokenize(data.strip()))

output_file = open(output_file_name, 'w')
for item in sent_detector.tokenize(data.strip()):
  output_file.write("%s\n" % item.encode('utf-8'))
