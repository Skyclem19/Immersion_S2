import logging
import azure.functions as func

def main(myblob: func.InputStream):
    logging.info(f"Fichier détecté : {myblob.name}")

