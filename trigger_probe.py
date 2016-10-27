"""
Methods to extract video metadata by using ffprobe
<ffprobe : this little cute program is the most amazing thing I have watched in my life after this gif
 https://i.imgur.com/9AsqsFj.gifv >
"""
import subprocess as sp
import json
import argparse

FFPROBE_BIN = "ffprobe"

def get_metadata(input_file):
    """

    :param input_file:
    :return:
    """
    command = [FFPROBE_BIN,
               '-v', 'quiet',
               '-print_format', 'json',
               '-show_format',
               '-show_streams',
               input_file]
    output = sp.check_output(command)
    output = json.loads(output)
    return output

# Testing get_metadata()

parser = argparse.ArgumentParser( description="Extract Metadata from some videos")
parser.add_argument('-s', '--source', help='Enter the path to the video that has to be processed')
parser.add_argument('--version', action='version', version='MetaMorph 1.0')
args = parser.parse_args()

print('File Path : ' + args.source)

output = get_metadata(args.source)
print(json.dumps(output, indent=4, sort_keys=True))
