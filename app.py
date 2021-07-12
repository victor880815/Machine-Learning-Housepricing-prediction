from flask import Flask, jsonify, request
import requests
import json
import os
import pickle

app = Flask(__name__)
#json 中文回傳
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return 'Welcome to Taichung House Price Prediction Model API !'

def model_file(city, district, year, type_):
    path = 'model'
    files = os.listdir(path)
    for file in files:
        if (city in file) and (district in file) and (year in file) and (f'_{type_}_' in file):
            model_filename = f'{path}/{file}'
            model = pickle.load(open(model_filename, 'rb'))
            return model
    return None

def price_predict(model, lat, lon, bs=0.5, g=0, l=0, room=3, living=2, toilet=2, s=50, real_s=None):
    #calculate bs from s and real_s
    if real_s != None:
        bs = real_s / s

    #auto calculate real_s
    if real_s == None:
        real_s = bs * s

    data = {
        'bs':bs,#主建物比
        'g':g,#屋齡
        'l':l,#車位數
        'lat':lat,#緯度
        'lon':lon,#經度
        's':s,#總坪數
        'room':room,#房
        'living':living,#廳
        'toilet':toilet,#衛
        'real_s':real_s#主建物坪數
    }
    data = list(data.values())
    result = model.predict(data)[0]
    return result
    
@app.route('/model_api', methods=['GET', 'POST'])
def model_api():
    try:
        #read model
        city = request.args.get('city')
        district = request.args.get('district')
        year = str(request.args.get('year'))
        model_p = model_file(city=city, district=district, year=year, type_='p')
        model_tp = model_file(city=city, district=district, year=year, type_='tp')
        #specs
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        bs = float(request.args.get('bs', default = 0.5))
        g = int(request.args.get('g', default = 0))
        l = int(request.args.get('l', default = 0))
        room = int(request.args.get('room', default = 3))
        living = int(request.args.get('living', default = 2))
        toilet = int(request.args.get('toilet', default = 2))
        s = float(request.args.get('s', default = 50))
        real_s = float(request.args.get('real_s', default = bs * s))
        #predict p and tp
        p = price_predict(model_p, lat=lat, lon=lon, bs=bs, g=g, l=l, room=room, living=living, toilet=toilet, s=s, real_s=real_s)
        tp = price_predict(model_tp, lat=lat, lon=lon, bs=bs, g=g, l=l, room=room, living=living, toilet=toilet, s=s, real_s=real_s)
        #result
        data = {
            'p':int(p),
            'tp':int(tp)
        }
        return jsonify(data)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()