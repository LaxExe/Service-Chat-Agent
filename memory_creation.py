from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font

import os
import json


# 1. SETUP ()
# String --> AI ---> Packets (Json different categories - ex. services, timings, faqs) ---> Master JSON (Address - name, location, description)

# 2. Normal workflow
# Manager --> Master JSON () ---> Packets --> retrieve that json ---> return 




