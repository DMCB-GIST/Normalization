#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import tensorflow as tf
import os
import re
from nltk.tokenize import sent_tokenize
import argparse
import time


def split_sentence_for_train(input_file, sent_file, mention_file):
    #input_file = "NCBI/NCBItrainset_corpus.txt"
    #sent_file = "NCBI"/NCBI_sentences.txt"

    with open(input_file, 'r') as reader, \
         open(sent_file, 'a') as s_writer, \
         open(mention_file, 'w') as m_writer:
        for line in reader:
        	if not line.strip():
        		continue

            if any(a in line for a in ('|t|', '|a|')):
                text = line.strip().split('|')[-1]
                splitsentences = sent_tokenize(text)

                for sentence in splitsentences:
                    s_writer.write(de_hypenation(sentence) + '\n')

                if '|a|' in line:
                	s_writer.write('\n')
            else:
            	tmp = line.strip().split('\t')
            	del tmp[4]
            	m_writer.write("\t".join(tmp) + "\n")



def de_hypenation (input_string):
    result = []
    tokens = input_string.split(" ")
    for token in tokens:
        char_list = list(token)
        tmp = "";

        for c in char_list:
            if re.match("[a-zA-Z0-9]+", c):
                tmp += c
            else:
                tmp += " "

        tmp = re.sub(r"\s+", " ", tmp)
        result.append(tmp.strip())
    
    return " ".join(result)



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', default='NCBI_Disease/NCBItrainset_corpus.txt', type=str, required=True, help='input_file')
    parser.add_argument('--ment_file', default='NCBI_Disease/NCBItrain_mentions.txt', type=str, required=True, help='output_file')
    parser.add_argument('--sent_file', default='NCBI_Disease/NCBI_sentences.txt', type=str, required=True, help='output_file')
    args = parser.parse_args()
    print('\nargs:\n' + args.__repr__())

    start_time = time.time()
    split_sentence_for_train(args.input_file.strip(), args.sent_file.strip(), args.ment_file.strip())
    end_time = time.time()

    print ("*******************************")
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print ("     --- {} seconds---".format(end_time-start_time))
    print ("*******************************")



if __name__ == '__main__':
    main()
