import re
import time
from io import StringIO
import requests
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdf2image import convert_from_path
import pytesseract
from pytesseract import image_to_string
import os.path
import phonenumbers
from phonenumbers import timezone
from datetime import datetime
import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor
import pypostalwin

