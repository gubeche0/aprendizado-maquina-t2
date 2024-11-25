import kagglehub
import shutil
from datasets import load_dataset


# Download latest version
path = kagglehub.dataset_download("aadyasingh55/sexism-detection-in-english-texts")

print("Path to dataset files:", path)

# Move to content folder
shutil.move(path, "./sexism")



