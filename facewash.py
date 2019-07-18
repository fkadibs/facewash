#! /bin/python3
import os
import sys
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--directory', metavar='', help='directory to search and clean')
group.add_argument('-f', '--file', metavar='', help='file to clean')
parser.add_argument('-r', '--recursive', action='store_true', help='recursively search directory')
parser.add_argument('-o', '--overwrite', action='store_true', help='replace original files')
args = parser.parse_args()


def open_file(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    return content

def clean_blob(blob):
    jpg = b'\xFF\xD8\xFF\xE2\x00\x00\x4A\x46\x49\x46\x00\x01\x02\x00\x00\x01\x00\x01\x00\x00\xFF\xED\x00\x9C'
    jpg += b'\x00' * 164
    jpg += blob[153::]
    return jpg

def save_file(root, filename, blob, overwrite):
    if overwrite:
        output_file = filename
    else:
        output_file = 'clean_' + filename
    target_output = os.path.join(root, output_file)
    print('[+] Saving clean copy: {}'.format(output_file))
    with open(target_output, 'wb') as c:
        c.write(blob)

def parse_file(root, filename):
    target_file = os.path.join(root, filename)
    blob = open_file(target_file)
    if b'\x28\x00\x62\x46\x42\x4D\x44\x30\x31\x30\x30\x30' in blob:
        print('[+] Found metadata: {}'.format(filename))
        clean = clean_blob(blob)
        save_file(root, filename, clean, args.overwrite)

def parse_folder(directory):
    abs_dir = os.path.abspath(directory)
    if args.recursive:
        for root, subdirs, files in os.walk(abs_dir):
            for filename in files:
                if filename.endswith('.jpg'):
                    parse_file(root, filename)
    else:
        for filename in os.listdir(abs_dir):
            if not os.path.isdir(filename):
                if filename.endswith('.jpg'):
                    parse_file(abs_dir, filename)

if args.directory:
    parse_folder(args.directory)
    
elif args.file:
    parse_file(os.path.dirname(args.file), os.path.basename(args.file))
