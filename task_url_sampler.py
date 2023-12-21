import glob
import random
import json

TASK_CONFIGS = {
    "Medical Challenge Calls" : {
        "task_dir": "./task_configs/medical_challenge_calls_12_17/"
    },
    # "Lab Engine Calls" : {
    #     "task_dir": "./task_configs/lab_engine_calls_12_11/"
    # }
    "Kickout Calls 12/21" : {
        "task_dir": "./task_configs/kickouts_12_19/"
    },
    # # "RAG Mentoring Calls" : {
    # #     "task_dir": "./task_configs/rag_mentoring_calls_12_13/"
    # # },
    # "RN Targeted Eval" : {
    #     "task_dir": "./task_configs/RN_targeted_eval_12_19/"
    # },
    # "Medication Engine Calls" : {
    #     "task_dir": "./task_configs/medication_engine_calls/"
    # },
    # "ASR Test Calls": {
    #     "task_dir": "./task_configs/ASR_calls_12_18/"
    # }
    "Mentoring Calls": {
        "task_dir": "./task_configs/mentoring_calls_12_20/"
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

