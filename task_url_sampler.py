import glob
import random
import json

TASK_CONFIGS = {
    # "Retrieval - Hospital Policy Questions": {
    #     "task_dir": "./task_configs/1_21_rag/"
    # },
    # "Kickout End-to-End" : {
    #     "task_dir": "./task_configs/1_18_kickout_calls/"
    # },
    # "Nutrition & Retrieval Data Generation - 1/30" : {
    #     #"task_dir": "./task_configs/1_24_all_engine/"
    #     "task_dir": "./task_configs/1_30_menu_retrieval/"
    # }
    # "Nutrition & Retrieval Data Generation - 1/30" : {
    #     #"task_dir": "./task_configs/1_24_all_engine/"
    #     "task_dir": "./task_configs/1_27_mentoring_rewrites/"
    # }
    # "Skill Eval Calls - 2/1": {
    #     "task_dir": "./task_configs/2_1_skill_eval/"
    # },
    # "HRA and Colonoscopy Mentoring - 2/2" : {
    #     "task_dir": "./task_configs/2_2_hra_colonoscopy/"
    # },
    # "Kickout Calls - 2/4" : {
    #     "task_dir": "./task_configs/2_4_kickout_calls/"
    # },
    # "Mentoring Calls - 2/4" : {
    #     "task_dir": "./task_configs/2_4_mentoring/"
    # },
    # "Menu Mentoring - 2/7" : {
    #     "task_dir": "./task_configs/2_7_menu_mentoring/"
    # },
    "Kickout Calls - 2/8" : {
        "task_dir": "./task_configs/2_8_kickout_calls/"
    },
    }


def sample_call_url(call_config_dir):
    call_configs = glob.glob(call_config_dir)
    call_config_fn = random.choice(call_configs)
    with open(call_config_fn) as f:
        call_config = json.load(f)
    call_cfg = random.choice(call_config)
    call_url = call_cfg["url"]
    #call_type = call_config_fn.split("/")[-1][5:-5]
    #call_type = call_type.replace("_", " ")
    return call_url



def sample_task_url(task_name):
    """Sample a URL from the task config."""
    task_config = TASK_CONFIGS[task_name]
    task_dir = task_config["task_dir"]
    call_url = sample_call_url(task_dir + "*.json")
    
    return call_url

