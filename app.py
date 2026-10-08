"""
AI-Oríkì Flask API — Render deployment
"""
import json
import os
import numpy as np
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from fuzzywuzzy import fuzz
from sentence_transformers import SentenceTransformer

# ============================================
# LOAD DATA AND MODELS
# ============================================
print("🔄 Loading retrieval dataset...")
with open("data/retrieval_dataset.json", "r", encoding="utf-8") as f:
    retrieval_dataset = json.load(f)
print(f"✅ Loaded {len(retrieval_dataset)} entries")

print("🔄 Loading aliases...")
with open("data/town_aliases.json", "r", encoding="utf-8") as f:
    alias_map = json.load(f)
print(f"✅ Loaded {len(alias_map)} aliases")

print("🔄 Loading embedding model...")
embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
print("✅ Model loaded")

# ============================================
# BUILD INDEXES
# ============================================
towns = [entry["town"] for entry in retrieval_dataset]
town_embeddings = embedder.encode(towns, convert_to_numpy=True, show_progress_bar=False)

town_index = {}
for entry in retrieval_dataset:
    key = entry["town"].lower().strip()
    town_index.setdefault(key, []).append(entry)

alias_index = {}
for entry in retrieval_dataset:
    town = entry["town"]
    alias_index[town.lower().strip()] = entry
    for alias, target in alias_map.items():
        if target == town:
            alias_index[alias.lower().strip()] = entry

print(f"✅ Indexes ready: {len(town_index)} towns, {len(alias_index)} aliases")

# ============================================
# RETRIEVAL FUNCTION
# ============================================
def retrieve_oriki(query, top_k=3):
    q = query.lower().strip()
    if q in alias_index:
        return {"method": "alias", "results": [alias_index[q]]}
    if q in town_index:
        return {"method": "exact", "results": town_index[q]}
    best_match, best_score = None, 0
    for town in town_index.keys():
        score = fuzz.ratio(q, town)
        if score > best_score:
            best_score, best_match = score, town
    if best_score >= 85:
        return {"method": "fuzzy", "corrected_to": best_match, "score": best_score, "results": town_index[best_match]}
    query_embedding = embedder.encode([query], convert_to_numpy=True)
    similarities = np.dot(town_embeddings, query_embedding.T).flatten()
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    suggestions = [
        {"town": retrieval_dataset[i]["town"], "id": retrieval_dataset[i]["id"], "score": float(similarities[i])}
        for i in top_indices
    ]
    return {"method": "semantic", "suggestions": suggestions}

# ============================================
# FLASK APP
# ============================================
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"name": "AI-Oríkì API", "version": "1.0", "entries": len(retrieval_dataset)})

@app.route("/app", methods=["GET"])
def serve_frontend():
    return send_file("index.html")

@app.route("/api/oriki", methods=["GET"])
def list_oriki():
    limit = int(request.args.get("limit", 100))
    results = [
        {"id": e["id"], "town": e["town"], "state": e["state"], "audio_type": e["audio_type"],
         "audio_file": e["audio_file"], "text_preview": e["text"][:120]}
        for e in retrieval_dataset
    ]
    return jsonify({"count": len(results), "results": results[:limit]})

@app.route("/api/oriki/<oriki_id>", methods=["GET"])
def get_oriki(oriki_id):
    for entry in retrieval_dataset:
        if entry["id"] == oriki_id:
            return jsonify({"success": True, "entry": entry})
    return jsonify({"success": False, "error": "Not found"}), 404

@app.route("/api/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"success": False, "error": "Empty query"}), 400
    result = retrieve_oriki(query)
    result["query"] = query
    result["success"] = True
    return jsonify(result)

@app.route("/api/audio/<path:filename>", methods=["GET"])
def serve_audio(filename):
    audio_path = os.path.join("audio", filename)
    if os.path.exists(audio_path):
        return send_file(audio_path)
    return jsonify({"error": "Audio not found"}), 404

@app.route("/api/feedback", methods=["POST"])
def feedback():
    return jsonify({"success": True, "message": "Thank you for your feedback!"})

# ============================================
# RUN
# ============================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)