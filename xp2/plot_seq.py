from PIL import Image, ImageColor, ImageDraw
from Bio.SeqIO.FastaIO import FastaIterator
import os
import argparse 

def draw_sequence(seq: str):
    size = len(seq)

    if size > 1000:
        return None

    pos  = [size,size]
    vec  = (1,1)
    col  = ImageColor.getrgb("black")
    im = Image.new("RGB", (size*2, size*2), (255,255,255))


    for base in seq.upper(): 
        if base == 'A':
            vec = (1,0)
            col = ImageColor.getrgb("green")
        if base == 'C':
            vec = (-1,0)
            col = ImageColor.getrgb("blue")
        if base == 'T':
            vec = (0,-1)
            col = ImageColor.getrgb("red")
        if base == 'G':
            vec = (0,1)
            col = ImageColor.getrgb("black")

        pos[0] = pos[0] + vec[0]
        pos[1] = pos[1] + vec[1]
    
        im.putpixel(pos, col)
    return im 


def save_image_from_fasta(filename, output="output"):

    os.makedirs(output)
    with open(filename) as handle:
        for record in FastaIterator(handle):
            img = draw_sequence(record.seq)
            print(record.id+" processed")
            if img is not None:
                img.save(os.path.join(output,record.id+".png"))
                del(img)
            



save_image_from_fasta("mir_refseq_slop50.fasta")