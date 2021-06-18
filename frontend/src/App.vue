<template>
  <v-app :style="{ background: $vuetify.theme.themes[theme].background }">
    <nav v-if="isLoggedIn">
      <Navbar />
      <Appbar />
    </nav>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar'
import Appbar from './components/Appbar'
import { mapGetters } from 'vuex'

export default {
  components: {
    Navbar,
    Appbar,
  },
  name: 'App',
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? 'dark' : 'light'
    },
    ...mapGetters('auth', ['isLoggedIn']),
  },
}
</script>
