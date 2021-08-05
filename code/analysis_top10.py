#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import time
import numpy as np
import re


def create_re_ranking_output(input_file, output_file, eval_type="last", topn=10):
    do_last = False
    do_sum = False
    do_aver = False
    if eval_type == "last":
        do_last = True
    elif eval_type == "sum":
        do_sum = True
    elif eval_type == "average":
        do_aver = True
    else:
        raise ValueError(
        "Only one of `last`, `sum` or `average' must be.")
    line_list = []
    idx = []
    with open(output_file, 'w') as writer, \
         open(input_file, 'r') as reader:
            for line in reader:
                if not line.strip():
                    #idx_list = sorted(range(len(prob_list)), key=lambda x: prob_list[x], reverse=True)
                    idx_list = sorted(range(len(prob_list)), key=lambda x: (prob_list[x][0], prob_list[x][1]), reverse=True)
                    for i, idx in enumerate(idx_list):
                        label = ""
                        tmp = line_list[idx].split("\t")
                        if tmp[0] == "*":
                            label = "*"
                            line_tmp = "\t".join(tmp[2:])
                        else:
                            line_tmp = "\t".join(tmp[1:])

                        writer.write("\t{}\t{}\t{}\t{}\n".format(label, (i+1), line_tmp, prob_list[idx]))

                        if i == (topn-1):
                            break

                    writer.write("\n")

                else:
                    tmp = line.split("\t")
                    if len(tmp) == 2:
                        writer.write(line.strip() + "\n")
                        line_list = []
                        prob_list = []

                    else:
                        prev = float(line.strip().split("\t")[-2])
                        score = float(line.strip().split("\t")[-1])
                        if do_last:
                            prob =  score
                        elif do_sum:
                            prob =  score + prev
                        else: #do_aver
                            prob = (score + prev)/2

                        line_list.append(line.strip())
                        prob_list.append((prob, score))


def analyze_result_of_ranking(input_file, output_file):
    rank = {}
    for i in range(11):
        rank[str(i+1)] = 0

    with open(input_file, 'r') as reader, \
         open(output_file, 'w') as writer:
        writer.write(output_file + "\n")
        for line in reader:
            if not line.strip():
                if not chk:
                    value = rank['11'] + 1
                    rank['11'] = value
                continue

            tmp = line.strip().split("\t")
            if len(tmp) == 2:
                chk = False
            else:
                if not chk:
                    if "\t*" in line:
                        chk = True
                        value = rank[tmp[1]] + 1
                        rank[tmp[1]] = value
                    else:
                        pass
                else:
                    pass

        for i in range(11):
            num = str(i+1)
            writer.write (("Rank {}:\t{}\n").format(num, str(rank[num])))
            print (("Rank {}\t{}").format(num, str(rank[num])))                  


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', default='input.txt', type=str, required=True, help='input_file')
    parser.add_argument('--output_file', default='output.txt', type=str, required=True, help='output_file')
    parser.add_argument('--topn', default=10 , type=int, required=False, help='the number of rankings')
    parser.add_argument('--result_file', default='result.txt', type=str, required=True, help='final_output_file')
    parser.add_argument('--eval_type', default='last', type=str, required=False, help='last/sum/average')
    args = parser.parse_args()
    print('\nargs:\n' + args.__repr__())

    start_time = time.time()
    create_re_ranking_output(args.input_file, args.output_file, args.eval_type, args.topn)
    analyze_result_of_ranking(args.output_file, args.result_file)
    end_time = time.time()

    print ("*******************************")
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print (time.strftime("     %Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print ("     --- {} seconds---".format(end_time-start_time))
    print ("*******************************")



if __name__ == '__main__':
    main()

