from flask import Flask, request, jsonify
# pip3 install googletrans
from googletrans import Translator
## pip3 install googletrans

t = Translator()
app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    data_to_send = {
        "type" : "text",
        "buttons":[]
    }
    
    return jsonify(data_to_send)

## 메세지 전달
def send_message(text):
    
    return jsonify({'message': {"text":text}})

## 메시지 받아서 전달 (KO->EN으로 변경)
@app.route('/message', methods=['POST'])
def Message():
    data_received = request.get_json()
    content = data_received['content']
    print(data_received)
    translated_text = t.translate(content, src='ko', dest='en').text
    return send_message(translated_text)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
        
##https://center-pf.kakao.com/login 에서 봇 세팅
