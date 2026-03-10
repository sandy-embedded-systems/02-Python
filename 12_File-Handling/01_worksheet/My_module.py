import os,re
def process_log_entries(log_file):
    if os.path.exists(log_file):
        with open(log_file,"r") as log:
           sample_log=open("sample.log",'w')
           for line in log:
                if line.count('ERROR')!=-1:
                    time=re.search(r"\d{2}:\d{2}:\d{2}",line)
                    msg=re.search(r"ERROR -\s*(.*)",line)
                    sample_log.write(msg.group())
                    sample_log.write(f"     Time instant:{time.group()}"+'\n')
                else:
                    print("No such File exist")