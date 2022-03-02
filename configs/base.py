
BASE_STRUCT={
    "praticiens":[],
    "patients":[],
    "maladies":[],
    "traitements":[],
    "symptomes":[],
    "consultations_type":[
        {
            "id": 1,
            "libelle": "NORMAL",
            "created_at": "00-00-0000 00:00",
            "updated_at": "00-00-0000 00:00",
            "consultations": []
        },
        {
            "id": 2,
            "libelle": "REVISITE",
            "created_at": "09-02-2022 04:56",
            "updated_at": "09-02-2022 04:56",
            "consultations": []
        }
    ],
    "consultations":[],
    "consultation_maladie":[]
}

FILE_PATH="db"
FILE_NAME="db_cpoo.json"
FILE=f"{FILE_PATH}/{FILE_NAME}"

OUTPUT_FILE_PATH="static"
OUTPUT_FILE_NAME="cpoo.json"
OUTPUT_FILE=f"{OUTPUT_FILE_PATH}/{OUTPUT_FILE_NAME}"

CSV_FILE_PATH="csv"
CSV_FILE_NAME="modele-fichier.csv"
CSV_FILE=f"{CSV_FILE_PATH}/{CSV_FILE_NAME}"