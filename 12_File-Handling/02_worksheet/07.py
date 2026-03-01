'''
Command-Line Log Filter
Develop a command-line tool using Python’s argparse module that accepts two
arguments: a log level (e.g., “ERROR”) and a module name. The script should filter the log
file to print only those entries matching both criteria.
Challenge: Validate the command-line inputs and provide helpful error messages for invalid
or missing arguments.

'''
import argparse

def parse_log_file(filename):
    logs=[]
    with open(filename,"r") as f:
        for line in f:
            parts=line.strip().split()
            if len(parts)<4:
                continue

            timestamp=parts[0]+" "+parts[1]
            log_level=parts[2]
            module=parts[3]
            message=" ".join(parts[4:])

            logs.append({
                "timestamp":timestamp,
                "log_level":log_level,
                "module":module,
                "message":message
            })
    return logs


def main():
    parser=argparse.ArgumentParser(description="Filter log file by level and module")

    parser.add_argument("logfile",help="Path to log file")
    parser.add_argument("level",help="Log level (INFO,ERROR,WARNING)")
    parser.add_argument("module",help="Module name")

    args=parser.parse_args()

    valid_levels=["INFO","ERROR","WARNING","DEBUG"]

    if args.level not in valid_levels:
        print("Error: Invalid log level.")
        print("Allowed levels:",valid_levels)
        return

    logs=parse_log_file(args.logfile)

    filtered=[log for log in logs
              if log["log_level"]==args.level and log["module"]==args.module]

    if not filtered:
        print("No matching log entries found.")
    else:
        for log in filtered:
            print(log)


if __name__=="__main__":
    main()