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
    :return: metadata_output
    """
    command = [FFPROBE_BIN,
               '-v', 'quiet',
               '-print_format', 'json',
               '-show_format',
               '-show_streams',
               input_file]
    output = sp.check_output(command)
    metadata_output = json.loads(output)
    return metadata_output

