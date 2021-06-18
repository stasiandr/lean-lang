import Vue from 'vue'
import Vuex from 'vuex'
import auth from './auth'
import modal from './modal'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    auth,
    modal,
  },
})
