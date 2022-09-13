from distutils.log import debug
from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/email_val/<string:em>')
def email_val(em):
    k, j, d = 0, 0, 0
    if len(em) >= 6:
        if em[0].isalpha():
            if ("@" in em) and (em.count('@') == 1):
                if (em[-4] == '.') ^ (em[-3] == '.'):
                    for i in em:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if (k == 1) or (j == 1) or (d == 1):
                        result={
                            "1.E-Mail": em,
                            "2.Valid": False
                        }
                    else:
                        em=str(em)
                        #For Domain Name 
                        dn=em[em.index('@')+1:]
                        # For Username
                        un=em.split("@")
                        result={
                            "1.E-Mail": em,
                            "2.Valid": True,
                            "3.User_name": un[0],
                            "4.Domain_Name": dn
                        }
                else:
                    result={
                        "1.E-Mail": em,
                        "2.Valid": False
                    }
            else:
                result={
                    "1.E-Mail": em,
                    "2.Valid": False
                }
        else:
            result={
                "1.E-Mail": em,
                "2.Valid": False
            }
    else:
        result={
            "1.E-Mail": em,
            "2.Valid": False
        }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)
