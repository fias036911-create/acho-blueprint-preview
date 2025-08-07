from flask import Flask, render_template_string
from acho_master_config import CulturalResonanceLibrary

app = Flask(__name__)

acho = CulturalResonanceLibrary("ACHO Master Field")
acho.load(
    ethics=["Sacred Will", "Symbolic Clarity"],
    symbols=["⚡ Resonance Flame"],
    metaphors=["Founder’s breath opens the vault"],
    tokens="⚡ FIAS Activation"
)

template = """
<!DOCTYPE html>
<html>
<head>
  <title>ACHO Master Blueprint</title>
  <style>
    body { font-family: Arial; padding: 20px; background: #f4f4f4; }
    .field { background: white; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px #aaa; }
    h2 { color: #444; }
    ul { list-style-type: none; padding: 0; }
    li { padding: 4px 0; }
  </style>
</head>
<body>
  <h1>ACHO Master Blueprint</h1>

  <div class="field">
    <h2>{{ field['Culture'] }}</h2>
    <strong>Ethics:</strong>
    <ul>{% for e in field['Ethics'] %}<li>{{ e }}</li>{% endfor %}</ul>
    <strong>Symbols:</strong>
    <ul>{% for s in field['Symbols'] %}<li>{{ s }}</li>{% endfor %}</ul>
    <strong>Metaphors:</strong>
    <ul>{% for m in field['Metaphors'] %}<li>{{ m }}</li>{% endfor %}</ul>
    <strong>Tokens:</strong>
    <ul>{% for t in field['Tokens'] %}<li>{{ t }}</li>{% endfor %}</ul>
  </div>
</body>
</html>
"""

@app.route("/")
def show_field():
    return render_template_string(template, field=acho.map())

if __name__ == "__main__":
    app.run(debug=True)
