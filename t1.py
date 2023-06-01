import tkinter as tk
from tkinterweb import HtmlFrame

# Create the main Tkinter window
root = tk.Tk()
root.title("React Toastify with Tkinter")
root.geometry("400x300")

# Create an HtmlFrame to embed the web content
frame = HtmlFrame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Load the React app into the HtmlFrame
frame.set_content("""
<!DOCTYPE html>
<html>
<head>
  <title>React Toastify</title>
  <meta charset="UTF-8">
  <script src="https://unpkg.com/react/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/react-toastify/dist/ReactToastify.js"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    // Your React component code here
    ${your_react_component_code}
    ReactDOM.render(<App />, document.getElementById('root'));
  </script>
</body>
</html>
""".replace("${your_react_component_code}", open("your_react_component_file.js").read()))

root.mainloop()
