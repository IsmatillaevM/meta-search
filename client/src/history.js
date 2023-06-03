const { createApp } = Vue

const App = createApp({

  data() {

    return {

      history: [],
      Searches: [],
      answers: [],
      offline: [],
      sites: [],


    }

  },

  methods: {

    getHistory() {
      this.history.length = 0
      this.Searches.length = 0
      this.answers.length = 0

      request('/getHistory', 'POST', { get: 'history' }).then(data => {

        this.history.push(data)

      })
    },
    getSearches() {
      this.history.length = 0
      this.Searches.length = 0
      this.answers.length = 0
      request('/getSearches', 'POST', { get: 'searchedHistory' }).then(data => {


        for (let i in data) {

          if (!this.Searches.includes(data[i].query)) {
            this.Searches.push(data[i].query);
          }
        }


      })
    },
    getAnswers(query) {
      this.history.length = 0
      this.Searches.length = 0
      this.answers.length = 0

      request('/getAnswers', 'POST', { query: query }).then(data => {
        for (let i in data) {
          if (query == data[i].query) {

            this.answers.push(data[i]);

          }
        }



      })
    },
    getoffline() {

      this.offline.pop()
      this.sites.pop()

      request('/getoffline', 'POST', { get: 'history' }).then(data => {

        this.offline.push(data)

      })
    },
    getofflinesite(title) {
      request('/getoffline', 'POST', { get: 'history' }).then(data => {
        this.offline.pop()
        this.sites.pop()

        for (let i in data) {

          if (title == data[i].title) {
            
            this.sites.push(data[i].body)  
            
           
          }
        }

      })
    }

  },

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
