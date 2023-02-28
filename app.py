from flask import Flask, request, jsonify
from facturx import get_facturx_xml_from_pdf
import xml.etree.ElementTree as ET
from extract_data import extract_data_from_xml
import xmltodict, json

app = Flask(__name__)


@app.route('/')
def home():
    return 'API is running ...'

@app.route('/analyze', methods=["POST"])
def analyze():
    facture = request.files['file'].read()
    filename, xml = get_facturx_xml_from_pdf(facture)

    xml_to_json = xmltodict.parse(xml)

    return json.dumps(xml_to_json)

