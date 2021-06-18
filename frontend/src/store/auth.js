import axios from 'axios'
import router from '../router'

const state = {
  auth: {},
  user: {
    username: 'stasiandr',
    first_name: 'Stas',
    last_name: 'Datsuk',
    email: 'stasiandr@gmail.com',
    profile_pic: '/tmp-avatar.png',
  },
}

const getters = {
  user: (state) => {
    return state.user
  },
  isLoggedIn: (state) => {
    return 'access' in state.auth
  },
}

const actions = {
  async retriveUserData({ commit }, id) {
    await axios
      .get(`/api/auth/users/${id}/`)
      .then((res) => {
        commit('updateUser', res.data)
        router.push('/account')
      })
      .catch((error) => {
        console.log(error)
      })
  },

  async login({ commit, dispatch }, credentials) {
    await axios
      .post('/api/auth/token/', credentials)
      .then((res) => {
        commit('updateCreds', res.data)
        dispatch('retriveUserData', res.data.id)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  async register(_, data) {
    console.log(data)
    await axios
      .post('/api/auth/users/', data)
      .then(() => {
        router.push('/login')
      })
      .catch((error) => {
        console.log(error)
      })
  },
  logout({ commit }) {
    commit('dropCreds', {})
    router.push('/')
  },
}

const mutations = {
  dropCreds(state) {
    state.auth = {}
    axios.defaults.headers.common['Authorization'] = ''
  },
  updateCreds(state, res) {
    state.auth = { ...state.auth, ...res }
    axios.defaults.headers.common['Authorization'] = `Bearer ${res.access}`
  },
  updateUser(state, user) {
    state.user = user
  },
}

export default {
  namespaced: true,
  actions,
  getters,
  mutations,
  state,
}
