from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Configurações para acesso ao Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

spreadsheet_id = '1PPe020gSd4bmvelXLl68rKUjo9eDSser2g4_-aDIYbo'
sheet_name = 'Produtividade'

@app.route('/')
def index():
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    data = sheet.get_all_records()
    return render_template('index.html', data=data)

@app.route('/update', methods=['POST'])
def update():
    count = request.form.get('count')
    # Logica para salvar o count no Google Sheets
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
