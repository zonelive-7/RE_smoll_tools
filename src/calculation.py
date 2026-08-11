#检查输入

def check_addr_input(base , main,va_start = None,raw_start = None):
	name = ["基址","main 地址","内存起点","硬盘起点"]
	vals = [None] * 4
	for i,v in enumerate((base,main,va_start,raw_start)):#enumurate will produce a tuple
		if v is None :
			continue

		try :
			vals[i] = v if isinstance(v,int) else int(str(v),16)
		except(ValueError,TypeError):
			print(f"[!] Error: {name[i]} Not a valid Hex!!")
			return False,None
	
	base_v , main_v = vals[0], vals[1]

	if vals[0] is not None and vals[1] is not None and main_v < base_v:
		print("[!] 检查你写入的参数")
		return False , None

	return True,vals





#这里是再x64dbg 找到main 的方法
#首先找到main的地址（main），接着找到虚拟基址（Base）然后填上去
#填完利用公式就可以找到RVA（相对虚拟地址）

def addr_count(base , main,va_start = None,raw_start = None):
	ok,vals = check_addr_input(base , main,va_start = None,raw_start = None)
	#ok is the return True / false
	#vals is the returned list
	if not ok:
		return

	base_v,main_v ,va_v , raw_v = vals
	#let the four list has their name
	rva = main - base

	if va_v is not None and raw_v is not None:
		file_offset = rva - va_v + raw_v
		print(f"[*] RVA = {rva:x} || File Offset = {file_offset:x}")
		return rva , file_offset
	else:
		print(f"RVA = 0x{rva:x}")
		return rva







