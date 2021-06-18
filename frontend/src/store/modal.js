const state = {
  menu: {
    isOpened: false,
  },
}

const getters = {
  menuIsOpened: (state) => {
    return state.menu.isOpened
  },
}

const actions = {
  toggleMenu(context) {
    context.commit('toggleMenu')
  },
  setMenuOpened(context, open) {
    context.commit('setMenuOpened', open)
  },
}

const mutations = {
  toggleMenu(state) {
    state.menu.isOpened = !state.menu.isOpened
  },
  setMenuOpened(state, open) {
    state.menu.isOpened = open
  },
}

export default {
  namespaced: true,
  actions,
  getters,
  mutations,
  state,
}
