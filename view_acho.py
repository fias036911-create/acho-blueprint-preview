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

ocean = CulturalResonanceLibrary("Ocean Field")
ocean.load(
    ethics=["Emotional Truth"],
    symbols=["🌊 Wave"],
    metaphors=["Still water holds memory"],
    tokens="🌊 Emotional Memory Field"
)

template = """
<h1>ACHO Master Blueprint</h1>

<h2>ACHO Master Field</h2>
<p><strong>Ethics:</strong> {{ ", ".join(field1['Ethics']) }}</p>
<p><strong>Symbols:</strong> {{ ", ".join(field1['Symbols']) }}</p>
<p><strong>Metaphors:</strong> {{ ", ".join(field1['Metaphors']) }}</p>
<p><strong>Tokens:</strong> {{ ", ".join(field1['Tokens']) }}</p>

<h2>🌊 Ocean Field</h2>
<p><strong>Ethics:</strong> {{ ", ".join(field2['Ethics']) }}</p>
<p><strong>Symbols:</strong> {{ ", ".join(field2['Symbols']) }}</p>
<p><strong>Metaphors:</strong> {{ ", ".join(field2['Metaphors']) }}</p>
<p><strong>Tokens:</strong> {{ ", ".join(field2['Tokens']) }}</p>
"""
@app.route("/")
def show_fields():
    return render_template_string(template, field1=acho.map(), field2=ocean.map())

if __name__ == "__main__":
    app.run(debug=True)

