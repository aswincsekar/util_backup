import json
import trigger_probe
import argparse


# Testing get_metadata()

parser = argparse.ArgumentParser( description="Extract Metadata from some videos")
parser.add_argument('-s', '--source', help='Enter the path to the video that has to be processed')
parser.add_argument('--version', action='version', version='MetaMorph 1.0')
args = parser.parse_args()

print('File Path : ' + args.source)

output = trigger_probe.get_metadata(args.source)
print(json.dumps(output, indent=4, sort_keys=True))