import argparse
from micro_scope import output, visuals, decision

# take input
# microanalyse --input market.jsonl --outdir ./reports --visuals --summary

# take the input, parse it as necessary
# feed input into analyser, then feed it into output
# add output to folder as json
# send signal to visuals to display these on screen if commanded

def main():
    parser = argparse.ArgumentParser(prog="MicroScope: Market Microstructure Tool", usage=)
    parser.add_argument("--input", type=str, required=True, help="Path to input directory")
    parser.add_argument("--outdir", type=str, required=True, help="Output directory")
    parser.add_argument("--visuals", action='store_true', help="Generate visuals")
    parser.add_argument("--summary", action='store_true', help="Generate summary decision")

    args = parser.parse_args()
    data = input.load_data(args.input)

    if args.visuals:
    
    if args.summary:

if __name__ == "__main__":
    main()