import util
import subprocess 

websites_arg = " ".join(util.get_random_websites("websites.csv",10))

process = subprocess.Popen(["python", "py/logocrawler/__init__.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stdout, _ = process.communicate(input=websites_arg.encode())
process.stdin.close()

print(stdout.decode())