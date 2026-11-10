"""
EmotionDetection package — exposes the emotion_detector application module.
"""

import os
import sys

_PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_PACKAGE_DIR)
if _PROJECT_DIR not in sys.path:
    sys.path.insert(0, _PROJECT_DIR)

_module_file = os.path.join(_PACKAGE_DIR, "emotion_detection.py")
if os.path.isfile(_module_file):
    from .emotion_detection import emotion_detector
else:
    from emotion_detection import emotion_detector

__all__ = ['emotion_detector']
