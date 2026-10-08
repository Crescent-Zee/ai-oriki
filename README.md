# 🎵 AI-Oríkì — Yoruba Eulogy Retrieval and Chanting System

> An AI-powered system for compiling, retrieving, and chanting verified Yoruba Oríkì (oral praise poetry).

---

## 📖 About the Project

**AI-Oríkì** is a final-year research project from the **Department of Computer Science, University of Ibadan**, designed to preserve and disseminate Yoruba Oríkì — a revered form of oral praise poetry that expresses identity, lineage, history, and cultural pride.

Unlike text-generation approaches, this system is **retrieval-based**: it does not invent Oríkì. It retrieves **verified, source-attributed Oríkì** from a curated dataset and presents them as both text and audio (real recordings or AI-generated chanting).

**Author:** Oladimeji Zainab Olamide (254161)  
**Supervisor:** Prof. S. O. Akinola  
**Institution:** University of Ibadan, Nigeria  
**Year:** 2026

---

## ✨ Key Features

- 🎙️ **40 verified Oríkì entries** from 7 states across Yoruba Land
- 🔊 **Hybrid audio strategy** — real field recordings preferred, neural TTS as fallback
- 🔍 **Four-stage AI retrieval** — alias, exact, fuzzy, and Transformer-based semantic search
- 🎤 **100% performer attribution** — every recording credits its chanter
- 📖 **Full source transparency** — every Oríkì traces back to its origin
- 🖥️ **Browse + search interface** — music-app-style grid with AI-powered search
- 🗣️ **Not-found handling** — semantically similar suggestions instead of dead ends

🏗️ System Architecture

📊 Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Oríkì entries | 40 |
| 🎙️ Real field recordings | 30 (75%) |
| 🔊 AI-generated (TTS) | 10 (25%) |
| Unique towns | 40 |
| States covered | 7 (Oyo, Osun, Ogun, Ondo, Ekiti, Lagos, Kwara) |

Performer attribution:
| Performer | Number of Recordings |
|-----------|---------------------|
| Asake Akewi | 22 |
| Ajani Akewi | 5 |
| Tife Alare | 1 |
| Rodiat Elere | 1 |
| AI-generated (MMS-TTS) | 10 |


 🚀 How to Run Locally

Prerequisites
- Python 3.10+
- pip

Academic Context
This project demonstrates:

AI for low-resource languages — Transformer-based semantic retrieval for Yoruba

Cultural preservation — verified corpus with 100% source attribution

Hybrid audio generation — real recordings + neural TTS

Ethical AI — performer attribution, cultural data sovereignty

Reproducibility — open-source, documented, deployable

Evaluation pillars:

Corpus Fidelity — 100% source attribution

Mean Opinion Score (MOS) — 4.67/5 for real recordings, 3.96/5 for TTS

Expert Cultural Validation — 4.60/5 average across 5 criteria

User Feedback — SUS 82.5, NPS 55

⚠️ Known Limitations
Dataset size: 40 entries — expandable through additional field collection

Render deployment: Free tier (512 MB RAM) insufficient for PyTorch + Transformer models

ngrok demo: URLs expire and require Colab to stay connected

TTS quality: MMS-TTS lacks chant-style prosody compared to real recordings

🔮 Future Work
Fine-tune TTS on real recordings — adapt facebook/mms-tts-yor to match chanter style

Voice cloning — use F5-TTS Yoruba or VoxCPM2-Yoruba for voice preservation

Expand corpus — collect additional Oríkì from more towns

Permanent deployment — migrate to a paid cloud tier or dedicated server

Mobile app — package as Android/iOS for wider reach

🙏 Acknowledgements
Special thanks to the real chanters who performed these Oríkì:

Asake Akewi — 22 recordings across Oyo, Osun, Ogun, Lagos, and Kwara

Ajani Akewi — 5 recordings from Osun and Ogun

Tife Alare — 1 recording from Oyo

Rodiat Elere — 1 recording from Kwara

And to Prof. S. O. Akinola for supervision and guidance.

📄 License
This project is licensed under the MIT License — free to use for educational and cultural purposes. The Oríkì texts and audio recordings remain the intellectual property of their original performers and communities.

📞 Contact
Oladimeji Zainab Olamide
Department of Computer Science
University of Ibadan, Nigeria
GitHub: @Crescent-Zee
pip install -r requirements.txt
python app.py
