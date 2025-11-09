import os


#############################
# Functions
#############################
def is_feature_enabled(feature: str) -> bool:
    '''Check if a feature is enabled based on environment variable.'''
    return os.environ.get(feature, "false").lower() in ["true", "1"]
