import argparse
from micro_scope import analyser, output, visuals, decision

# take input
# microanalyze --input market.jsonl --outdir ./reports --visuals --summary

# take the input, parse it as necessary
# feed input into analyser, then feed it into output
# add output to folder as json
# send signal to visuals to display these on screen if commanded