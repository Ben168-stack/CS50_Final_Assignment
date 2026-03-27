from website import create_app

app = create_app()
print("Server Has Started ")

if __name__ == "__main__":
    app.run(debug=True)