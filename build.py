
import os
import sys
use_no_cache = " --no-cache" if "no" in sys.argv else ""
os.system("docker rm 803_database 803_web_api 803_web_front")
os.system("docker build"+ use_no_cache + " -t 803_database --file 803_database.dockerfile .")
os.system("docker build"+ use_no_cache + " -t 803_web_api --file 803_web_api.dockerfile .")
os.system("docker build"+ use_no_cache + " -t 803_web_front --file 803_web_front.dockerfile .")
os.system("docker compose up --force-recreate")

