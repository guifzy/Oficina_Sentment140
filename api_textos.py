from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# puxo o modelo já treinado e binzarizado, aqui contem todas as funçõe e parametros do modelo
model = joblib.load(r'C:\Users\guipi\Desktop\python\api oficina\Oficina_Sentment140\modelo.pkl')

# puxo o modelo de tfidf já treinado com o meu datasset previo, contendo os pesos atribuidos as palavras
tfidf_vectorizer = joblib.load(r'C:\Users\guipi\Desktop\python\api oficina\Oficina_Sentment140\vetor_tfidf.pkl')

# defino o resqueste para o caminho /predict, e recebo dados com metodo Post
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() # puxo os dados com minha request
        print("Recebido:", data)  
        text = data['text']
        
        if not text:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        # Transformar o texto usando o vetor TF-IDF
        text_tfidf = tfidf_vectorizer.transform([text])
        
        # Fazer a previsão
        prediction = model.predict(text_tfidf)
        
        if prediction[0] == 1:
            result = "Positive"
        else: result = "Negative"
        
        return jsonify({'prediction': result})
    
    except Exception as e:
        print("Erro:", str(e)) 
        return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
