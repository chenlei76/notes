import os
for md in os.listdir():
	name,type = os.path.splitext(md)
	# print(name,type)
	if type=='.md':
		n = None
		with open(md,'r',encoding="utf-8") as f:
			n = f.read()
		if '[toc]' in n or '[TOC]' in n:
			print(md, '==> Unfinshed')
		else:
			n = "[toc]\n\n" + n
			with open(md, 'w', encoding="utf-8") as f:
				f.write(n)
			print(md, '==> Finished')
# input('>>> ')