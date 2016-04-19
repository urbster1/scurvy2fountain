import re, sys, os
filename = sys.argv[1]
if '.' in filename:
	filename = os.path.splitext(filename)
	filename = filename[0]
outfilename = filename + '.fountain'
farray = []
tarray = []
with open(sys.argv[1], encoding="utf8", errors='replace') as infile:
	inscurvy = infile.read()
	print('Reading file...')
	if '\t'in inscurvy:
		print('Replacing tabs...')
		inscurvy = inscurvy.replace('\t', ' ')
	print('Finding aliases...')
	aliases = re.findall(r'(\w+):=(.+)', inscurvy)
	print('Stripping whitespace...')
	for line in inscurvy.split('\n'):
		line = line + '\n'
		line = line.lstrip()
		farray.append(line)
	print('Done with first pass.')
for tline in farray:
	iscomment = tline.startswith('#')
	if iscomment:
		print('Parsing comment...')
		tline = tline.replace('\n', ' ')
		tline = '/* ' + tline[1:] + '*/'
	isalias = re.search(r'\w+:=.+',  tline)
	if isalias:
		print('Deleting alias description...')
		tline = ''
	for src,  target in aliases:
		name = r'.*\{!*' + re.escape(src) + r'\}'
		isname = re.search(name, tline)
		if isname:
			print('Replacing ' + src + '...')
			tline = tline.replace('{' + src + '}', target)
			tline = tline.replace('{!' + src + '}', target.upper())
		char = re.escape(src) + r'\(*.*\)*: '
		isdialog = re.match(char, tline)
		if isdialog:
			print('Parsing dialogue...')
			preparen = re.escape(src) + r'\s*\(.+\): '
			ispreparen = re.match(preparen, tline)
			if ispreparen:
				tline = tline.replace(src + ' (', target.upper() + ' (')
				tline = tline.replace('): ', ') ')
			tline = tline.replace(') ', ')\n')
			tline = tline.replace(src + ': ',  target.upper() + '\n')
	newchar = re.search(r'.+\(*.*\)*: ',  tline)
	if newchar:
		print('Parsing non-alias character dialogue...')
		testline = tline.split(':')
		if '(' in testline[0]:
			paren = testline[0].split('(')
			tline = paren[0].upper() + '(' + paren[1] + testline[1]
		else:
			testlinea = testline[1]
			tline = testline[0].upper() + '\n' + testlinea[1:]
		if ') ' in tline:
			tline = tline.replace(') ', ')\n')
	if '||' in tline:
		print('Parsing newline...')
		tline = tline.replace('||', '\n')
	issection = tline.startswith('|#')
	if issection:
		print('Parsing section...')
		tline = tline.replace('|#','#')
	tran = ['in:', 'out:', 'dissolve:', 'to:', 'IN:', 'OUT:', 'TO:', 'DISSOLVE:', 'INT.', 'EXT.'] 
	for t in tran:
		if t in tline:
			print('Forcing scene transition...')
			tline = '> ' + tline.upper()
	cont = ["(cont)", "(cont'd)", "(contd)", "(CONTD)", "(cont.)", "(CONT.)", "(CONT)"]
	for c in cont:
		if c in tline:
			print("Parsing (CONT'D)...")
			tline = tline.replace(c,  "(CONT'D)")
	iscaps = tline.startswith('!')
	if iscaps:
		print('Forcing uppercase...')
		tline = tline[1:].upper()
	if '\n\n' in tline:
		print('Eliminating double newline...')
		tline = tline.replace('\n\n', '\n')
	if tline is ' ':
		tline = ''
	if tline.strip():
		tline = tline + '\n'
	tarray.append(tline)
lastline = tarray.pop()
lastline = lastline.rstrip('\n')
tarray.append(lastline)
with open(outfilename,  'w') as outfile:
	outfile.writelines(tarray)
print('Complete!')
