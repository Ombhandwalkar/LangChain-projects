import onnxruntime

try:
    print("onnxruntime loaded successfully:", onnxruntime.__version__)
except ImportError as e:
    print("Error loading onnxruntime:", e)