import Vue from 'vue'
import Vuetify from 'vuetify/lib/framework'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#9652ff',
        secondary: '#6c757d',
        success: '#3cd1c2',
        info: '#ffaa2c',
        accent: '#3ea2fb',
        error: '#f83e70',
        petrol: '#17a499',
        background: '#F5F5F5',
      },
    },
    options: {
      customProperties: true,
    },
  },
})
