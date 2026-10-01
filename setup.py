import os

project_structure={
    "core":[
        "extractor.py",
        "rag_engine.py",
        "summarizer.py",
        "transcriber.py",
        "vector_store.py",

    ],

    "utils":[
        "audio_processor.py",

    ],


}

root_files=[
    "requirements.txt",
    "app.py",
    "main.py",
    "test.py",
]

def create_project_structure():
    for folder, files in project_structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            file_path=os.path.join(folder, file)

            if not os.path.exists(file_path):
                open(file_path,"w").close()

    for files in root_files:
        if not os.path.exists(files):
            open(files,"w").close()

    print("Project Structured Created Successfully")

if __name__ == "__main__":
    create_project_structure()

