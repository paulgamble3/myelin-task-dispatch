import base64
import json

def url_from_config(config_dict):
    encoded_config_str = base64.b64encode(json.dumps(config_dict, separators=(",", ":")).encode("utf-8"))  # type: ignore
    encoded_config_str = encoded_config_str.decode("utf-8")  # type: ignore
    return f"https://eval.myelin-healthcare.com:447/appdemo/eval/call?config={encoded_config_str}"



# pull munjal calls
# call ids from
# mentoring calls
# 

config = {
  "model": "gpt4",
  "method": "voip",
  "supportEngines": [
    "dob-verification-engine",
    "identity-verification-engine",
    "speaker-engine",
    "kickout-engine",
    "lab-engine",
    "medication-engine"
  ],
  "template": "neel_v2",
  "asrService": "dg-nova-2-medical",
  "scriptId": "8f0ae499-5b31-4a68-b813-67e314a958c5",
  "nurseId": "ed9ca802-fb12-46d8-8298-dae2d2e7f81c",
  "patientId": "11b3eb84-1191-41f3-979e-fec682769597",
  "kickoutId": "b8b2a8be-47ee-4562-bb93-d07ee97ea546",
  "ttsStreaming": False,
  "llmStreaming": True,
  "uiSettings": {
    "showTasks": True,
    "showDebug": False,
    "showSystemPrompts": False,
    "showVotes": True,
    "showFeedback": True,
    "showUserAudio": True
  },
  "otherSettings": {
    "GOD_MODE_ENABLED": True,
    "USE_LLAMA_SIMPLE_PROMPT_FORMAT": False,
    "TURN_OFF_CONVERSATION_ENGINE": False,
    "USE_DYNAMIC_CHEAT_SHEET": False,
    "USE_SUMMARIZATION": True,
    "USE_SUMMARY_FOLLOW_UP_IN_KICKOUTS": False,
    "RAG_EMBEDDING_INDEX_NAME": "facilities-curated",
    "USE_TOPIC_DETECTION": False,
    "ELEVEN_LABS_STREAMING_LATENCY": 0,
    "ELEVEN_LABS_MODEL_ID": "eleven_monolingual_v1",
    "GOOGLE_ASR_MAX_AGGREGATE": 2,
    "VOICE_FLOOR_RUN_LOCALLY": True,
    "VOICE_FLOOR_RUN_TIMEOUT": 0.02,
    "VOICE_FLOOR_VOLUME": 0,
    "REMOVE_SPEAKER_UTTERANCE_THRU_VERIFICATION": True,
    "SPEAKER_VERIFICATION_THRESHOLD_HIGH": 0.02,
    "SPEAKER_VERIFICATION_THRESHOLD_LOW": 0.01,
    "SPEAKER_VERIFICATION_NUM_FRAMES": 50,
    "ASR_CONFIDENCE_STRATEGY": "words",
    "ASR_CONFIDENCE_THRESHOLD": 0,
    "SINGLE_WORD_ASR_CONFIDENCE_THRESHOLD": 0.6,
    "SINGLE_WORD_ASR_CONFIDENCE_THRESHOLD_WHILE_SPEAKING": 0.75,
    "ENABLE_TTS_CACHE": True,
    "VAD_THRESHOLD": 0.95,
    "VAD_CONTENT_BASED_TIME": 2000,
    "VAD_VERIFICATION_TIME": 250,
    "DUPLICATE_UTTERANCE_DETECTION_THRESHOLD": 0.9,
    "GC_KEEP_IN_LAST_N_TURNS": 7,
    "SUPPRESS_LABMED_DURING_KICKOUTS": False,
    "SUPPRESS_LABS_AFTER_LAB_SECTION": False,
    "IDENTITY_ENGINE_MODEL_NAME": "llama",
    "DOB_ENGINE_MODEL_NAME": "llama-dob-model",
    "KICKOUT_DETECTOR_MODEL_NAME": "kickout-detector",
    "KICKOUT_EVALUATOR_MODEL_NAME": "kickout-evaluator",
    "KICKOUT_FOLLOW_UPS_MODEL_NAME": "kickout-follow-up-evaluator",
    "MEDICAL_DETECTOR_MODEL_NAME": "llama-medication-detector",
    "MEDICAL_DOSAGE_EVALUATOR_MODEL_NAME": "llama-medication-dosage-evaluator",
    "DRUG_ASR_DETECTOR_MODEL_NAME": "llama-drug-asr-detector",
    "NUTRITION_DETECTOR_MODEL_NAME": "llama-nutrition-detector",
    "LAB_DETECTOR_MODEL_NAME": "llama-lab-detector",
    "RAG_DETECTOR_MODEL_NAME": "rag-detector",
    "CHECKLIST_EVALUATOR_MODEL_NAME": "checklist-evaluator",
    "SUMMARY_MODEL_NAME": "summary-model-v2",
    "MENU_ENGINE_DETECTOR_MODEL_NAME": "menu-detector",
    "MENU_ENGINE_EVALUATOR_MODEL_NAME": "G35:llama-base__loracpt-4__align-7.2dpo__pref4",
    "SPEAKER_ENGINE_MODEL_NAME": "llama",
    "CALL_END_ENGINE_MODEL_NAME": "llama",
    "TOPIC_DETECTOR_MODEL_NAME": "topic-detector",
    "MEDICAL_TANGENT_DETECTOR_MODEL_NAME": "medical-tangent-detector",
    "NON_MEDICAL_TANGENT_DETECTOR_MODEL_NAME": "non-medical-tangent-detector",
    "SUGGEST_FROM_OTC_LIST": False
  }
}


url = url_from_config(config)

print(url)