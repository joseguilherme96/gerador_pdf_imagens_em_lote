import argparse
import os
from src.Flags import flags

parser = argparse.ArgumentParser()

for flag in flags:

    parser.add_argument(flag["flag_name"],f'-{flag["flag_name"]}',help=f"{flag["help"]}")

args = parser.parse_args()

flags[0]['value'] = args.qtd_imagens_por_folha
flags[1]['value'] = args.ajuste_width
flags[2]['value'] = args.ajuste_height
