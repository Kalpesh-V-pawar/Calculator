from flask import Flask, request, jsonify, render_template_string, redirect, url_for, render_template




app = Flask(__name__)


HTML_template = """
<!DOCTYPE html>
<html lang="en">
<html>
    <head>
        <title>Hiii</title>
    </head>
    <body>
      <form method = "POST">
         <label for="first1">inputt1:</label>
         <input type="text" id="first1" name="first1" required>
         <input type="text" id="second1" name="second1" required>
         <input type="text" id="op" name="op" required>
         <button type = "submit">Submit</button>
      </form>  
      
      {% if output is not none %}
      <h2>Result: {{ hier }}</h2>
      {% endif %}

    </body>

</html>





"""

# first = int(input("input first number:"))
# Second = int(input("input second number:"))
# operation = input("input your operation:")

# first = int(first2)
# Second = int(second2)
# operation = op


# if operation == "+":
#   output = first + Second

# elif operation == "-":
#    output = first - Second

# elif operation == "*":
#    output = first * Second

# elif operation == "/":
#    output = first / Second
# else :
#   print("invalid operation")
  
# out1 = f"the output is {output}"
# print(out1)





@app.route("/", methods=["GET", "POST"])
def oper():
    output = None  # Initialize output for the template
    
    if request.method == "POST":
        
            # Retrieve form data
            first2 = request.form.get("first1")
            second2 = request.form.get("second1")
            oper2 = request.form.get("op")
            

                # Convert inputs to numbers
            first = float(first2)
            second = float(second2)
            operation = oper2.strip()

                # Perform the calculation based on the operation
            if operation == "+":
                    output = first + second
            elif operation == "-":
                    output = first - second
            elif operation == "*":
                    output = first * second
            else:
                    output = "Invalid operation. Use +, -, *, or /."
        
    # Render the HTML template with the output
    return render_template_string(HTML_template, hier=output)


if __name__ == '__main__':
    
    app.run(debug=True)
