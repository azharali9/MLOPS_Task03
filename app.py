from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def input_output():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return f'You entered: {user_input}'
    
    return '''
        <form method="post">
            <label for="user_input">Enter something:</label><br>
            <input type="text" id="user_input" name="user_input"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
