
@app.route('/users_show/<int:user_id>')
def show_city(user_id):
    user = get(f'http://localhost:5000/api/users/{user_id}').json()
    response = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={user['users']['city_from']}&format=json")
