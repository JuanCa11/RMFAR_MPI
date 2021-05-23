import flask
import pickle
from flask import jsonify
from flask import request
from flask_cors import CORS
from preprocess.preprocess import Preprocess
from preprocess.utils import dict_transpose
from preprocess.settings import WILDCARDS, SANITY_MSG, PARSE_MONTH

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/recomendaciones', methods=['GET'])
def recomendations():
    data_dict = request.args.to_dict(flat=True)
    response = recomendation_process(data_dict)
    return jsonify(response)


def recomendation_process(data):
    pred, new_rules = get_new_rules_from_recommender(data)
    
    dict_res = {'pred': pred[0], 'score': pred[1]}
    wildcards_dict = dict_transpose(WILDCARDS)
    recommendations = []
    
    for _, row in new_rules.iterrows():
        dict_rec = {}
        feature_wildcard = wildcards_dict[row['wildcard']]
        new_item = None
        for item in list(row['new_rule']):
            if item in wildcards_dict:
                if wildcards_dict[item] == feature_wildcard:
                    new_item = item
                    break
        
        old_item = row['wildcard'] if feature_wildcard != 'MES' else PARSE_MONTH[row['wildcard']]
        new_item = new_item if feature_wildcard != 'MES' else PARSE_MONTH[new_item]
        if new_item:
            si = f"{SANITY_MSG[feature_wildcard]} {old_item}"
            luego = f'{new_item}'
            #msg = f"Si usted cambia {SANITY_MSG[feature_wildcard]} {old_item} por {new_item}"
        else:
            si = f"{SANITY_MSG[feature_wildcard]} {old_item}"
            luego = f"{SANITY_MSG[feature_wildcard]}"
            #msg = f"Si usted cambia {SANITY_MSG[feature_wildcard]} {old_item} por cualquier {SANITY_MSG[feature_wildcard]}"
        dict_rec['if'] = si
        dict_rec['then'] = luego
        dict_rec['score'] = pred[1] - row['diff']
        recommendations.append(dict_rec)

    dict_res['recommendations'] = recommendations
    return dict_res


def get_new_rules_from_recommender(data):
    with open('api/pickles/recommenderV1.pickle', 'rb') as handle:
        recommender = pickle.load(handle)

    preprocess = Preprocess()
    preprocess.preprocess_data(data)
    raw_data = preprocess.fuzzify_data()

    pred = recommender.predict_proba(raw_data)
    trigger_rules = recommender._trigger_rules
    new_rules = recommender.get_new_rules(trigger_rules).loc[0:9]
    return pred, new_rules

app.run()