<template>
  <v-app-bar app>
    <v-app-bar-nav-icon
      class="grey--text"
      @click="toggleMenu"
      v-if="isLoggedIn"
    />
    <v-tollbar-title class="text-uppercase grey--text">
      <span class="font-weight-light">LEAN</span>
      <span>LANG</span>
    </v-tollbar-title>
    <v-spacer />
    <v-text class="mr-4">{{ user.first_name }} {{ user.last_name }}</v-text>
    <v-btn outlined @click="logout">
      <span>SIGN OUT</span>
      <v-icon right>mdi-logout-variant</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('auth', ['user', 'isLoggedIn']),
  },
  methods: {
    ...mapActions('modal', ['toggleMenu']),
    ...mapActions('auth', ['logout']),
  },
}
</script>
