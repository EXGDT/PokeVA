from celery import shared_task
from . import models
import invresult.models
import subprocess
import os

protein_list = ['A0A140JWM8', 'A0A178U7J2']
plant = 'soybean'
smile = ''

@shared_task
def run_vina_docking(plant, smile, protein_list, email_address):
    data_dir = '/home/yxguo/html/PokeVA/data/'
    pocket_conf = '/home/yxguo/html/PokeVA/data/Alpha_Pocket/01.AF2_Pocket/v4/{}_v4_pocket.list'.format(plant)
    pocket_dir = '/home/yxguo/html/PokeVA/data/Alpha_Pocket/01.AF2_Pocket/v4/{}'.format(plant)
    receptor_dir = '/home/yxguo/html/PokeVA/data/Alpha_Pocket/02.AF2_PDBQT/v4/{}'.format(plant)
    ligand_dir = '/home/yxguo/html/PokeVA/data/Alpha_Pocket/03.PhytoHormone_PDBQT/{}'.format(smile)
    out_dir = '/home/yxguo/html/PokeVA/data/Alpha_Pocket/09.Vina_Docking_Output/v4/{}/{}'.format(plant, smile)

    protein_list = protein_list.split('\n').strip()

    pocket_list = [item for item in pocket_conf if any(protein in item for protein in protein_list)]

    os.makedirs(out_dir, exist_ok=True)

    with open(pocket_conf, 'r') as file:
        for line in file:
            line = line.strip()
            command = [
                "vina",
                "--cpu", '8',
                "--exhaustiveness", '8',
                "--config", os.path.join(work_dir, pocket_dir, line),
                "--receptor", os.path.join(work_dir, receptor_dir, f"{line.split('_pocket')[0]}.pdbqt"),
                "--ligand", os.path.join(work_dir, ligand_dir, ligand),
                "--out", os.path.join(work_dir, out_dir, f"{line[:-5]}_{ligand[:-6]}_out.pdbqt")
            ]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{line[:-5]} finished successfully :-)")
            else:
                print(f"Error in processing {line[:-5]}: {result.stderr}")
