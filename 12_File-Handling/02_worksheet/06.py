'''
JSON Log Converter
Write a script that converts the log file into a JSON file. Each log entry should be a JSON
object containing the keys: timestamp, log_level, module, and message.
Challenge: Ensure that the JSON output correctly represents all valid log entries while
ignoring or flagging misformatted lines.

'''


import json

def parse_log_file(input_file):
    logs=[]
    errors=[]

    with open(input_file,"r") as f:
        for line_no,line in enumerate(f,1):
            line=line.strip()
            parts=line.split()

            if len(parts)<4:
                errors.append(f"Line {line_no}: Invalid format")
                continue

            timestamp=parts[0]+" "+parts[1]
            log_level=parts[2]

            if len(parts)>=5:
                module=parts[3]
                message=" ".join(parts[4:])
            else:
                module=None
                message=" ".join(parts[3:])

            log_entry={
                "timestamp":timestamp,
                "log_level":log_level,
                "module":module,
                "message":message
            }

            logs.append(log_entry)

    return logs,errors


def convert_to_json(input_file,output_file):
    logs,errors=parse_log_file(input_file)

    with open(output_file,"w") as f:
        json.dump(logs,f,indent=4)

    print("JSON file created:",output_file)

    if errors:
        print("Some lines were skipped:")
        for e in errors:
            print(e)


if __name__=="__main__":
    convert_to_json("log.txt","output.json")