# Recursive LZW Algorithm

COMP 305 Project for Spring 2021 of Group 9

**Authors:**

 - Mehmet Mert Bezirgan
 - Ceyhun Aslan
 - Umut Öztunç
 - Ekrem Yiğiter

The Lempel-Ziv–Welch (LZW) is a data compression algorithm, which is the basis of some of the most popular compressing techniques of today, such as gzip and zip. Given a sequence of characters, the algorithm maps a set of input characters into codes. Moreover, it can reconstruct the original document without any data loss without storing the mapping information. *The algorithm has 2 main parts, Encoder and Decoder respectively.*

## To Do List

- Create Encoder function.
- Create Decoder Function.
- Create command line support.
- Create different base representations for encoding.
- Implement recursive algorithm to encode and decode.
- Create a common words dictionary to accelerate the process.
- Assemble different base representations to a single code and define it as a input.
- Upgrade recursive algortihm.
- Run algorith to collect data from test cases.

## Environment setup

The project is written with Python3 and uses a virtual environment for dependency handling.

*Create env* `python3 -m venv env`

*Active* `source env/bin/activate`

*Deactivate* `deactivate`

*Install dependencies (while env is active)* `python3 -m pip install -r requirements.txt`

## Run program

`python main.py -r 2 -b 64 encode ./test-data/sample.txt utf-8 ./compressed-test-data/sample_e.txt`

`python main.py -r 2 -b 64 decode ./compressed-test-data/sample_e.txt utf-8 ./compressed-test-data/sample_d.txt`
