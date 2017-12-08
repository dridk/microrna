from PIL import Image, ImageColor
import argparse 

def draw_sequence(seq: str):
    size = len(seq)
    pos  = [size,size]
    vec  = (1,1)
    col  = ImageColor.getrgb("black")
    im = Image.new("RGB", (size*2, size*2), (255,255,255))

    for base in seq: 
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


parser = argparse.ArgumentParser(description='Draw sequence according ')
parser.add_argument('sequences',type=str,help='an integer for the accumulator')
parser.add_argument("-o", "--output", action='store', dest='output', help="file output ")

args = parser.parse_args()
image = draw_sequence(args.sequences)
image.save(args.output)

image.show()
