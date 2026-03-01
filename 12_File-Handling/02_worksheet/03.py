'''
Log Parser to Dictionary
Develop a function that reads each line of the log file and parses it into a dictionary with
keys: timestamp, log_level, module (if available), and message. Return a list of
such dictionaries.
Challenge: Handle lines that deviate from the standard format by either skipping them or
recording an error message.

'''


def parse_log(filename):
    result=[]
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            parts=line.split()

            if len(parts)<4:
                continue   # skip invalid line

            timestamp=parts[0]+" "+parts[1]
            log_level=parts[2]

            if len(parts)>=5:
                module=parts[3]
                message=" ".join(parts[4:])
            else:
                module=None
                message=" ".join(parts[3:])

            log_dict={
                "timestamp":timestamp,
                "log_level":log_level,
                "module":module,
                "message":message
            }

            result.append(log_dict)

    return result