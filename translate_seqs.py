'''
Author: Mudra Hegde
Email: mhegde@broadinstitute.org
'''

import pandas as pd
import csv, argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', type=str, help='Input file with sequences to translate in the first column')
    parser.add_argument('--frame', type=int, help='Reading frame of sequence (1,2 or 3)')
    parser.add_argument('--codon-file', type=str, default='Codon_map.txt', help='File with codon map')
    parser.add_argument('--outputfile', type=str, help='Outputfile with translations')
    return parser

def read_arguments(args):
    input_df = pd.read_table(args.inputfile)
    frame = args.frame
    codon_map = read_codon_map(args.codon_file)
    outputfile = args.outputfile
    return input_df, frame, codon_map, outputfile


def read_codon_map(file):
    codon_map_df = pd.read_table(file)
    codon_map = {}
    for i,r in codon_map_df.iterrows():
        codon_map[r[0]] = r[1]
    return codon_map


def translate(input_df, frame, codon_map, w):
    for i, r in input_df.iterrows():
        seq = r[0]
        aa = ''
        j = frame - 1
        while j < len(seq):
            substring = seq[j:(j + 3)]
            if len(substring) == 3:
                aa = aa + codon_map[substring]
                j += 3
            else:
                break
        row = list(r)
        row.append(aa)
        w.writerow((row)
    return


if __name__ == '__main__':
    args = get_parser().parse_args()
    input_df, frame, codon_map, outputfile = read_arguments(args)
    colnames = list(input_df.columns)
    colnames.append('Translated Sequence')
    with open(outputfile,'w') as o:
        w = csv.writer(o,delimiter='\t')
        w.writerow((colnames))
        translate(input_df, frame, codon_map, w)




