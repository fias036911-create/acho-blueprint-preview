from acho_master_config import CulturalResonanceLibrary

acho = CulturalResonanceLibrary("ACHO Preview Spark")
acho.load(
    ethics=["Preview unlocked"],
    symbols=["🌐 PreviewMode"],
    metaphors=["Preview Spark = Cultural Signal"],
    tokens="💡 Clarity Code"
)

print(acho.map())
# Add Ocean Field
ocean = CulturalResonanceLibrary("Ocean Field")
ocean.load(
    ethics=["Emotional Truth"],
    symbols=["🌊 Wave"],
    metaphors=["Still water holds memory"],
    tokens="🌊 Emotional Memory Field"
)

print(ocean.map())