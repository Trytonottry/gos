from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    #Обработка заказа
    departure = request.form['departure']
    destination = request.form['destination']
    # ... Обработка заказа, вызов алгоритма ...
    return jsonify({'message': 'Заказ принят'}) #Ответ в формате JSON
  return render_template('index.html') #Отобразить форму заказа

if __name__ == '__main__':
  app.run(debug=True)
