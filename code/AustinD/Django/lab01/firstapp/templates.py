<h1>Grocery List</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Save</button>
        </form>
        <h2>Incomplete Items</h2>
        <ul>
            {% for item in items %}
                <li>{{ item.description }}</li>
            {% endfor %}
        </ul>
        <h2>Complete Items</h2>
        <ul>
            {% for item in completed_items %}
                <li>{{ item.description }}</li>
            {% endfor %}
        </ul>