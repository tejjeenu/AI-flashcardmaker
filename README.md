# FlashcardMaker  

**FlashcardMaker** is an AI-powered tool that transforms exam specifications (GCSEs and A Levels) into ready-to-use flashcards for [Anki](https://apps.ankiweb.net/).  
It eliminates the time-consuming process of creating revision resources by automatically extracting examinable content, rephrasing it into questions, and exporting them into a CSV file.  

---

## 🎯 Problem  
Students often spend **hours creating revision resources** from textbooks, handouts, and notes.  
- Much of this content is **not directly examinable**, leading to wasted effort.  
- Resource creation time takes away from **actual learning and revision**.  

---

## 💡 Solution  
FlashcardMaker streamlines revision by:  
- **Detecting specification points** from official exam documents using AI.  
- **Converting them into flashcard questions** with the ChatGPT API.  
- **Exporting them to Anki-compatible CSV files** for instant use.  

This means students can spend **less time making resources** and more time **actively revising examinable content**.  

---

## 🛠️ Key Technologies  
- **YOLOv8** – Detects and crops specification points in PDFs.  
- **pytesseract** – Extracts text via OCR.  
- **ChatGPT API** – Rephrases specification points into effective flashcard questions.  
- **pdf2image** – Converts PDF pages into images.  
- **Tkinter** – Provides a simple user interface.  

---

## ⚙️ Workflow  
1. Upload exam specification PDF.  
2. AI model detects specification points and crops them.  
3. OCR extracts the text.  
4. ChatGPT API converts each point into a flashcard question.  
5. Export results into a CSV file ready for Anki.  

---

## ✅ Impact  
- Saves **hours of preparation time**.  
- Focuses only on **relevant exam content**.  
- Produces **high-quality flashcards instantly**, improving revision effectiveness.  

---

## 🔮 Future Plans  
- Faster performance with paid GPT API.  
- Support for more exam boards.  
- Automatic generation of flashcard answers.  
- Web-based version for broader accessibility.  

---

👉 With FlashcardMaker, students can focus less on **making revision resources** and more on **mastering exam content**.  









