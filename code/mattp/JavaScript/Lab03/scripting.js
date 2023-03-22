axios({
    method: 'get',
    url: 'https://favqs.com/api/qotd',
    headers: {
        'x-api-key': 'api_key'
    }
}).then((response) => {
    console.log(response.data)
})