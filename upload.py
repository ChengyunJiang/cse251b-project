from huggingface_hub import upload_folder
from pathlib import Path

upload_folder(
    folder_path=str(Path("~/private/cse251b-project/submission-best").expanduser()),
    repo_id="chj014/cse251b-group-maggie",
    repo_type="model"
)
