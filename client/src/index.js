const { createApp } = Vue


const App = createApp({

  data() {

    return {

      queryText: '',
      googleAnswer: [],
      yandexAnswer: [],
      bingAnswer: [],
      youtubeAnswer: [],
      history: [],

    }

  },

  methods: {

    searchQueryText() {


      if (this.queryText != '') {
        request('/search', 'POST', { search: this.queryText }).then(data => {

          this.googleAnswer.length = 0

          this.yandexAnswer.length = 0

          this.bingAnswer.length = 0

          this.youtubeAnswer.length = 0


          this.googleAnswer.push(data.google)

          this.yandexAnswer.push(data.yandex)

          this.bingAnswer.push(data.bing)

          this.youtubeAnswer.push(data.youtube)



        })
      }
      else {
        alert('Please enter a query')
      }

    },

    saveHistory(link, title) {

      request('/saveHistory', 'POST', { link: link, title: title })

    },
    
    addoffline(title, link, query) {

      request('/addoffline', 'POST', { title: title, link: link, query: query })

    }

  }

})

App.mount('#vueapp')






async function request(url, method, data) {

  try {
    const headers = {}
    let body
    if (data) {
      headers['Content-Type'] = 'application/json'
      body = JSON.stringify(data)
    }

    const response = await fetch('http://127.0.0.1:5000' + url, {
      method,
      headers,
      body
    })

    return await response.json()

  }
  catch (e) {
    console.warn('Error:', e.message)
  }
}

