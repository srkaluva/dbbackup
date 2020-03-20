from argparse import Action, ArgumentParser

class DriveAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination



def create_parser():
  parser = ArgumentParser(description="backup postgres DB")
  parser.add_argument("url", help="URL of Database to backup")
  parser.add_argument("--driver", help="how and where to store backup", nargs=2, action=DriveAction, required=True)





  return parser

