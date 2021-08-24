from flask import Flask , render_template , request , redirect
import csv 

app = Flask(__name__)

@app.route('/<string:page_name>')
def hello_world(page_name):
    return render_template(page_name)


@app.route('/')
def hello_world2():
    return render_template('index.html')

def save (data ):
    with open ('dataBase.txt' , mode = 'a' ) as dataBase :
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = dataBase.write(f'\n  {email} ,  {subject}   , {message}') # we can do it without file ( the first onein this line)

def save_csv (data) : 
    with open ('dataBase2.csv' , newline='',mode ='a') as dataBase2 :
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer( dataBase2 , delimiter=',', quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email , subject , message])

@app.route('/submet_form', methods=['POST', 'GET'])
def submet_form():
    if request.method == 'POST': # we wrote in the html the method should be post after submitting the form
        #because we wrote it in the contact.html  in /submet_form  in the header of it you will see the request.method is really post
            # print( request.form['email'] )# in the developer tools there are the date. with it's names so you only take it from there ( browser) . we named it in the contact so it's name will appear there
            try : 
                data = request.form.to_dict() # it will take the whole info in clear way
                save(data)
                save_csv(data)
                print(data) 
            
            # هي قبل ما ترجع قالب الشكر الثانمس اش تي ام ال اخذت الشي اللي تريده ثم غيرته 
            # اذا تريد تشوف المعلومات بالديفيلوبر تولس اعمل
            #return 'thanks very much'      
# سؤال مهم جدن اذ الرمز راح يظل بالبراوزر ما ممكن اعل ريكويست و اخذ الرمز و اخرتق الرجل اللطيف
                return redirect('/thanks.html') # in the header the content type is application/x-www-form-urlencoded and it's stander for forms in Html
            except : 
                return 'did not save to data base there is errors'
    else:
            return ' some thing is wrong'
    