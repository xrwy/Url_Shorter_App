from flask import Flask, render_template, request
import pyshorteners

# successfly not : adfly, bitly, clckru, cuttly, gitio: for github, nullpointer, owly, qpsru, post, shortcm, tinycc
# successfly : chilpit, dagd, isgd, osdb, tinyurl  16

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def main():
    return render_template('url_shorter.html')

@app.route('/url_shorter_result', methods = ['GET','POST'])
def urlShorterResult():
    global info
    full = []
    if request.method == 'POST':
        address = request.form['address']
        type_ = request.form['type']
        
        if address == '' or type_ == '' or type_ == 'Type':
            return 'Do Not Leave The Fields Blank.'

        addreses = address.split(',')

        if type_ == 'tinyurl':
            if len(addreses) == 1:
                info = []
                shortened = pyshorteners.Shortener()
                try:
                    ShortenedLink = shortened.tinyurl.short(address)
                    full.append([address, ShortenedLink])
                    
                    return render_template('url_shorter_result.html', value = full, info = 0)

                except Exception as e:
                    info_ = '{}. An error occurred in the link. HTTP Connection'.format(1)
                    info.append([address,info_])
                    return render_template('url_shorter_result.html', value = full, info = info)
            else:
                info = []
                counter = 1
                for addres in addreses:
                    shortened = pyshorteners.Shortener()
                    try:
                        ShortenedLink = shortened.tinyurl.short(addres)
                        full.append([addres, ShortenedLink])
                    except Exception as e:
                        info_ = '{}. An error occurred in the link. HTTP Connection'.format(counter)
                        info.append([addres,info_])

                    counter += 1

                if len(info) == 0:
                    info = 0
                else:
                    pass

                return render_template('url_shorter_result.html', value = full, info = info)
    

        elif type_ == 'osdb':
            if len(addreses) == 1:
                info = []
                shortened = pyshorteners.Shortener()
                try:
                    ShortenedLink = shortened.osdb.short(address)
                    full.append([address, ShortenedLink])

                    return render_template('url_shorter_result.html', value = full, info = 0)
                except Exception as e:
                    info_ = '{}. An error occurred in the link. HTTP Connection'.format(1)
                    info.append([address,info_])
                    return render_template('url_shorter_result.html', value = full, info = info)

            else:
                info = []
                counter = 1
                for addres in addreses:
                    shortened = pyshorteners.Shortener()
                    try:
                        ShortenedLink = shortened.osdb.short(addres)
                        full.append([addres, ShortenedLink])
                    except Exception as e:
                        info_ = '{}. An error occurred in the link. HTTP Connection'.format(counter)
                        info.append([addres,info_])
                        
                    counter += 1

                if len(info) == 0:
                    info = 0
                else:
                    pass

                return render_template('url_shorter_result.html', value = full, info = info)


        elif type_ == 'isgd':
            if len(addreses) == 1:
                info = []
                shortened = pyshorteners.Shortener()
                try:
                    ShortenedLink = shortened.isgd.short(address)
                    full.append([address, ShortenedLink])
                    
                    return render_template('url_shorter_result.html', value = full, info = 0)
                except Exception as e:
                    info_ = '{}. An error occurred in the link. HTTP Connection'.format(1)
                    info.append([address,info_])
                    return render_template('url_shorter_result.html', value = full, info = info)

            else:
                info = []
                counter = 1
                for addres in addreses:
                    shortened = pyshorteners.Shortener()
                    try:
                        ShortenedLink = shortened.isgd.short(addres)
                        full.append([addres, ShortenedLink])
                    except Exception as e:
                        info_ = '{}. An error occurred in the link. HTTP Connection'.format(counter)
                        info.append([addres,info_])

                    counter += 1

                if len(info) == 0:
                    info = 0
                else:
                    pass

                return render_template('url_shorter_result.html', value = full, info = info)


        elif type_ == 'dagd':
            if len(addreses) == 1:
                info = []
                shortened = pyshorteners.Shortener()
                try:
                    ShortenedLink = shortened.dagd.short(address)
                    full.append([address, ShortenedLink])
                    
                    return render_template('url_shorter_result.html', value = full, info = 0)
                except Exception as e:
                    info_ = '{}. An error occurred in the link. HTTP Connection'.format(1)
                    info.append([address,info_])
                    return render_template('url_shorter_result.html', value = full, info = info)

            else:
                info = []
                counter = 1
                for addres in addreses:
                    shortened = pyshorteners.Shortener()
                    try:
                        ShortenedLink = shortened.dagd.short(addres)
                        full.append([addres, ShortenedLink])
                    except Exception as e:
                        info_ = '{}. An error occurred in the link. HTTP Connection'.format(counter)
                        info.append([addres,info_])

                    counter += 1

                if len(info) == 0:
                    info = 0
                else:
                    pass

                return render_template('url_shorter_result.html', value = full, info = info)


        elif type_ == 'chilpit':
            if len(addreses) == 1:
                info = []
                shortened = pyshorteners.Shortener()
                try:
                    ShortenedLink = shortened.chilpit.short(address)
                    full.append([address, ShortenedLink])

                    return render_template('url_shorter_result.html', value = full, info = 0)
                except Exception as e:
                    info_ = '{}. An error occurred in the link. HTTP Connection'.format(1)
                    info.append([address,info_])
                    return render_template('url_shorter_result.html', value = full, info = info)

            else:
                info = []
                counter = 1
                for addres in addreses:
                    shortened = pyshorteners.Shortener()
                    try:
                        ShortenedLink = shortened.chilpit.short(addres)
                        full.append([addres, ShortenedLink])

                    except Exception as e:
                        info_ = '{}. An error occurred in the link. HTTP Connection'.format(counter)
                        info.append([addres,info_])

                    counter += 1

                if len(info) == 0:
                    info = 0
                else:
                    pass

                return render_template('url_shorter_result.html', value = full, info = info)

    else:
        return 'For post requests only.'

if __name__ == '__main__':
	app.run(debug=True)
