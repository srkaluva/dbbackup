from argparse import Action, ArgumentParser

class DriveAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.destination = destination
        namespace.driver = driver.lower()



def create_parser():
  parser = ArgumentParser(description="backup postgres DB")
  parser.add_argument("url", help="URL of Database to backup")
  parser.add_argument("--driver", "-d", help="how and where to store backup", nargs=2, metavar=("DRIVER", "DESTINATION"), action=DriveAction, required=True)

  return parser

def main():
    import time
    import sys
    import boto3
    from dbbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3' :
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print(f"Backing database up to {args.destination} in s3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, 'example.sql')
    elif args.driver == 'local':
        outfile = open(args.destination, 'wb')
        print(f"Backing database up locally to {outfile.name}")
        storage.local(dump.stdout, outfile)
    else:
        print("invalid args")
        sys.exit(1)

  
