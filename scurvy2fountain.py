	iscaps = tline.startswith('!')
	if iscaps:
		print('Forcing uppercase...')
		tline = tline[1:].upper()
	scraps = ['int.', 'INT.', 'ext.', 'EXT.']
	for cap in scraps:
		craps = tline.startswith(cap)
		if craps:
			print('Forcing uppercase...')
			tline = tline.upper()
