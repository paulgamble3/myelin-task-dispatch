import glob
import random
import json

TASK_CONFIGS = {
    # "Medical Challenge Calls 12/26" : {
    #     "task_dir": "./task_configs/medical_challenge_calls_12_26/"
    # },
    # "Kickout Calls 12/26" : {
    #     "task_dir": "./task_configs/kickouts_12_26/"
    # },
    # "Mentoring Calls 12/26": {
    #     "task_dir": "./task_configs/mentoring_calls_12_26/"
    # }
    # "Lab Calls": {
    #     "task_dir": "./task_configs/lab_eval_1_1/"
    # },
    "Side Health": {
        "task_dir": "./task_configs/side_health_mentoring_1_4/"
    },
    "Kickout Calls": {
        "task_dir": "./task_configs/kickout_calls_1_5/"
    },
    }

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

