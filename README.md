# Recursive LZW Algorithm

COMP 305 Project for Spring 2021 of Group 7

**Authors:**

 - Mehmet Mert Bezirgan
 - Ceyhun Aslan
 - Umut Öztunç
 - Ekrem Yiğiter

The Lempel-Ziv–Welch (LZW) is a data compression algorithm, which is the basis of some of the most popular compressing techniques of today, such as gzip and zip. Given a sequence of characters, the algorithm maps a set of input characters into codes. Moreover, it can reconstruct the original document without any data loss without storing the mapping information. *The algorithm has 2 main parts, Encoder and Decoder respectively.*

## Environment setup

The project is written with Python3 and uses a virtual environment for dependency handling.

*Create env* `python3 -m venv env`
*Active* `source env/bin/activate`
*Deactivate* `deactivate`
*Install dependencies (while env is active)* `python3 -m pip install -r requirements.txt`

